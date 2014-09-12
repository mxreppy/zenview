import unittest
from unittest.mock import patch, MagicMock

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

class myTestCase(unittest.TestCase):
    def test_load_zd(self):
        mock = MagicMock()
        mock.json.return_value = "{'data':'test'}"
        with patch.object(requests, 'get', return_value=mock) as mock_requests:
            url = 'https://energyplus.zendesk.com/api/v2/views/30701628/tickets.json'
            data = get_zd_url(url)
            assert(data)
            mock_requests.assert_called_once_with(url, auth=(config.zendesk_user, config.zendesk_pwd))


if __name__ == "__main__":
    unittest.main()
