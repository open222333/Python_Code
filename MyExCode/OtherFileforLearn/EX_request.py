import requests

# url = 'https://ccl.jkimg02.xyz/imgs/actor/a3/54aaa99092bb0.jpg'
# print(requests.get(url).status_code, type(requests.get(url).status_code))

# 重定向
# https://www.cnblogs.com/xswt/p/11475164.html


# def get_status_code(img_path) -> int:
#     return requests.get(img_path).status_code


# url = ''
# print(get_status_code(url))


url = 'http://dekm6v70x775h.cloudfront.net/JKSR-235/240/JKSR-235.m3u8'
r = requests.get(url, headers={"Content-Type": "application/json"})
reditList = r.history
print(f'獲取追蹤歷史：{r}')
# print(f'headers：{reditList[0].headers}')
# print(f'url：{reditList[len(reditList)-1].headers["location"]}')