import urllib.request # 这个模块提供了访问URL和操作HTTP请求的功能
import re

# 要爬的网站链接
url = "https://ssr.gamecenter.qq.com/hippy-ssr/v1/app/action-sheet?p_collections=&action_type=download&appid=123331&report_params=%7B%22module%22%3A834%2C%22subModule%22%3A83402%7D&_qv=9.0.50&_pf=android&_ws=400x855&_ss=400x889"

# 定义请求头信息，模仿浏览器的行为
# 有些网站会检查请求头是否来自浏览器(这个url就检查了),如果不是就会返回403Forbidden错误
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 创建了一个request对象，将前面的url和headers放进去
# 用于发送HTTP请求
request = urllib.request.Request(url, headers=headers)

try:
    response = urllib.request.urlopen(request) # 获取请求的响应
    html = response.read().decode('utf-8')
    #res = re.findall(r"<head>(.+?)</head>", html, re.DOTALL)
    res = re.findall(r'src="(.*?)"', html)
    #print(html)
    print("\nThe src is :", res[0])
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")