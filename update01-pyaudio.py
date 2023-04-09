import pyaudio
import wave
import time
import struct

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
WAVE_OUTPUT_FILENAME = "output.wav"

THRESHOLD = 300

# 创建 pyaudio 对象
p = pyaudio.PyAudio()

# 打开一个音频流
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("等待用户开始说话...")

# 等待用户开始说话
while True:
    data = stream.read(CHUNK)

    max_value = 0
    data_int = struct.unpack(f'{CHUNK}h', data)
    max_value = max(data_int)
    # print(max_value)

    # if abs(max(data)) > THRESHOLD:
    #     break
    if max_value > THRESHOLD:
        break

print("开始录音...")

# 开始录音
frames = [data]
silent_counter = 0
while True:
    data = stream.read(CHUNK)
    frames.append(data)

    data_int = struct.unpack(f'{CHUNK}h', data)
    max_value = max(data_int)

    # silent_counter = silent_counter + 1 if abs(max(data)) < THRESHOLD else 0
    silent_counter = silent_counter + 1 if max_value < THRESHOLD else 0
    if silent_counter > RATE // CHUNK * 3:
        break

print("录音结束！")

# 将录制的音频保存为 wav 文件
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# 关闭音频流和 pyaudio 对象
stream.stop_stream()
stream.close()
p.terminate()
