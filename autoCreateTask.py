#!/usr/bin/env python
# coding:utf-8

import os
import AutoTool


def create_Task(task_content_file):
    # 执行结果 0表示 success ， 1表示 fail
    command = 'python ' + task_content_file
    result = os.system(command)
    print '\n\n'
    if result == 0:
        print 'Tasks are created success.'
    else:
        print 'Tasks are created fail.'
