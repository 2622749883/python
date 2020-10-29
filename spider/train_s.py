# 模拟浏览器向服务器发送请求
import requests
import re
import urllib.request as r
import urllib.parse      # 编码

# 由于火车站使用三字码，所以我们需要先获取站点对应的三字码
code_url = r"https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
code_data = r.urlopen(code_url).read().decode('utf-8')
# print(code_data)

# 处理获得的字符串，返回字典类型
def zip_dic(code_data):
    code_data = code_data[20:]
    # print(code_data)
    list_code = code_data.split("|")
    # print(list_code)
    a=1
    b=2
    t1=[]
    t2=[]
    while (a < (len(list_code))):
        t1.append(list_code[a])
        t2.append(list_code[b])
        a = a + 5
        b = b + 5
    dic = dict(zip(t1,t2))
    return dic
# print(code_dic)

# 定义函数，用户输入起始站终点站和时间，转化为编码做返回
def get_message(code_dic):
    from_station = input("输入起始站：\n")
    to_station = input("输入终点站：\n")
    time = input("输入时间，例如：2020-4-28:\n")
    for key, value in code_dic.items():
        if(key == from_station):
            from_station = value
        if(key == to_station):
            to_station = value
    return from_station, to_station, time

# 请求URL，由于该URL请求方式为get
def send_request():
    code_dic = zip_dic(code_data)
    from_station, to_station, time = get_message(code_dic)
    # url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-08-19&leftTicketDTO.from_station=IZQ&leftTicketDTO.to_station=XMS&purpose_codes=ADULT'
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(time, from_station, to_station)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
               'Cookie': '_uab_collina=159827773935642277475107; JSESSIONID=C0AAF2593A87C6ABEC63BB0F89A0AF30; BIGipServerotn=1725497610.64545.0000; RAIL_EXPIRATION=1602943779030; RAIL_DEVICEID=ZM0Un8RcwzaSrjYzZdEDLIJJEUFMC6fyFTrZbjgOyN_xK5z5tNUJFVHFB28AlPEFS0tgiRCK4kbLQIOl85_Go2VIBnJ6OiWazoJF2cXJ6N3NrqRKJ_tg75H0rfR3A8G2xgijkyi_CD1CtfWaHVCsICRGjCmPzODA; BIGipServerpassport=904397066.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_fromDate=2020-10-14; _jc_save_toDate=2020-10-14; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u6210%u90FD%2CCDW'}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    # print(resp.text)
    return resp
# 提取数据
def parse_json(resp,city):
    json_ticket = resp.json()     # 将响应结果转成json
    data_list = json_ticket["data"]["result"] # 提取车次的列表
    # 遍历每一个车次信息
    # d = data_list[0].split('|')
    lst = []
    for item in data_list:
        d = item.split('|')
        lst.append([d[3], city[d[6]], city[d[7]],d[8],d[9],d[10], d[32], d[31], d[30], d[21], d[23], d[28], d[27], d[29], d[26], d[13]])
    return lst
    '''3、车次
    4、车起始
    5、车终点
    6、查询起始点
    7、查询车终点
    8、出发时间
    9、到达时间
    10、历时
    21、高级软卧
    23、软卧一等座
    26、无座
    27、软座
    28、硬卧二等座
    29、硬座
    30、二等座、二等包座
    31、一等座
    32商务特等'''

def start():
    lst = parse_json(send_request(), get_city())
    print(lst)
    return lst
    # for i in lst:
    #     print(i)

        # if i[3]!='无'and i[3]!='':
        #     print(i)

# 获取站点信息
def get_city():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9152'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',resp.text)     #[\u4e00-\u9fa5]表示全部中文汉字

    # 将列表转成字典
    stations_data = dict(stations)
    station_d = {}
    for item in stations_data:
        station_d[stations_data[item]] = item
    return station_d

if __name__ == '__main__':
    start()