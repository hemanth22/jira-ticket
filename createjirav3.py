import requests
import os

# Jira API endpoint for creating an issue
create_url = "https://bitroidbitra.atlassian.net/rest/api/2/issue/"

# Jira API endpoint for transitioning the issue
transition_url = "https://bitroidbitra.atlassian.net/rest/api/2/issue/{issue_key}/transitions"

# Provide your Jira credentials
username = os.environ.get('JIRA_USER')
password = os.environ.get('JIRA_ACCESS')

# Create a JSON payload for the new issue
create_payload = {
    "fields": {
        "project": {
            "key": "DEV"
        },
        "summary": "Issue summary",
        "description": "Issue description",
        "issuetype": {
            "name": "Task"
        }
    }
}

# Send a POST request to create the issue
create_response = requests.post(
    create_url,
    auth=(username, password),
    json=create_payload
)

# Check the response status code
if create_response.status_code == 201:
    print("Issue created successfully.")
    issue_key = create_response.json()["key"]
    print("Issue key:", issue_key)

    # Transition the issue to the desired workflow state
    transition_payload = {
        "transition": {
            "id": "TRANSITION_ID"
        }
    }

    # Replace TRANSITION_ID with the ID of the desired workflow transition
    # You can find the transition ID by inspecting the workflow configuration or using the Jira REST API

    transition_url = transition_url.format(issue_key=issue_key)

    # Send a POST request to transition the issue
    transition_response = requests.post(
        transition_url,
        auth=(username, password),
        json=transition_payload
    )

    if transition_response.status_code == 204:
        print("Issue transitioned successfully.")
    else:
        print("Failed to transition the issue. Status code:", transition_response.status_code)
else:
    print("Failed to create issue. Status code:", create_response.status_code)
    print("Response:", create_response.text)


"""
Make sure to replace the following placeholders with your own values:

"https://your-jira-instance/rest/api/2/issue/": Replace your-jira-instance with the URL of your Jira instance.
username and password: Replace with your Jira credentials.
"PROJECT_KEY": Replace with the key of the Jira project where you want to create the issue.
"Issue summary": Replace with the desired summary for your issue.
"Issue description": Replace with the desired description for your issue.
"Task": Replace with the desired issue type for your issue (e.g., "Bug", "Story", "Epic", etc.).
"TRANSITION_ID": Replace with the ID of the workflow transition you want to trigger. You can find the transition ID by inspecting the workflow configuration or using the Jira REST API.
This code creates a Jira issue using the Jira API, and upon successful creation, it transitions the issue to the desired workflow state using another API request. Adjust the URLs and payload data according to your specific Jira instance and workflow configuration.

Make sure you have the requests library installed (pip install requests) before running the code.
"""