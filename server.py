import os
from flask import Flask, jsonify

from zd_lib import get_zd_url

application = Flask(__name__, static_folder="dist")
application.debug = True


@app.route("/api/zendesk/ticket/")
def get_zd_tickets():
    return jsonify(get_zd_url())


@app.route('/')
def root():
    return application.send_static_file('index.html')


@app.route('/js/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return application.send_static_file(os.path.join('js', path))


@app.route('/views/<path:path>')
def static_proxy_views(path):
    return application.send_static_file(os.path.join('views', path))


if __name__ == "__main__":
    application.run()
