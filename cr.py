import requests
from bs4 import BeautifulSoup
import os

# 创建一个soup对象
def get_soup(url):
    r = requests.get(url, headers=headers)
    html = r.text
    return BeautifulSoup(html, 'html.parser')

# 获取原图链接并将图片保存到本地
def get_jpg(soup):
    global index
    for link in soup.find_all('a', {'class': 'view_img_link'}):
        href = link.get('href')
        with open('{}{}.jpg'.format(root, index), 'wb') as f:
            f.write(requests.get('http:' + href).content)
        print('成功爬取%d张图片' % index)
        index += 1


if __name__ == '__main__':
    root = '/Users/sssningzhiyuan/Desktop/study/pic'
    os.mkdir(root)  #创建一个文件夹
    index = 1    # 初始化图片索引
    depth = 30   # 指定爬取页数
    url = 'http://jandan.net/ooxx'
    headers = {'referer': 'http://jandan.net/',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    for i in range(depth):
        soup = get_soup(url)
        get_jpg(soup)
        url = 'http:' + soup.find('a', {'class': 'previous-comment-page'}).get('href')