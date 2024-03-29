import requests
import json
import datetime;

class Youtrack_api_client:
    def __init__(self, base_url, token, verify=True):
        self.base_url = self.__ensure_url(base_url)
        self.cert_verify = verify
        self.headers = {
            'Accept': 'application/json',
            'Authorization': "Bearer {}".format(token),
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json',
        }

    def __ensure_url(self, url):
        if url[-1] == '/':
            return url[:-1]
        else:
            return url

    def __log(self, value):
        now = datetime.datetime.now()
        print("{}\t{}".format(now, value))

    def get_issues_by_query(self, query):
        params = (
            ('fields', 'idReadable,summary,description'),
            ('query', query),
        )
        response = requests.get("{}/api/issues".format(self.base_url), headers=self.headers, params=params, verify=self.cert_verify)
        if response.status_code == 200:
            return json.loads(response.text)
        self.__log("Cannot get issues, Response code: '{}'".format(response.status_code))
        return {}

    def get_issue_properties_by_id(self, issue_id):
        params = {
            'fields': '$type,id,summary,project(shortName),customFields($type,id,projectCustomField($type,id,field($type,id,name)),value($type,avatarUrl,buildLink,color(id),fullName,id,isResolved,localizedName,login,minutes,name,presentation,text))'
        }
        response = requests.get("{}/api/issues/{}".format(self.base_url, issue_id), headers=self.headers, params=params, verify=self.cert_verify)
        if response.status_code == 200:
            return json.loads(response.text)
        self.__log("Cannot get issues, Response code: '{}'".format(response.status_code))
        return {}
