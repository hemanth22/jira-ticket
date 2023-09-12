import requests
from requests.auth import HTTPBasicAuth

# Jira API endpoint for creating an issue
url = "https://bitroidbitra.atlassian.net/rest/api/2/issue/"

# Provide your Jira credentials
username = os.environ.get('JIRA_USER')
password = os.environ.get('JIRA_ACCESS')

# Create a JSON payload for the new issue
payload = {
    "fields": {
        "project": {
            "key": "DEV"
        },
        "summary": "creating ticket through python through github",
        "description": "creating ticket through python",
        "issuetype": {
            "name": "Task"
        }
    }
}

# Send a POST request to create the issue
response = requests.post(
    url,
    auth=HTTPBasicAuth(username, password),
    json=payload
)

# Check the response status code
if response.status_code == 201:
    print("Issue created successfully.")
    issue_key = response.json()["key"]
    print("Issue key:", issue_key)
else:
    print("Failed to create issue. Status code:", response.status_code)
    print("Response:", response.text)
