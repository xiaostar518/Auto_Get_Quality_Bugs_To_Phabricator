#!/usr/bin/env python
# coding:utf-8


title = [u'files',
         u'operType',
         u'grade',
         u'headway',
         u'stateName',
         u'topic',
         u'typeName',
         u'creatorEmail',
         u'd7',
         u'chargeDeptDis',
         u'estimatedDate',
         u'id',
         u'd1',
         u'd5',
         u'd4',
         u'descr',
         u'd3',
         u'provider',
         u'type',
         u'disTime',
         u'creatorName',
         u'partInfo',
         u'creatorSect',
         u'createTime',
         u'creatorDept',
         u'stage',
         u'problemFinder',
         u'creatorTel',
         u'systemName',
         u'creatorId']

columnName = [u'Title',
              u'Assigned',
              u'Status',
              u'Priority',
              u'Description',
              u'Visible',
              u'Subscribers',
              u'Module',
              u'FoundMethod',
              u'HWVersion',
              u'SWVersion',
              u'FixVersion',
              u'VerifyVersion',
              u'Workload',
              u'DueDate',
              u'ResolveDate',
              u'RootCause',
              u'File_location']

priority = {
    "A": "High",
    "B": "Normal",
    "C": "Low",
    "D": "Wishlist"
}

excel_name_quality_issues_path = "./Excel_file/quality_issues.xlsx"
excel_name_task_content_path = "./Excel_file/task_content.xlsx"
task_content_file_path = "./AutoTool/index.py"

attach_path = "./Attach_files/"
pre = './Attach_files/'

IS_CREATED_TRUE = '1'
IS_CREATED_FALSE = '0'

# url
login_url = "http://info.pov.byd.com/rdmsbase/login"
query_issue_url = "http://info.pov.byd.com/api/bydsign-web/quality/findQualityByProviderDivision"
attach_url = "http://info.pov.byd.com/api/bydsign-web/quality/download"


assign_username = 'xiaoxiao2(xiaoxiao2)'
project_visible = 'VP820'

