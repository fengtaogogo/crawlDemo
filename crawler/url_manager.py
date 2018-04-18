class UrlManager(object):
    # 维护两个列表，待爬取列表，爬取过的列表
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):  # 向管理器添加新的url
        if url is None:
            return
        # 该url即不在待爬取的列表也不在已爬取的列表
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)  # 用来待爬取

    def add_new_urls(self, urls):  # 向管理器中添加批量url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):  # 判断管理器是否有新的url
        # 如果待爬取的列表不等于0就有
        return len(self.new_urls) != 0

    def get_new_url(self):  # 从管理器获取新的url
        new_url = self.new_urls.pop()  # 从待爬取url集合中取一个url，并把这个url从集合中移除
        self.old_urls.add(new_url)  # 把这个url添加到已爬取的url集合中
        return new_url