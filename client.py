import socket
import re

def convert_number_to_chinese(num):
    num = int(num)
    units = ['', '十', '百', '千']
    nums = '零一二三四五六七八九'
    result = []

    if num < 10:
        return nums[num]

    num_str = str(num)
    num_len = len(num_str)

    for i, n in enumerate(num_str):
        if n == '0':
            if result and result[-1] != '零':
                result.append('零')
        else:
            result.append(nums[int(n)])
            result.append(units[num_len - i - 1])

    return ''.join(result).rstrip('零')


import re
def replace_numbers_with_chinese(text):
    def replace(match):
        number = match.group(0)
        return convert_number_to_chinese(number)

    return re.sub(r'\d+', replace, text)

server_addr = '172.23.116.224'
server_port = 8989
listen_addr = '10.181.243.251'
listen_port = 6666

sk_s = socket.socket()  # 实例化一个对象sk
sk_s.bind((listen_addr, listen_port))  # 把地址绑定到套接字
sk_s.listen()  # 监听链接
print("windows开始监听")

while True:
    conn_pi, addr_pi = sk_s.accept()  # 接收客户端链接
    print(addr_pi)  # 打印出客户端的地址+端口

    # 先接受等待转换成语音的文本
    text = conn_pi.recv(1024).decode('utf-8')
    print('从pi接收：',text)

    # 2023/05/06 去除换行符
    text = text.replace('\n', '')
    # print("去除换行符后结果:")
    # print(text)
    pattern = re.compile(r"[^\da-zA-Z0-9\u4e00-\u9fa5]+")
    text = pattern.sub("，", text)
    text = replace_numbers_with_chinese(text)
    print(text)


    # 向wsl请求生成语音
    # 作为client向wsl发起请求
    sk_c = socket.socket()  # 创建客户端套接字
    sk_c.connect((server_addr, server_port))  # 连接服务器(ip地址+端口)

    sk_c.send(text.encode('utf-8'))

    ret = sk_c.recv(1024)  # 等待wsl完成任务的消息
    print("从wsl接收：",ret.decode('utf-8'))
    sk_c.send('windows收到消息!'.encode('utf-8'))
    sk_c.close()  # 关闭客户端套接字

    filename = './results/result123.mp3'
    with open(filename,"rb") as f:
        rdata = f.read()

    len_data = len(rdata)
    print("向pi发送的文件大小为：",len_data)
    conn_pi.send(str(len_data).encode('utf-8'))
    ret = conn_pi.recv(1024).decode('utf-8')
    print(ret)

    conn_pi.sendall(rdata)

    ret = conn_pi.recv(1024)
    print(ret.decode('utf-8'))
    conn_pi.close()  # 关闭客户端套接字

sk_s.close()  # 关闭服务器套接字