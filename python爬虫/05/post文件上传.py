import requests

# 文件上传

url = 'https://httpbin.org/post'

files = {
    'file': open('page.html', 'r')
}
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

response = requests.post(url, files=files, headers=headers)

if response.status_code == 200:
    print(response.text)
