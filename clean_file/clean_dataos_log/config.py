#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：config.py
# 功能描述：dataos日志路径配置
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20201009
# 修改日志：
# 修改日期：
# ***************************************************************************
# 程序调用格式：python config.py
# ***************************************************************************

import os
import sys
import time

# delete 2 day ago file
day_180 = 180

log_path = {'172.19.168.96': ['home/dacp/apps', 'home/dacp/apps']}