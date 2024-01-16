import oss2
from itertools import islice

import json

# 打开并加载JSON文件
with open('config.json', 'r') as f:
    config_data = json.load(f)

# 填写RAM用户的访问密钥（AccessKey ID和AccessKey Secret）。
accessKeyId = config_data['accessKeyId']
accessKeySecret = config_data['accessKeySecret']

print(f"auth accessKeyId:{accessKeyId} accessKeySecret:{accessKeySecret}")
# 使用代码嵌入的RAM用户的访问密钥配置访问凭证。
auth = oss2.Auth(accessKeyId, accessKeySecret)
endpoint = 'oss-cn-shanghai.aliyuncs.com'

# 填写Bucket名称。
bucket = oss2.Bucket(auth, endpoint, 'guhui-demo') 

bucket.put_object_from_file('sample.jpg', 'sample.jpg')

bucket.get_object_to_file('飞书20231226-150553.jpg','downlaod_jpg.jpg')

print("begin to browser Bucket")
for b in islice(oss2.ObjectIterator(bucket), 10):
    print(b.key)