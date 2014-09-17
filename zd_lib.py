import unittest
from unittest.mock import patch, MagicMock

import re

import requests

try:
    import config
except:
    print("could not import config.py, please create it")
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


class myTestCase(unittest.TestCase):
    def test_load_zd(self):
        mock = MagicMock()
        mock.json.return_value = "{'data':'test'}"
        with patch.object(requests, 'get', return_value=mock) as mock_requests:
            url = config.zd_view_url
            data = get_zd_url(url)
            assert(data)
            mock_requests.assert_called_once_with(url, auth=(config.zendesk_user, config.zendesk_pwd))

    def test_ws_extrac(self):
        self.assertEquals(extract_ws(installed_js_fragment), expected_ws_token)
        self.assertRaises(LookupError, extract_ws, 'no good content')

    def test_load_ws_token(self):
        mock = MagicMock()
        mock.json.return_value = installed_js_fragment
        with patch.object(requests, 'get', return_value=mock) as mock_requests:
            self.assertEqual(get_ws_token(), expected_ws_token)

    @patch('zd_lib.extract_ws')
    def test_get_jira_list(self, mock1):
        mock_response = MagicMock()
        mock_response.json.return_value = "{'test': 'true'}"
        mock1.return_value = '999111'
        with patch.object(requests, 'get', return_value=mock_response) as mock_requests:
            self.assertEqual(get_jira_ticket_list('111'),"{'test': 'true'}")
            mock_requests.assert_called_with(
                config.zd_integrations_jira % ('999111', '111'))


installed_js_fragment = '''\
ZendeskApps["JIRA OnDemand"].install({"id":12345,"app_id":12345,"settings":{"title":"JIRA","jira_url":"https://yourdomain.atlassian.net","webservice_token":"92348923482194fefefefefef123103901","jira_username":"jusername","jira_password":"jpassword","jira_field_settings":null,"has_jira_shared_secret":"9"},"enabled":true,"updated":"20140822044814"});
  ZendeskApps.sortAppsForSite('ticket_sidebar', [1234, 123456]);''
'''
expected_ws_token = '92348923482194fefefefefef123103901'

if __name__ == "__main__":
    unittest.main()
