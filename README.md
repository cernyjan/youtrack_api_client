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
```

### Example output
```
PS C:\_git\youtrack_api_client> python.exe .\example.py
'OMS-500 test access' with id 'OM5-1'
```
