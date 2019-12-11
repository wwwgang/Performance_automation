性能自动化，支持模板导入，html报告导出

入门说明：
第一步：
pip install git+https://github.com/wg18618262234/locust.git
第二步：
在preformance_automation.csv编写接口信息
第三步：
1、分布式：主机使用命令locust --master，被代理机使用命令locust --slave --master-host=x.x.x.x
2、单机：使用命令locust。单机建议使用单机分布式可尽可能跑满本台u性能（单机分布式，启动多个进程，主进程命令locust --master，副进程locust --slave）
第四步：
访问web查看并开始压测，web入口http://masterip:8089/
第五步：
压测结束在web页面导出报告（目前一缺点，分布式master分发给slave任务后生成的error_info.csv信息只能够存在slave客户机上，还无法收回csv文件）

官网：https://locust.io/
官方文档：https://docs.locust.io/en/stable/
