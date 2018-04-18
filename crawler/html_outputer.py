class HtmlOutputer(object):
    def __init__(self):
        self.datas = []  # 建立列表存放数据

    def collect_data(self, data):  # 收集数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):  # 用收集好输出到html文件中
            fout = open('output.html', 'w', encoding='utf-8')# 写模式
            fout.write("<html>")
            fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
            fout.write("<body>")
            fout.write("<table>")  # 输出为表格形式
            # ascii
            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])  # 输出url
                fout.write('<td>%s</td>' % data['title'])
                fout.write('<td>%s</td>' % data['summary'])
                fout.write("</tr>")

            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")  # 闭合标签

            fout.close()