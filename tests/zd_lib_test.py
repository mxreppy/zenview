from unittest.mock import MagicMock, patch
import requests
import unittest

from zd_lib import config, get_zd_url, extract_ws, installed_js_fragment, \
    expected_ws_token, get_ws_token, get_jira_ticket_list


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
        mock.text = installed_js_fragment
        with patch.object(requests, 'get', return_value=mock) as mock_requests:
            self.assertEqual(get_ws_token(), expected_ws_token)

    @patch('zd_lib.extract_ws')
    def tes_get_jira_list(self, mock1):
        mock_response = MagicMock()
        mock_response.json.return_value = "{'test': 'true'}"
        mock1.return_value = '999111'
        with patch.object(requests, 'get', return_value=mock_response) as mock_requests:
            self.assertEqual(get_jira_ticket_list('111'), "{'test': 'true'}")
            mock_requests.assert_called_with(
                config.zd_integrations_jira % ('999111', '111'))


if __name__ == "__main__":
    unittest.main()
