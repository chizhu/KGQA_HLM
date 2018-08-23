# KGQA_HLM
基于知识图谱的《红楼梦》人物关系可视化及问答系统

<del>* 详情请见[http://chizhunlp.com](http://111.230.92.110/)</del>

1)  app.py是整个系统的主入口<br>
2)  templates文件夹是HTML的页面<br>
     |-index.html 欢迎界面<br> 
     |-search.html 搜索人物关系页面<br>
     |-all_relation.html 所有人物关系页面<br>
     |-KGQA.html 人物关系问答页面<br>
3)  static文件夹存放css和js，是页面的样式和效果的文件<br>
4)  raw_data文件夹是存在数据处理后的三元组文件<br>
5)  neo_db文件夹是知识图谱构建模块<br>
     |-config.py 配置参数<br>
     |-create_graph.py 创建知识图谱，图数据库的建立<br>
     |-query_graph.py 知识图谱的查询<br>
6)  KGQA文件夹是问答系统模块<br>
     |-ltp.py 分词、词性标注、命名实体识别<br>
7)  spider文件夹是爬虫模块<br>
     |- get_*.py 是之前爬取人物资料的代码，已经产生好images和json 可以不用再执行<br>
     |-show_profile.py 是调用人物资料和图谱展示在前端的代码
<hr>

部署步骤：<br>
* 0.安装所需的库 执行pip install -r requirement.txt<br>
* 1.先下载好neo4j图数据库，并配好环境（注意neo4j需要jdk8）。修改neo_db目录下的配置文件config.py,设置图数据库的账号和密码。<br>
* 2.切换到neo_db目录下，执行python  create_graph.py 建立知识图谱<br>
* 3.去 [这里](http://pyltp.readthedocs.io/zh_CN/latest/api.html#id2) 下载好ltp模型。[ltp简介](http://ltp.ai/)<br>
* 4.在KGQA目录下，修改ltp.py里的ltp模型文件的存放目录<br>
* 5.运行python app.py,浏览器打开localhost:5000即可查看<br>

系统整体流程图：

![流程](https://github.com/chizhu/KGQA_HLM/blob/master/%E5%9B%BE%E7%89%87%201.png)



