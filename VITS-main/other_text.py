filename = 'paimon_response.mp3'
with open(filename,"rb") as f:
    rdata = f.read()

len_data = len(rdata)
print("向pi发送的文件大小为：",len_data)