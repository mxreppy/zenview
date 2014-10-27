import os

from flask import Flask, jsonify

from zd_lib import get_zd_ticket_by_id, get_zd_ticket_list

application = Flask(__name__, static_folder="dist")
application.debug = True


@application.route("/api/zendesk/ticket/")
def get_zd_tickets():
    return jsonify(get_zd_ticket_list())


@application.route("/api/zendesk/ticket/<ticket_id>")
def get_zd_ticket(ticket_id):
    return jsonify(get_zd_ticket_by_id(ticket_id))


@application.route('/')
def root():
    return application.send_static_file('index.html')


@application.route('/js/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return application.send_static_file(os.path.join('js', path))


@application.route('/views/<path:path>')
def static_proxy_views(path):
    return application.send_static_file(os.path.join('views', path))


if __name__ == "__main__":
    application.run()
