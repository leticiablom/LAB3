import csv
import requests
import os
import time

from datetime import datetime

# CONFIGURAÇÕES
GITHUB_TOKEN = "TOKEN AQUI"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# CAMINHOS
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INPUT_CSV = os.path.join(BASE_PATH, "results", "prs_filtered.csv")
OUTPUT_CSV = os.path.join(BASE_PATH, "results", "prs_enriquecidos.csv")

def get_pr_details(repo, pr_number):
    """Consulta detalhes do PR pela API do GitHub"""
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    timeline_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/timeline"

    pr_data = {}
    
    pr_response = requests.get(url, headers=HEADERS)
    if pr_response.status_code == 200:
        pr_json = pr_response.json()
        pr_data["files_changed"] = pr_json.get("changed_files", 0)
        pr_data["additions"] = pr_json.get("additions", 0)
        pr_data["deletions"] = pr_json.get("deletions", 0)
        pr_data["description_length"] = len(pr_json.get("body") or "")
    else:
        print(f" Erro ao buscar PR {repo}#{pr_number}")
        return None

    comments_response = requests.get(comments_url, headers=HEADERS)
    pr_data["comments"] = len(comments_response.json()) if comments_response.status_code == 200 else 0

    timeline_response = requests.get(timeline_url, headers={**HEADERS, "Accept": "application/vnd.github.mockingbird-preview"})
    participants = set()
    if timeline_response.status_code == 200:
        for event in timeline_response.json():
            if "actor" in event and event["actor"]:
                participants.add(event["actor"]["login"])
    pr_data["participants"] = len(participants)

    time.sleep(1) 

    return pr_data

def enriquecer_dataset():
    enriched_data = []

    with open(INPUT_CSV, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            repo = row["repo_name"]
            pr_number = row["pr_number"]

            print(f" Enriquecendo {repo}#{pr_number}...")
            pr_metrics = get_pr_details(repo, pr_number)

            if pr_metrics:
                enriched_row = {
                    **row,
                    **pr_metrics
                }
                enriched_data.append(enriched_row)

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as outfile:
        fieldnames = list(enriched_data[0].keys())
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_data)

    print(f"\n PRs enriquecidos salvos em: {OUTPUT_CSV}")

if __name__ == "__main__":
    enriquecer_dataset()
