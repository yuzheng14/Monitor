from urllib import request
from lxml import etree
from log import log

class Crawler:
    __url__ = 'https://jwc.wh.sdu.edu.cn/gztz.htm'

    def crawl(self):
        '''
        爬取教务处工作通知网站的源码
        '''
        self.__html = request.urlopen(self.__url__)
        self.__html_content__ = self.__html.read().decode()
        self.__selector__ = etree.HTML(self.__html_content__)
        self.__data__ = self.__selector__.xpath(
            '//*[@id="content"]/div[2]/div[2]/div[1]/ul') #定位通知所在的无序列表
        self.__children__ = self.__data__[0].getchildren() # 获取子节点
        self.__nodes__ = []
        for child in self.__children__:
            self.__nodes__.append(child.getchildren()[0]) # 取子节点中的第一个子节点，即通知名称及超链接所在节点

    def crawl_titles(self):
        '''
        爬取教务处工作通知网站通知的标题
        '''
        titles = []
        for node in self.__nodes__:
            titles.append(node.attrib['title'])
        return titles

    def crawl_content(self, number):
        '''
        爬取教务处工作通知网站的前number条通知
        '''
        
        urls = []
        for node in self.__nodes__[:number]:
            href=node.attrib['href']
            urls.append(f'https://jwc.wh.sdu.edu.cn/{href}')
        content=self.__crawl_all_content__(urls)

        return content

    def __crawl_all_content__(self,urls):
        '''
        根据urls爬取所有页面的正文内容并返回
        '''
        content=[]
        for url in urls:
            
            text=f'<a href=\'{url}\'>点此前往通知页面</a>'
            try:
                data=etree.HTML(request.urlopen(url).read().decode()).xpath('//*[@id="content"]/div[2]/div[2]/form') # 通知具体内容
                for i in data[0].getchildren()[1:]:
                    text+=etree.tostring(i).decode()
            except:
                log(F'爬取{url}失败')
                text+=F'当前页面无法访问，请单击超链接前往网页'

            content.append(text)
            
        return content

if __name__=='__main__':
    crawler=Crawler()
    crawler.crawl()
    content=crawler.crawl_content(20)
    print(content)
