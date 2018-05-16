from urllib import request  
from bs4 import BeautifulSoup            #Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库  
  
txt =''
top = 0
# 遍历豆瓣网站，爬虫分页数据
for i in range(10):
	start =i*25
	#构造头文件，模拟浏览器访问  
	url="https://movie.douban.com/top250?start="+str(start) 
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  
	page = request.Request(url,headers=headers)  
	page_info = request.urlopen(page).read().decode('utf-8')#打开Url,获取HttpResponse返回对象并读取其ResposneBody  
	soup = BeautifulSoup(page_info ,'html.parser') #将html.parser作为解析器  
	info = soup.select('.info')

	for moive in info:
		top=top+1
		txt += 'Top'+str(top) + ' 电影名：'
		for title in moive.select('.hd .title'):
			txt += title.string
			pass
		
		txt += '  评分：'+moive.select('.bd .star .rating_num')[0].string
		txt +='\n\r' 

	#打开一个文件,window下需要加 utf-8 ,因为 新创建的文件默认为gbk
	fo = open("movietop.txt", "w",encoding='utf-8')

	#写入
	fo.write(txt)
	 
	# 关闭打开的文件
	fo.close()
#   