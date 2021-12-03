import requests, bs4, openpyxl
import string
# 创建工作簿
def get_movie_list():
    wb = openpyxl.Workbook()
    # 获取工作簿的活动表
    sheet = wb.active
    # 工作表重命名
    sheet.title = 'movies'

    sheet['A1'] = '序号'  # 加表头，给A1单元格赋值
    sheet['B1'] = '电影名'  # 加表头，给B1单元格赋值
    sheet['C1'] = '主演'  # 加表头，给C1单元格赋值
    sheet['D1'] = '推荐语'  # 加表头，给D1单元格赋值
    sheet['E1'] = '链接'  # 加表头，给E1单元格赋值
    sheet['F1'] = '年份'
    sheet['G1'] = '出版地'
    sheet['H1'] = '种类'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}#伪装请求头
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
        res = requests.get(url, headers=headers)
        bs = bs4.BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
        for titles in bs.find_all('li'):
            num = titles.find('em', class_="").text
            title = titles.find('span', class_="title").text
            info = titles.find('p', class_="").text
            url_movie = titles.find('a')['href']
            list = info.split("\n")
            actor = list[1].split("/")[0].strip().strip('.')
            # actor1 = actor.replace(string.ascii_uppercase,'')
            year = list[2].split("/")[0].strip()
            place = list[2].split("/")[1].strip()
            kind = list[2].split("/")[2].strip()

            if titles.find('span', class_="inq") != None:
                tes = titles.find('span', class_="inq").text
                sheet.append([num, title, actor, tes, url_movie, year, place, kind])
            else:
                sheet.append([num, title, actor, None, url_movie, year, place, kind])
    # 最后保存并命名这个Excel文件
    wb.save('movieTop250.xlsx')

