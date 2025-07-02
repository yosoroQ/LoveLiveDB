* 现已上线，但仅供测试（数据未完全填充）：http://ll.mxzfun.xyz/

# LoveLiveDatabase
* 现阶段v1.0为静态页面，主要页面分为：`首页/成员`、`CV`、`歌曲`、`BD/DVD`、`TV`和`思维导图`。
* ~~后台管理是给弱者用的，强者直接写死数据~~（bushi）。
* 那你要问既然是静态的，我这几百条数据怎么插，手插？那当然不可能，那就得请Python来了，借助`Crawler/excelToTxt.py`将爬取出去的Excel表格数据转变为html的`<tr><td>`语句，输出示例如`Crawler/lovelive_table_rows.txt`所示。
* 移动端已适配，PC端页面有待优化。
* 数据来源：<https://ll-fans.jp/>， 爬虫示例：`Crawler/pa.py`。（命名不规范，后续修改）
* 先构建好v1.0版本，后续有新增模块，数据量较大的情况下重构引入后端和数据库(v2.0)。
