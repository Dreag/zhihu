# 知乎
- - -
#### 2017.12.30修改 
> 今天是17年的倒数第二天了，元旦哎，再撸撸代码放松放松。。

- 现阶段可爬取的内容为用户的粉丝数量和关注列表的信息。
- **待解决：反反爬虫策略**
> 使用ip代理池。<a href="http://www.daxiangdaili.com/">（这里使用大象代理。）</a>

#### 2018.1.1修改
- 新增了mysql数据库的存储。
- 去掉了headline字段。
- 问题：增加代理池的时候总是出现,未解决。
```python
TypeError: to_bytes must receive a unicode, str or bytes object, got NoneType.
```