import functools
import json
import unittest

import re

import requests
import requests_cache

#Cache requests, need to lower this in prod
requests_cache.install_cache(expire_after=3600)

try:
    import config
except:
    print("could not import config.py, please create it (see ./config_example.py for an example)")
    exit(1)


def get_zd_url(url, content_type='json'):
    response = requests.get(url, auth=(config.zendesk_user, config.zendesk_pwd))
    if content_type == 'json':
        return response.json()
    else:
        return response.text


functools.lru_cache()
def get_zd_username(user_id):
    user = get_zd_url(config.zd_user_url.format(user_id)).get('user', {})
    return user.get('name', 'Unknown')


def get_zd_ticket_list():
    tickets = get_zd_url(config.zd_view_url)
    for ticket in tickets['tickets']:
        ticket['assignee'] = get_zd_username(ticket['assignee_id'])
        ticket['requester'] = get_zd_username(ticket['requester_id'])
    return tickets


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


def get_ticket(zd_ticket_url):
    base = get_zd_url(zd_ticket_url)['ticket']
    jira_tickets = get_jira_ticket_list(base['id'])
    base['jira'] = [get_jira_ticket(x["issue_id"]) for x in jira_tickets['links']]
    return base


def get_zd_ticket_by_id(ticket_id):
    return get_ticket('https://energyplus.zendesk.com/api/v2/tickets/%s.json' % ticket_id)


def get_jira_ticket(jira_id):
    url = config.jira_url % jira_id
    response = requests.get(url, auth=(config.jira_user, config.jira_pwd))
    return response.json()


installed_js_fragment = '''\
ZendeskApps["JIRA OnDemand"].install({"id":12345,"app_id":12345,"settings":{"title":"JIRA","jira_url":"https://yourdomain.atlassian.net","webservice_token":"92348923482194fefefefefef123103901","jira_username":"jusername","jira_password":"jpassword","jira_field_settings":null,"has_jira_shared_secret":"9"},"enabled":true,"updated":"20140822044814"});
  ZendeskApps.sortAppsForSite('ticket_sidebar', [1234, 123456]);''
'''
expected_ws_token = '92348923482194fefefefefef123103901'

if __name__ == "__main__":
    #unittest.main()
    zd_ticket = '7368'
    print(json.dumps(get_zd_ticket_by_id(zd_ticket)))
