import requests
import os

# Jira API endpoint for creating an issue
url = "https://bitroidbitra.atlassian.net/rest/api/2/issue/"

# Provide your Jira credentials
username = os.environ.get('JIRA_USER')
password = os.environ.get('JIRA_ACCESS')

# Create a JSON payload for the new issue
payload = {
    "fields": {
        "project": {
            "key": "DD"
        },
        "summary": "Issue summary",
        "description": "Issue description",
        "issuetype": {
            "name": "Task"
        }
    }
}

# Send a POST request to create the issue
response = requests.post(
    url,
    auth=(username, password),
    json=payload
)

# Check the response status code
if response.status_code == 201:
    print("Issue created successfully.")
    issue_key = response.json()["key"]
    print("Issue key:", issue_key)
    # Perform the custom button action
    custom_action_url = f"https://bitroidbitra.atlassian.net/rest/api/2/issue/{issue_key}/your-custom-action"
    response = requests.post(
        custom_action_url,
        auth=(username, password)
    )
    if response.status_code == 204:
        print("Custom action performed successfully.")
    else:
        print("Failed to perform the custom action. Status code:", response.status_code)
else:
    print("Failed to create issue. Status code:", response.status_code)
    print("Response:", response.text)
