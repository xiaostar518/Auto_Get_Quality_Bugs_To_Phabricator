#!/usr/bin/env python
# coding:utf-8
import requests
import time
import json
import util

# 格式化成2016-03-20形式
today_date = time.strftime("%Y-%m-%d", time.localtime())

query_issue_url = util.query_issue_url
query_time = {}


def query_issue(token, end_time=today_date):
    print "--------parse issue messages start--------"
    print "\n\n"
    authorization_value = "Bearer " + token
    # print authorization_value

    headers = {
        'Authorization': authorization_value,
    }

    query_time["startTime"] = "2018-08-01"
    query_time["endTime"] = end_time

    response = requests.request("GET", query_issue_url, headers=headers, params=query_time)
    query_message_json = response.text
    query_messages = json.loads(query_message_json, encoding='UTF-8')

    if query_messages["data"] is not None:
        for data in query_messages["data"]:
            print data
            print "\n"

    print "--------parse issue messages end--------"
    print "\n\n"
    return query_messages["data"]
