import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    # 构造函数，初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downLoader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    # root_url入口url
    def craw(self, root_url):
        count = 1  # 记录当前爬去的第几个url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  # 判断有没有url
            try:
                new_url = self.urls.get_new_url()  # 如果有url，就添加到urls
                print("craw链接 %s : %s" % (count, new_url))
                html_cont = self.downLoader.download(new_url)  # 下载的页面数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)  # 收集
                if count == 1000:
                    break
                count = count + 1
            except:
                print("craw failed")

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)