# GitHub Repository Analyzer

## Overview
The **GitHub Repository Analyzer** is a Python-based tool designed to analyze GitHub repositories and assess their reliability based on various metrics. It provides insights into repository activity, contributor engagement, and code quality, helping developers and teams determine whether a project is legitimate or potentially risky.

## Key Features
- **User-Friendly GUI**: Built with Tkinter for easy input and visualization.
- **Risk Analysis**: Evaluates repositories based on metrics like stars, forks, commits, and contributors.
- **Description Match Assessment**: Compares repository metadata with user-provided descriptions to detect inconsistencies.
- **Recent Activity Tracking**: Displays the date of the last commit and checks for signs of abandonment.
- **Community Engagement**: Analyzes contributors, open issues, and commit frequency.
- **Code Structure Inspection**: Traverses repository directories to identify patterns.

## Metrics Analyzed
- **Stars & Forks**: Measures popularity and adoption.
- **Commits**: Evaluates code evolution and maintenance activity.
- **Contributors**: Assesses collaboration and code review practices.
- **Issues**: Highlights outstanding problems or maintenance gaps.
- **Last Commit Date**: Detects inactivity or potential abandonment.
- **Language Match**: Checks whether the language aligns with the project description.
- **Keyword Matching**: Analyzes keywords in descriptions and file structures for suspicious terms.

## Risk Assessment Criteria
- **Low Activity**: Few commits or contributors.
- **Abandonment Signs**: Long gaps since the last update.
- **Poor Engagement**: Minimal stars, forks, or pull requests.
- **Unclear Purpose**: Vague or mismatched descriptions.
- **Unusual Keywords**: Presence of terms like "pump", "dump", or "scam".
- **No License**: Lack of licensing information may indicate risks for reuse.

## Getting Started
### Prerequisites
- Python 3.x
- Libraries: `requests` and `tkinter` (pre-installed with Python).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ins6nity/BABIBUTERMINAL-AI-Agent.git
   cd BABIBUTERMINAL-AI-Agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python3 github_analyzer.py
   ```

## How to Use
1. Enter the GitHub repository URL.
2. Provide a description of the project.
3. Click **Analyze**.
4. Review the results, including:
   - General repository details.
   - Activity metrics and engagement.
   - Risk assessment and trustworthiness.

## Example Output
```
Analyzing repository: https://github.com/example/repo

Repository Information:
Name: Example Repo
Stars: 120
Forks: 30
Commits: 200
Contributors: 10
Issues: 2
Last Updated: 2024-01-10
Language: Python
Last Commit: 2024-01-10

Match Analysis: Strong alignment with description.
Trustworthiness: Appears trustworthy based on metrics.
```

## Limitations
- Requires an active internet connection to access GitHub API.
- May have rate limits on API calls if used extensively without authentication.

## Contributions
Contributions are welcome! Fork this repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---
**Note**: Use this tool as a reference and not as the sole criterion for evaluating repositories. Always perform manual reviews for final decisions.

