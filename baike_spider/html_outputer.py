#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

# 5. 输出器  (数据写出到html页面  )



class HtmlOutputer(object):



    def __init__(self):

        #列表来维护收集的数据
        self.datas = []


    def collect_data(self,data):
        # 用于收集数据

        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        # 将收集好的数据写入到html文件中,
        # 打开这文件就可以看到收集好的数据

        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write('''<head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"></head>''')
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))  #python默认编码是ascii转换成utf8
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()