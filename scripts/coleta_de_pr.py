import requests
import time
import csv
import os
from datetime import datetime, timedelta
from config import GITHUB_TOKEN

# Configurações da API do GitHub
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Criar a pasta results se não existir
RESULTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results"))
os.makedirs(RESULTS_PATH, exist_ok=True)

def get_top_repositories(limit=200):
    print("🔎 Buscando repositórios populares...")
    url = "https://api.github.com/search/repositories?q=stars:>10000&sort=stars&order=desc&per_page=100"
    repositories = []

    for page in range(1, (limit // 100) + 1):
        response = requests.get(f"{url}&page={page}", headers=HEADERS)
        if response.status_code == 200:
            data = response.json()["items"]
            repositories.extend(data)
        else:
            print(f"Erro ao buscar repositórios (página {page}): {response.status_code}")
            break
        time.sleep(1)

    return repositories[:limit]

def get_pull_requests(repo_full_name, min_prs=100):
    url = f"https://api.github.com/repos/{repo_full_name}/pulls?state=closed&per_page=100"
    pull_requests = []

    for page in range(1, 11):  # Máximo de 1000 PRs
        response = requests.get(f"{url}&page={page}", headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            pull_requests.extend(data)
            if len(data) < 100:
                break
        else:
            print(f" Erro ao buscar PRs para {repo_full_name} (página {page}): {response.status_code}")
            break
        time.sleep(1)

    if len(pull_requests) < min_prs:
        print(f"⚠️ {repo_full_name} ignorado: apenas {len(pull_requests)} PRs encontrados.")
        return []

    return pull_requests

def filter_pull_requests(repo_name, pull_requests):
    filtered_prs = []
    print(f"\n Coletando PRs de: {repo_name}")

    for pr in pull_requests:
        pr_number = pr["number"]
        created_at = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        closed_at_str = pr.get("closed_at") or pr.get("merged_at")

        if not closed_at_str:
            continue

        closed_at = datetime.strptime(closed_at_str, "%Y-%m-%dT%H:%M:%SZ")
        duration = closed_at - created_at

        if duration < timedelta(hours=1):
            continue

        # Verifica se possui review (não comentários simples)
        review_url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}/reviews"
        response = requests.get(review_url, headers=HEADERS)

        if response.status_code == 200:
            reviews = response.json()
            if len(reviews) == 0:
                continue
            else:
                filtered_prs.append({
                    "repo_name": repo_name,
                    "pr_number": pr_number,
                    "created_at": created_at,
                    "closed_at": closed_at,
                    "duration": duration,
                    "reviews_count": len(reviews)
                })
        time.sleep(1)

    return filtered_prs

def salvar_em_csv(prs, filepath):
    """ Salva os PRs em um arquivo CSV """
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["repo_name", "pr_number", "created_at", "closed_at", "duration", "reviews_count"])
        
        for pr in prs:
            writer.writerow([
                pr["repo_name"], pr["pr_number"], 
                pr["created_at"], pr["closed_at"], 
                pr["duration"], pr["reviews_count"]
            ])

    print(f"\n PRs salvos em '{filepath}' (total: {len(prs)})")

def salvar_repositorios(repositories, filepath):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["full_name", "html_url", "stargazers_count", "language"])
        for repo in repositories:
            writer.writerow([
                repo["full_name"],
                repo["html_url"],
                repo["stargazers_count"],
                repo["language"]
            ])
    print(f" Repositórios salvos em '{filepath}'")

def main():
    LIMITE_TOTAL_PRS_VALIDOS = 200
    repositories = get_top_repositories()
    all_filtered_prs = []
    csv_path = os.path.join(RESULTS_PATH, "prs_filtered.csv")
    repos_csv_path = os.path.join(RESULTS_PATH, "repositorios_selecionados.csv")

    try:
        for repo in repositories:
            if len(all_filtered_prs) >= LIMITE_TOTAL_PRS_VALIDOS:
                break  

            repo_name = repo["full_name"]
            prs = get_pull_requests(repo_name)
            if not prs:
                continue

            filtered_prs = filter_pull_requests(repo_name, prs)

            for pr in filtered_prs:
                if len(all_filtered_prs) < LIMITE_TOTAL_PRS_VALIDOS:
                    all_filtered_prs.append(pr)
                else:
                    break

    except KeyboardInterrupt:
        print("\n Interrupção detectada pelo usuário. Salvando PRs já coletados...")

    finally:
        salvar_em_csv(all_filtered_prs, csv_path)
        salvar_repositorios(repositories, repos_csv_path)

if __name__ == "__main__":
    main()
