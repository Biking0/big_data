#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：config.py
# 功能描述：分区配置文件
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20210417
# 修改日志：
# 修改日期：
# ***************************************************************************
# 程序调用格式：python config.py
# ***************************************************************************

# 连接苏研集群
excute_sy_sh = "hive -e ' use csap;"

# 表结构存放路径
new_path = '/home/ocdp/hyn/hive_vt_check/table_info/'

# 生产环境
# excute_desc_sh = "beeline -u 'jdbc:hive2://192.168.190.88:10000/csap' -n hive -p %Usbr7mx -e "
excute_ocdp_sh = "beeline -u 'jdbc:hive2://172.19.40.241:10000/csap' -n ocdp -p 1q2w1q@W -e \' "
result_ocdp_sh = "beeline -u 'jdbc:hive2://172.19.40.241:10000/csap' -n ocdp -p 1q2w1q@W  --showHeader=false --outputformat=dsv --delimiterForDSV=$'\t' -e  "

# 测试环境
# excute_ocdp_test_sh = "beeline -u 'jdbc:hive2://172.22.248.19:10000/default' -n csap -p @WSX2wsx -e "

# sy程序执行路径
sy_path = "/home/hive/hyn/data_check/"

vt_schama = {'dwd': 'csapdwd',
             'dws': 'csapdws',
             'dwv': 'csapdwv',
             'dw': 'csapdw',
             'dm': 'csapdm',
             'rp': 'csaprp',
             'si': 'csapsi',
             'dim': 'csapdim',
             'etl': 'csapetl'}

# 测试vt
# test_database = {'csapdwd': ['csapdwd', 'qaQA#3e4r1'],
#                  'csapdws': ['csapdws', 'qaQA#3e4r1'],
#                  'csapdwv': ['csapdwv', 'qaQA#3e4r3'],
#                  'csapdw': ['csapdw', 'qaQA#3e4r4'],
#                  'csapdm': ['csapdm', 'qaQA#3e4r5'],
#                  'csaprp': ['csaprp', 'qaQA#3e4r6'],
#                  'csapsi': ['csapsi', 'qaQA#3e4r7'],
#                  'csapdim': ['csapdim', 'qaQA#3e4r8'],
#                  'csapetl': ['csapetl', 'qaQA#3e4r10'],
#                  # 'csapsi':'qaQA#3e4r7',
#
#                  }

# 生产
test_database = {'csapdwd': ['csap', '1qaz!QAZ'],
                 'csapdws': ['csap', '1qaz!QAZ'],
                 'csapdwv': ['csap', '1qaz!QAZ'],
                 'csapdw': ['csap', 'DwCap!QAZ'],
                 'csapdm': ['csap', 'DwCap!QAZ'],
                 'csaprp': ['csap', '01#J1B(n'],
                 'csapsi': ['csap', 'SaCap!QAZ'],
                 'csapdim': ['csap', 'DmCap12345'],
                 'CSAPETL': ['csap', 'I8hjH$Sw'],
                 }

check_table_name = 'tb_vt_check_result'
# check_table_name = 'tb_vt_data_check'

# 测试
# vt_ip = '172.19.74.63'

# 生产
vt_ip = '192.168.190.121'

mysql_exec = "mysql -h 172.19.168.22 -P 3308 -u zhao -pzhao zhao -e \'"
