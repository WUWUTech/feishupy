# -*- coding: utf-8 -*-
import os
import json

from feishupy import FeiShuClient, TOKEN_TYPE_APP_ACCESS_TOKEN_INTERNAL

if __name__ == '__main__':
    fs_client = FeiShuClient(
        app_id=os.environ.get('APP_ID') or 'INPUT_APP_ID_HERE',
        app_secret=os.environ.get('APP_SECRET') or 'INPUT_APP_SECRET_HERE',
        token_type=TOKEN_TYPE_APP_ACCESS_TOKEN_INTERNAL
    )

    # 发送群聊 WebHook 机器人消息
    # fs_client.hook_bot.send_msg('WebHook 机器人ID', 'content', 'title')

    # 获取 access_token
    # access_token = fs_client.access_token(token_type=TOKEN_TYPE_APP_ACCESS_TOKEN_INTERNAL)

    # code2session
    # result = fs_client.mina.code2session(code='633c9a0b9de7e1d9')

    # 获取通讯录授权范围
    # result = fs_client.contact.scope_get()

    # 获取角色列表
    # result = fs_client.contact.role_list()

    # print(json.dumps(result))
