# encoding:utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
str_dir = '/opt/fanruan/tomcat-linux/webapps/webroot/WEB-INF/reportlets'
# print(str_dir)
# 获取指定路径下的所有文件，文件夹
file_handle=open('/opt/fanruan/tomcat-linux/webapps/webroot/WEB-INF/check_file.txt',mode='a+')
for parent, dirname, filenames in os.walk(str_dir, followlinks=True):
#    print(parent)
#    print(filenames)

    for filename in filenames:
        file_path = os.path.join(parent, filename)
#        file_path = file_path.encode('raw_unicode_escape')
#         print(filename+","+file_path)
        file_handle.write(filename+","+file_path+'\r\n')
file_handle.close()