# youtrack_api_client
Simple Python API Client for new YouTrack REST API

## Demo
```
from youtrack_api_client import Youtrack_api_client as YT

yt_base_url = '<your YouTrack server URL>'
token = get_token()
query = "issue id:OM5-1"

yt_client = YT(yt_base_url, token, False)
issues = yt_client.get_issues_by_query(query)
for issue in issues:
    print("'{}' with id '{}'".format(issue.get("summary", "summary"), issue.get("idReadable", "idReadable")))

issue_id = 'OM5-1'
issue = yt_client.get_issue_properties_by_id(issue_id)
for index in range(len(issue['customFields'])):
    property_name = issue['customFields'][index]['projectCustomField']['field']['name']
    prop = issue['customFields'][index]['value']
    property_value = ""
    if prop is None:
        pass
    elif type(prop) is dict:
        if 'name' in issue['customFields'][index]['value']:
            property_value = issue['customFields'][index]['value']['name']
    else:
        property_value = issue['customFields'][index]['value']
    print("Property name '{}' with value '{}'".format(property_name, property_value))
```

### Example output
```
PS C:\_git\youtrack_api_client> python.exe .\example.py
'OMS-500 test access' with id 'OM5-1'
Property name 'Type' with value 'Bug'
Property name 'Assignee' with value '[]'
Property name 'Team' with value '[]'
Property name 'Found In Version(s)' with value '1.2.2.1'
Property name 'Defect Severity' with value 'L3 minor sci-fi'
Property name 'Priority' with value 'Medium [50.0]'
...
```
