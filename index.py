#!/usr/bin/env python
# coding:utf-8

import login
import queryIssue
import attach
import excel
import json
import os
import autoCreateTask
import util

excel_name_quality_issues_path = util.excel_name_quality_issues_path
excel_name_task_content_path = util.excel_name_task_content_path
task_content_file_path = util.task_content_file_path


def comparativeData(old_excel_data=None, query_messages=None):
    print 'old_excel_data', old_excel_data
    print 'query_messages', query_messages

    if old_excel_data is None:
        for current_data in query_messages:
            current_data['iscreated'] = util.IS_CREATED_FALSE
        return query_messages
    elif query_messages is None:
        return None
    else:
        for current_data in query_messages:
            # print 'current', current_data
            isCreated = util.IS_CREATED_FALSE
            for old_data in old_excel_data:
                # print 'old', old_data
                if current_data['id'] == old_data['id']:
                    isCreated = util.IS_CREATED_TRUE
                    break
            if isCreated == util.IS_CREATED_FALSE:
                current_data['iscreated'] = util.IS_CREATED_FALSE
            else:
                current_data['iscreated'] = util.IS_CREATED_TRUE
            # print 'current_data', current_data
        return query_messages


def update_excel_data(all_excel_data):
    for excelData in all_excel_data:
        if excelData['iscreated'] == util.IS_CREATED_FALSE:
            excelData['iscreated'] = util.IS_CREATED_TRUE
    return all_excel_data


if __name__ == "__main__":
    token = login.login_and_get_token()

    query_messages = queryIssue.query_issue(token)
    print 'query_messages', query_messages

    old_excel_data = excel.load_excel(excel_name_quality_issues_path)

    all_excel_data = comparativeData(old_excel_data, query_messages)

    if all_excel_data is not None:
        excel.export_excel(excel_name_quality_issues_path, all_excel_data)

        attach.attach_file(all_excel_data, token)

        excel_data = excel.load_excel(excel_name_quality_issues_path)

        i = 1
        for data in excel_data:
            print i
            i = i + 1
            print data
        print excel_data

        excel.export_excel_phabricator(excel_name_task_content_path, excel_data)

        excel.export_excel(excel_name_quality_issues_path, update_excel_data(all_excel_data))

        autoCreateTask.create_Task(task_content_file_path)

        # {
        #     u'files': [
        #         {
        #             u'id': u'8a89a11f64ff3c8f01651d66a4a01ce1',
        #             u'fileName': u'IMG_4390.JPG'
        #         }
        #     ],
        #     u'operType': 0,
        #     u'grade': u'C',
        #     u'headway': u'<p>&nbsp;\u5168\u5c4f<span style="font-family: tahoma, arial, helvetica, sans-serif; font-size: 13.3333px;">\u8fdb\u5ea6\u6761\u624d\u4f1a\u6d88\u5931</span></p>',
        #     u'stateName': u'\u539f\u56e0\u4e0d\u660e\uff0c\u5206\u6790\u4e2d',
        #     u'vin': u'9408', u'carType': u'STB',
        #     u'topic': u'\u539f\u8f66\u64ad\u653e\u5668\u89c6\u9891\u64ad\u653e\u65f6\uff0c\u8fdb\u5ea6\u6761\u4e0d\u6d88\u9690\uff0c\u6321\u5b57\u5e55',
        #     u'typeName': u'\u975e\u8bbe\u8ba1\u7c7b',
        #     u'creatorEmail': u'zhou.zhenpeng@byd.com',
        #     u'd6': u'<p><span style="font-size: 13.3333px;">&nbsp;</span><span style="font-size: 13.3333px;">&nbsp;\u6b63\u5e38\u73b0\u8c61\uff0c\u4e0d\u7528\u6574\u6539\u3002</span></p>',
        #     u'd7': u'<p>&nbsp;\u65e0</p>',
        #     u'chargeDeptDis': u'\u8f66\u7528\u7535\u5668\u90e8',
        #     u'estimatedDate': u'2018-10-01 00:00:00',
        #     u'id': u'172',
        #     u'd1': None,
        #     u'd5': None,
        #     u'd4': u'<p>&nbsp;<span style="font-size: 13.3333px;">&nbsp;\u6b63\u5e38\u73b0\u8c61\uff0c\u5168\u5c4f</span><span style="font-size: 13.3333px; font-family: tahoma, arial, helvetica, sans-serif;">\u8fdb\u5ea6\u6761\u624d\u4f1a\u6d88\u5931\u3002</span></p>',
        #     u'descr': u'<p>&nbsp;\u539f\u8f66\u5a92\u4f53\u4e2d\u5fc3\u7684\u64ad\u653e\u5668\u64ad\u653eu\u76d8\u89c6\u9891\u65f6\uff0c\u8fdb\u5ea6\u6761\u4e0d\u6d88\u9690\uff0c\u6321\u5b57\u5e55</p>',
        #     u'd3': None,
        #     u'state': u'black',
        #     u'provider': u'\u7b2c\u4e94\u4e8b\u4e1a\u90e8',
        #     u'type': 0,
        #     u'providerEng': None,
        #     u'disTime': u'2018-07-31 00:00:00',
        #     u'creatorName': u'\u5468\u632f\u9e4f',
        #     u'partInfo': u'ST-7924100T',
        #     u'creatorSect': u'\u6574\u8f66\u4e3b\u89c2\u8bc4\u4ef7\u79d1',
        #     u'createTime': u'2018-08-09 14:37:48',
        #     u'creatorDept': u'\u6574\u8f66\u8bc4\u4ef7\u6d4b\u8bd5\u90e8',
        #     u'stage': u'S3',
        #     u'src': u'\u6574\u8f66\u8bd5\u9a8c',
        #     u'problemFinder': u'\u5468\u632f\u9e4f',
        #     u'failureMileage': u'/',
        #     u'creatorTel': u'13632991231',
        #     u'systemName': u'\u97f3\u54cd\u7cfb\u7edf',
        #     u'creatorId': u'2332436',
        #     u'operTypeName': u'\u4e58\u7528\u8f66'
        # }
