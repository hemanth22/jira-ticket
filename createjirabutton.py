import requests
import json
import os


password = os.environ.get('JIRA_ACCESS')

def create_action_button(issue_key, action_name, action_url):
    """Creates a Jira action button.

    Args:
        issue_key: The key of the Jira issue.
        action_name: The name of the action button.
        action_url: The URL of the action button.

    Returns:
        The ID of the created action button.
    """

    url = "https://bitroidbitra.atlassian.net/jira/rest/api/3/issue/{}/actionButtons".format(issue_key)
    headers = {
        "Authorization": "Bearer password",
        "Content-Type": "application/json"
    }

    body = {
        "name": action_name,
        "url": action_url
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))

    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception("Error creating action button: {}".format(response.status_code))

if __name__ == "__main__":
    issue_key = "DEV-1"
    action_name = "Trigger Deployment"
    action_url = "https://github.com/hemanth22"

    action_button_id = create_action_button(issue_key, action_name, action_url)

    print("Action button created with ID: {}".format(action_button_id))