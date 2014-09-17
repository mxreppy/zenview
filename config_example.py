#Zendesk settings
zendesk_user = '************'
zendesk_pwd = '**********'
zd_view_url = "https://domain.zendesk.com/api/v2/views/[ViewNumber]/tickets.json"
zd_installed_js = "https://domain.zendesk.com/api/v2/apps/installed.js"
zd_integrations_jira  = '''https://jiraplugin.zendesk.com/integrations/jira/account/domain/links/for_ticket?auth_token=%s&ticket_id=%s'''
zd_ticket_url = "https://domain.zendesk.com/api/v2/tickets/%s.json"

jira_user = '***********'
jira_pwd = '**********'
jira_url = '''https://domain.atlassian.net/rest/api/2/issue/%s'''
