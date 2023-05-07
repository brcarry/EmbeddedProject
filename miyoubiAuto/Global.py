# -*- coding: utf-8 -*-
"""
在下面设置你的米游社Cookie
"""
# mysCookie = '_MHYUUID=debe88f0-46f3-417e-850b-33c8ba9bd785; aliyungf_tc=4113059898757768bce837d3d41f3d3cb53249943018472a4fc96dbe28a331f5; DEVICEFP_SEED_ID=e2ece28c969a8b4a; DEVICEFP_SEED_TIME=1681060031248; DEVICEFP=38d7ede97340d; login_uid=234118413; login_ticket=DRHvpGxy7sj798pcI9OrrSDGB7f1UuBVECv8DKb0'
# mysCookie = '_MHYUUID=86047378-7f82-42da-880c-3e7f3888426c; aliyungf_tc=d2574d523f5ce597bfb165d0beeff8536c153e15f1527cc98344669991b8b2d8; DEVICEFP_SEED_ID=55d5d0dad239cfd3; DEVICEFP_SEED_TIME=1681086025315; DEVICEFP=38d7ede9b2c96; login_uid=234118413; login_ticket=5yJyFxbtD5uORwetBNgS64lxF7ss069JVngzRWZK'

mysCookie = '_MHYUUID=86047378-7f82-42da-880c-3e7f3888426c; aliyungf_tc=d2574d523f5ce597bfb165d0beeff8536c153e15f1527cc98344669991b8b2d8; DEVICEFP_SEED_ID=55d5d0dad239cfd3; DEVICEFP_SEED_TIME=1681086025315; DEVICEFP=38d7ede9b2c96; login_uid=234118413; login_ticket=5yJyFxbtD5uORwetBNgS64lxF7ss069JVngzRWZK'

"""
以下内容不要改！！！
"""
mysVersion = "2.34.1"
salt = "z8DRIUjNDT7IT5IZXvrUAxyupA1peND9"  # 米游社2.34.1版本安卓客户端salt值
salt2 = "t0qEgfub6cvueAPgR5m9aQWWVciEer7v" #这个给签到用
client_type = "2"  # 1:ios 2:android

"""
api
"""
cookieUrl = "https://webapi.account.mihoyo.com/Api/cookie_accountinfo_by_loginticket?login_ticket={}"
cookieUrl2 = "https://api-takumi.mihoyo.com/auth/api/getMultiTokenByLoginTicket?login_ticket={}&token_types=3&uid={}"
signUrl = "https://bbs-api.mihoyo.com/apihub/app/api/signIn"  # post
listUrl = "https://bbs-api.mihoyo.com/post/api/getForumPostList?forum_id={}&is_good=false&is_hot=false&page_size=20&sort_type=1"
detailUrl = "https://bbs-api.mihoyo.com/post/api/getPostFull?post_id={}"
shareUrl = "https://bbs-api.mihoyo.com/apihub/api/getShareConf?entity_id={}&entity_type=1"
voteUrl = "https://bbs-api.mihoyo.com/apihub/sapi/upvotePost"  # post json 

"""
分区编号
"""
gameList = [
    {
        "id": "1",
        "forumId": "1",
        "name": "崩坏3",
        "url": "https://bbs.mihoyo.com/bh3/"
    },
    {
        "id": "2",
        "forumId": "26",
        "name": "原神",
        "url": "https://bbs.mihoyo.com/ys/"
    },
    {
        "id": "3",
        "forumId": "30",
        "name": "崩坏2",
        "url": "https://bbs.mihoyo.com/bh2/"
    },
    {
        "id": "4",
        "forumId": "37",
        "name": "未定事件簿",
        "url": "https://bbs.mihoyo.com/wd/"
    },
    {
        "id": "5",
        "forumId": "34",
        "name": "大别野",
        "url": "https://bbs.mihoyo.com/dby/"
    },
    {
    "id": "6",
    "forumId": "52",
    "name": "崩坏：星穹铁道",
    "url": "https://bbs.mihoyo.com/sr/"
    },
    {
    "id": "8",
    "forumId": "57",
    "name": "绝区零",
    "url": "https://bbs.mihoyo.com/zzz/"
    }
]
