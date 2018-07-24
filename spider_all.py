# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2018/7/5 20:41
# @Author  : lemon



from lib.is_key_or_isbn import is_key_or_isbn
from .spider import Spider, Spider_keyword


def spider_all(keyword):

    keyword = keyword.strip()
    key_or_isbn = is_key_or_isbn(keyword)
    spider_isbn = Spider()
    spider_keyword = Spider_keyword()

    if key_or_isbn == 'isbn':
        spider_isbn.save(keyword)
    else:
        page = input('请输入要抓取的页数：').strip()
        spider_keyword.save(keyword,page)



if __name__ == '__main__':
    keyword = input('请输入关键词: ').strip()
    spider_all(keyword)





