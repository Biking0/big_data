#!/usr/bin/env python
# -*-coding:utf-8 -*-
#********************************************************************************************
# **
# **  �ļ����ƣ� dw_user_after_before_yyyymmdd.py
# **
# **  ���������� ����ǰ�������ǰ��һ���ʡ��λ������
# **
# **  ���������
# **
# **  �� �� ��    
# **
# **  �� �� �� dw_user_after_before_yyyymmdd
# **  �� �� �ߣ� hhy
# **
# **  �������ڣ� 2019��02��21��
# **
# **  �޸���־��
# **
# **  �޸����ڣ�
# **
# **  �޸���  ��
# **
# **  �޸����ݣ�
# **
# *******************************************************************************************
# **
# **  ������ø�ʽ��python dw_user_after_before_yyyymmdd.py 20181006
# **
# *******************************************************************************************

import os,sys
import time,datetime
from settings import *
from hqltools3 import *
#from hqltools3_nt import *

#===========================================================================================
#����ʼ ����������
#===========================================================================================

name = 'dw_user_after_before_yyyymmdd'
dates= '20191015'
#taskPosition=""

#����1
hivesql = []
hivesql.append('''select * from dw_user_after_3day_yyyymmdd limit 5''')
HiveExe(hivesql,name,dates)