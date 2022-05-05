import logging
import json

import oss2
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdksts.request.v20150401.AssumeRoleRequest import AssumeRoleRequest

accessKeyId = u'' #替换为您的AccessKeyId
accessSecret = u'' #替换为您的AccessSecret

def handler(event, context):

  try:
    acsClient = AcsClient(accessKeyId, accessSecret, 'cn-beijing')
    request = AssumeRoleRequest()
    request.set_accept_format('json')
    request.set_RoleArn("acs:ram::xxxx:xxxx/xxxx") #替换为角色的ARN值
    request.set_RoleSessionName("migration_role")
    response = acsClient.do_action_with_exception(request)
    content = str(response, encoding='utf-8')
  except Exception as e:
    content = "occur exceptions"

  api_rep = {
    "isBase64Encoded":"false",
    "statusCode":"200",
    "body":content
  }
  return json.dumps(api_rep)