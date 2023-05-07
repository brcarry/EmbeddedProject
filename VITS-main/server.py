import socket
import torch
import utils
from models import SynthesizerTrn
from text.symbols import symbols
import soundfile as sf



# text = "我是VITS本地推理版"
text = "旅行者，我在"
length_scale = 1
filename = 'results/result123'
audio_path = f'{filename}.mp3'
# 创建模型，加载参数
hps = utils.get_hparams_from_file("./configs/biaobei_base.json")
model = SynthesizerTrn(
    len(symbols),
    hps.data.filter_length // 2 + 1,
    hps.train.segment_size // hps.data.hop_length,
    **hps.model).cuda()
model.eval()
utils.load_checkpoint('model/Paimon.pth', model)

# stn_tst = utils.get_text(text, hps)
# with torch.no_grad():
#     x_tst = stn_tst.cuda().unsqueeze(0)
#     x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
#     audio = model.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=length_scale)[0][
#         0, 0].data.cpu().float().numpy()
# sf.write(audio_path, audio, samplerate=hps.data.sampling_rate)



listen_addr = '172.23.116.224'

# listen_addr = '172.23.112.1'
listen_port = 8989

sk = socket.socket()  # 实例化一个对象sk
sk.bind((listen_addr, listen_port))  # 把地址绑定到套接字
sk.listen()  # 监听链接
print("开始监听")
while True:
    # 等待windows用户发送请求
    conn, addr = sk.accept()  # 接收客户端链接
    print(addr)  # 打印出客户端的地址+端口


    text = conn.recv(1024).decode('utf-8')
    text.replace('\n', ' ')
    # text = "旅行者，我在"
    print("从windwos收到，需要转换的文本为：",text)

    stn_tst = utils.get_text(text, hps)
    with torch.no_grad():
        x_tst = stn_tst.cuda().unsqueeze(0)
        x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
        audio = model.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=length_scale)[0][
            0, 0].data.cpu().float().numpy()
    sf.write(audio_path, audio, samplerate=hps.data.sampling_rate)


    conn.send('已完成语音生成'.encode('utf-8'))  # 向客户端发送信息
    print("已完成语音生成")
    ret = conn.recv(1024)  # 接收客户端信息(1024字节)
    print(ret.decode('utf-8'))  # 打印客户端信息(bytes类型需要decode)
    conn.close()  # 关闭客户端套接字
sk.close()  # 关闭服务器套接字
