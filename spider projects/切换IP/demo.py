import urllib.request
# import ssl
# from socket import AF_INET
#
# #构建代理IP的格式
# url = 'http://ip.chinaz.com/getip.aspx'
# ipdata ='59.56.224.218'
# port = '26890'
# new_data = {
#     "http":ipdata+":"+port,
# }
#
# proxy = urllib.request.ProxyHandler(new_data)
# opener = urllib.request.build_opener(proxy)
#
# urllib.request.install_opener(opener)
# res = urllib.request.urlopen(url)
#
# print(res.read().decode('utf-8'))

#切回原来的IP
# proxy_support = urllib.request.ProxyHandler({})
# opener = urllib.request.build_opener(proxy_support)
# res = urllib.request.urlopen(url)
#
# print(res.read().decode('utf-8'))




# import requests
# print(requests.get(url,proxies=new_data).text)
# print(requests.get(url,proxies={"http":""}).text)


"""
原始ip是A
切换B失效了  ==》我们先切换为原始IP,在访问代理IP提供的API获取新的ip
"""