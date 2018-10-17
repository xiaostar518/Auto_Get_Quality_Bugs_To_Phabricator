#!/usr/bin/env python
# coding:utf-8
import requests
import json
import util

login_url = util.login_url


def login_and_get_token():
    print("--------login_and_get_token start--------")
    print "\n\n"
    account_message_location = "./account_message.json"

    with open(account_message_location, 'r') as load_f:
        account_message = json.load(load_f, encoding='UTF-8')

    response = requests.request("GET", login_url, params=account_message)
    token_message_json = response.text
    print "token_message_json: ", token_message_json
    print "\n"
    token_message = json.loads(token_message_json, encoding='UTF-8')
    token = token_message["token"]
    print "token: ", token
    print "\n"

    print("--------login_and_get_token end--------")
    print "\n\n"
    return token
