import requests
import re

def get_data(start,end,date,s_data):
    url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-10-21&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
    # url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(date,start,end)
    print(url)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Accept': '*/*',
        'Connection':'keep-alive',
        'Cookie': '_uab_collina=160112445772772949021457; JSESSIONID=1CDDE84DF88E2BF277E748F73AD6FEE9; _jc_save_wfdc_flag=dc; RAIL_DEVICEID=CfI_vz8-I9gC9e0EAYH-RnE_S16g1ITxBQNQn1n319jka7XaSaLa6ti2956sJSSpwmxmmziw3N_E_5e6KYaNYFJxD1FEIPlbjfofYRmAylO7ygF4ImnkEMVoTa9Bb7b62MA36fu-9wyPP1fTryX_Mck33i0f6HhX; RAIL_EXPIRATION=1602856744171; _jc_save_toStation=%u4E0A%u6D77%2CSHH; BIGipServerpassport=837288202.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=2062024970.50210.0000; _jc_save_fromDate="'+date+'"; _jc_save_toDate="'+date+'"; _jc_save_fromStation=%u6210%u90FD%2CCDW',}
    response=requests.get(url,headers=headers)
    # response.encoding='utf-8'

    if response.status_code == 200:
        a = response.json()["data"]["result"]
        # print(a)
        city = get_city_e(s_data)
        # 遍历获取车次的列表，车次的信息中间是用|进行分割
        for item in a:
            i=item.split('|')
            print(i)
            print(i[3],city[i[6]],city[i[7]],i[31],i[30],i[13])
    else:
        print("出错啦")

# 获取station_name的信息
def get_city():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9161'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Cookie': '_uab_collina=160112445772772949021457; JSESSIONID=1CDDE84DF88E2BF277E748F73AD6FEE9; _jc_save_wfdc_flag=dc; RAIL_DEVICEID=CfI_vz8-I9gC9e0EAYH-RnE_S16g1ITxBQNQn1n319jka7XaSaLa6ti2956sJSSpwmxmmziw3N_E_5e6KYaNYFJxD1FEIPlbjfofYRmAylO7ygF4ImnkEMVoTa9Bb7b62MA36fu-9wyPP1fTryX_Mck33i0f6HhX; RAIL_EXPIRATION=1602856744171; _jc_save_toStation=%u4E0A%u6D77%2CSHH; BIGipServerpassport=837288202.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=2062024970.50210.0000; _jc_save_fromDate=2020-10-14; _jc_save_toDate=2020-10-14; _jc_save_fromStation=%u6210%u90FD%2CCDW',}
    resp = requests.get(url,headers=headers)
    # resp.encoding = 'utf-8'
    station = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)',resp.text)
    # 将列表转换成字典
    station_data = dict(station)
    return station_data
def get_city_e(s_data):
    # print(station_data)
    station_d = {}  # 空字典，用于将key和value进行交换
    for item in s_data:
        station_d[s_data[item]] = item
    # print(station_d)
    return station_d

def main():
    start="成都"
    end="上海"
    date="2010-10-14"
    s_data = get_city()
    # print(s_data)
    start=s_data[start]
    end=s_data[end]
    get_data(start,end,date,s_data)



if __name__ == "__main__":
    main()