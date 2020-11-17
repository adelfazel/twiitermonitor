from flask import Flask, Response
from flask import request
import os
import sys
from flask import jsonify

sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.abspath('../../'))
sys.path.append(os.path.abspath('../../../'))

import argparse
from app.src.auth import token
from app.src.twitter import itwitter
import json

server = Flask(__name__)
import threading


@server.route("/")
def get_tweets():
    global twitter
    json_response = json.dumps(twitter.get_all_tweets())
    response = Response(json_response, content_type='application/json; charset=utf-8')
    response.headers.add('content-length', json_response)
    response.status_code = 200
    return json_response


@server.route("/", methods=['PUT'])
def change_account():
    global twitter
    twitter.set_monitor_account(request.headers['account'])
    return jsonify(success=True)


def get_runtime_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--account", help="name of the account", default="VicGovDHHS")
    parser.add_argument("-ck", "--consumer_key", help="consumer key", default='3rJOl1ODzm9yZy63FACdg')
    parser.add_argument("-cs", "--consumer_secret", help="consumer secret",
                        default='5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8')
    parser.add_argument("-p", "--port", help="port for server to run", default=5000, type=int)
    return parser.parse_args()


def run_twitter(params):
    global twitter
    auth = token.Authenticator(params.consumer_key, params.consumer_secret)
    twitter = itwitter.Twitter(auth, params)
    twitter.run()


def run_server(params):
    server.run(host='0.0.0.0', port=params.port)


def run(params):
    threading.Thread(target=run_twitter, args=(params,)).start()
    threading.Thread(target=run_server, args=(params,)).start()


if __name__ == "__main__":
    params = get_runtime_params()
    run(params)
