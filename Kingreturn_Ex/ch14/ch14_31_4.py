# 讀取二進位檔案的應用
src = 'ch14/bdata'

with open(src, 'rb') as file_src:
    print("目前位移：", file_src.tell())
    file_src.seek(10)
    print("目前位移：", file_src.tell())
    data = file_src.read()
    print("目前內容：", data[0])
    file_src.seek(255)
    print("目前位移：", file_src.tell())
    data = file_src.read()
    print("目前內容：", data[0])