from jira import JIRA

jira_connection = JIRA(
    basic_auth=('workspace_email', 'api_token'),
    server="https://server_name.atlassian.net"
)

issue_dict = {
    'project': {'key': 'PJH'},
    'summary': 'Testing issue from Python Jira Handbook',
    'description': 'Detailed ticket description.',
    'issuetype': {'name': 'Bug'},
}

new_issue = jira_connection.create_issue(fields=issue_dict)
