# 将输入的URL字符串按照'?'分割成两部分，前面是路径，后面是查询参数
def parse_url(url:str) ->dict:
    temp=url.split('?')
    url=temp[1]#只取？后面的
    params=url.split('&')
    parse_dict={}
    for param in params:
        key , value =param.split('=')
        parse_dict[key]=value
    return parse_dict

url = "www.baidu.com?name=John&age=30&city=New%20York"
parsed_params = parse_url(url)
print(parsed_params)