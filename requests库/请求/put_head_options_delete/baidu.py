import requests

resp_put = requests.put('http://www.baidu.com/S', data={"wd":"123"})
resp_del = requests.delete('http://www.baidu.com')
resp_head = requests.head('http://www.baidu.com')
resp_options = requests.options('http://www.baidu.com')

# 打印put响应结果
print(resp_put.content.decode(encoding='utf-8'))

print('❀。。。。。。。。。。。。')

# 打印delete响应结果
print(resp_del.content.decode(encoding='utf-8'))
print(resp_del.headers)

print('❀。。。。。。。。。。。。')

# 打印head响应结果
print('响应头为：', resp_head.headers)
print('文本格式的响应头：', resp_head.text)

print('❀。。。。。。。。。。。。')

# 打印options方法的响应结果
print(resp_options.content.decode(encoding='utf-8'))


















