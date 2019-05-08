#! python3
#-*-coding:gbk-*-
# hefengtianqi.py - Prints the current weather for a location from the command line.The api this program used
# transfer from https://www.heweather.com/documents/api/s6/weather-now  ʵ������

import json, requests, sys

# Compute location from command line arguments.
#if len(sys.argv) < 2:
#    print('Usage: quickWeather.py location')
#    sys.exit()
#location = ' '.join(sys.argv[1:])

# Download the JSON data from https://www.heweather.com's API
#loc='%s'%location
print('��������Ҫ��ѯ�ĳ��У�')
loc=input()
#The key is used for my personal usage, please do not use it random, thx.
key1='38810bc1e40a401fb6ca6ff04a4f056b'
canshu={'location':loc,'key':key1}
#url=r'https://free-api.heweather.com/s6/weather/now?location=%s&key=38810bc1e40a401fb6ca6ff04a4f056b'%(location)
#response = requests.get(url)
response = requests.get(r'https://free-api.heweather.com/s6/weather/now',params=canshu)
response.raise_for_status()

#airquality=r'https://free-api.heweather.com/s6/air/now?location=%s&key=38810bc1e40a401fb6ca6ff04a4f056b'%(location)
#airqual=requests.get(airquality)
airqual=requests.get(r'https://free-api.heweather.com/s6/air/now',params=canshu)
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
airData=json.loads(airqual.text)

# Print weather descriptions.
w = weatherData['HeWeather6']
a = airData['HeWeather6']
#print('���У�%s' % (loc),'����ʱ�䣺'+w[0]['update']['loc'])
print('����:'+w[0]['basic']['location'],'����ʱ�䣺'+w[0]['update']['loc'])
#print('���У�%s' % (location),'����ʱ�䣺'+w[0]['update']['loc'])
print('����:'+w[0]['now']['cond_txt'],'  ����:'+w[0]['now']['wind_dir'])
print('����¶�:'+w[0]['now']['fl']+'��','�¶�:'+w[0]['now']['tmp']+'��')
print('����������'+a[0]['air_now_city']['qlty'],'PM2.5:'+a[0]['air_now_city']['pm25'],'PM10:'+a[0]['air_now_city']['pm10'])

#test2
# Compute location from command line arguments.
#if len(sys.argv) < 2:
#    print('Usage: quickWeather.py location')
#    sys.exit()
#location = ' '.join(sys.argv[1:])

# Download the JSON data from https://www.heweather.com's API
#loc='%s'%location
#url=r'https://free-api.heweather.com/s6/weather/now?location=%s&key=38810bc1e40a401fb6ca6ff04a4f056b'%(location)
#response = requests.get(url)
#response.raise_for_status()

#airquality=r'https://free-api.heweather.com/s6/air/now?location=%s&key=38810bc1e40a401fb6ca6ff04a4f056b'%(location)
#airqual=requests.get(airquality)
# Load JSON data into a Python variable.
#weatherData = json.loads(response.text)
#airData=json.loads(airqual.text)

# Print weather descriptions.
#w = weatherData['HeWeather6']
#a=airData['HeWeather6']
#print('���У�%s' % (location),'����ʱ�䣺'+w[0]['update']['loc'])
#print('����:'+w[0]['now']['cond_txt'],'����:'+w[0]['now']['wind_dir'])
#print('����¶�:'+w[0]['now']['fl']+'��','�¶�:'+w[0]['now']['tmp']+'��')
#print('��Ҫ��Ⱦ�� ','PM2.5:'+a[0]['air_now_city']['pm25'],'PM10:'+a[0]['air_now_city']['pm10'])