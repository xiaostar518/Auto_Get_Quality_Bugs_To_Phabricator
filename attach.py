#!/usr/bin/env python
# coding:utf-8
import requests
import os
import shutil
import util

attach_url = util.attach_url
attach_path = util.attach_path


def attach_file(query_messages, token):
    # if os.path.exists(attach_path):
    #     shutil.rmtree(attach_path)
    # os.mkdir(attach_path)

    if not os.path.exists(attach_path):
        os.mkdir(attach_path)
    if query_messages is None:
        return
    print("--------download attach start--------")
    print "\n\n"
    for message in query_messages:
        # print message
        file_messages = message["files"]
        if file_messages is not None:
            for file_message in file_messages:
                print 'file_message: ', file_message
                download_attach_file(file_message, token)

    print("--------download attach end--------")
    print "\n\n"


def download_attach_file(files, token):
    print files["fileName"] + " start downloading..."
    print "\n"
    if not os.path.exists(attach_path + files["fileName"]):
        fileId = {"fileId": files["id"]}
        headers = {
            'Authorization': "Bearer " + token,
        }
        response = requests.request("GET", attach_url, headers=headers, params=fileId)
        with open(attach_path + files["fileName"], "wb") as f:
            f.write(response.content)
        f.close()
