import unittest
from unittest.mock import patch, MagicMock

import re

import requests

try:
    import config
except:
    print("could not import config.py, please create it (see ./config_example.py for an example)")
    exit(1)


def get_zd_url(url, content_type='json'):
    response = requests.get(url, auth=(config.zendesk_user, config.zendesk_pwd))
    data = response.json()
    return data


def extract_ws(content):
    m = re.search('''"https://\w+.atlassian.net","webservice_token":"(\w+)","jira_username"''', content)
    if m:
        auth_token = m.groups()[0]
        return auth_token
    else:
        raise LookupError("Could not find WS token")


def get_ws_token():
    url = config.zd_installed_js
    content = get_zd_url(url, content_type='text')
    return extract_ws(content)


def get_jira_ticket_list(zd_ticket_id):
    auth_token = get_ws_token()
    response = requests.get(config.zd_integrations_jira % (auth_token, zd_ticket_id))
    return response.json()


installed_js_fragment = '''\
ZendeskApps["JIRA OnDemand"].install({"id":12345,"app_id":12345,"settings":{"title":"JIRA","jira_url":"https://yourdomain.atlassian.net","webservice_token":"92348923482194fefefefefef123103901","jira_username":"jusername","jira_password":"jpassword","jira_field_settings":null,"has_jira_shared_secret":"9"},"enabled":true,"updated":"20140822044814"});
  ZendeskApps.sortAppsForSite('ticket_sidebar', [1234, 123456]);''
'''
expected_ws_token = '92348923482194fefefefefef123103901'

if __name__ == "__main__":
    unittest.main()
