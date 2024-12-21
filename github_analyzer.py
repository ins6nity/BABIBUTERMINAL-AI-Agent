import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import requests
from concurrent.futures import ThreadPoolExecutor
import re

# Function to analyze the repository
def analyze_github_repo(repo_url):
    """
    Analyze a GitHub repository.
    """
    parts = repo_url.rstrip('/').split('/')
    if len(parts) < 2:
        return "Invalid GitHub link. Please provide a valid link."

    owner, repo = parts[-2], parts[-1]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/"

    def analyze_directory(url):
        results = {}
        response = requests.get(url)
        if response.status_code != 200:
            return results

        files = response.json()
        with ThreadPoolExecutor() as executor:
            futures = {}
            for file in files:
                if file['type'] == 'file':
                    results[file['path']] = file['download_url']
                elif file['type'] == 'dir':
                    sub_results = analyze_directory(file['url'])
                    results.update(sub_results)

        return results

    try:
        keyword_occurrences = analyze_directory(api_url)
        if keyword_occurrences:
            return keyword_occurrences
        else:
            return f"No files found in the repository."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to get repository information
def get_repo_info(repo_url):
    """
    Fetch general information about the repository.
    """
    parts = repo_url.rstrip('/').split('/')
    if len(parts) < 2:
        return "Invalid GitHub link. Please provide a valid link."

    owner, repo = parts[-2], parts[-1]
    repo_api_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(repo_api_url)
    if response.status_code != 200:
        return f"Error accessing repository info: {response.status_code}"

    repo_info = response.json()
    info = {
        "Name": repo_info.get("name", "N/A"),
        "Stars": repo_info.get("stargazers_count", 0),
        "Forks": repo_info.get("forks_count", 0),
        "Commits": get_commit_count(repo_url),
        "Contributors": get_contributor_count(repo_url),
        "Issues": get_open_issues(repo_url),
        "Last Updated": repo_info.get("updated_at", "N/A"),
        "Language": repo_info.get("language", "N/A"),
        "Description": repo_info.get("description", "N/A"),
        "Last Commit": get_last_commit(repo_url)
    }
    return info

# Function to get last commit date
def get_last_commit(repo_url):
    parts = repo_url.rstrip('/').split('/')
    owner, repo = parts[-2], parts[-1]
    commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(commits_url)
    if response.status_code != 200:
        return "Unavailable"

    commits = response.json()
    if commits:
        return commits[0]['commit']['committer']['date']
    return "No commits found"

# Additional repository checks
def get_commit_count(repo_url):
    parts = repo_url.rstrip('/').split('/')
    owner, repo = parts[-2], parts[-1]
    commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(commits_url)
    return len(response.json()) if response.status_code == 200 else 0

def get_contributor_count(repo_url):
    parts = repo_url.rstrip('/').split('/')
    owner, repo = parts[-2], parts[-1]
    contributors_url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    response = requests.get(contributors_url)
    return len(response.json()) if response.status_code == 200 else 0

def get_open_issues(repo_url):
    parts = repo_url.rstrip('/').split('/')
    owner, repo = parts[-2], parts[-1]
    issues_url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    response = requests.get(issues_url)
    return len(response.json()) if response.status_code == 200 else 0

# Tkinter UI Setup
root = tk.Tk()
root.title("GitHub Repository Analyzer")
root.geometry("600x600")

repo_label = tk.Label(root, text="Repository URL:")
repo_label.pack(pady=5)
repo_input = tk.Entry(root, width=80)
repo_input.pack(pady=5)

def analyze_action():
    repo_url = repo_input.get()

    if not repo_url:
        messagebox.showwarning("Input Error", "Repository URL is required!")
        return

    log_text.delete(1.0, tk.END)
    log_text.insert(tk.END, f"Analyzing repository: {repo_url}\n\n")

    repo_info = get_repo_info(repo_url)
    if isinstance(repo_info, dict):
        log_text.insert(tk.END, "Repository Information:\n")
        for key, value in repo_info.items():
            log_text.insert(tk.END, f"{key}: {value}\n")
    else:
        log_text.insert(tk.END, f"Error fetching repository information: {repo_info}\n\n")

analyze_button = tk.Button(root, text="Analyze", command=analyze_action)
analyze_button.pack(pady=10)

log_text = ScrolledText(root, width=70, height=20)
log_text.pack(pady=5)

root.mainloop()
