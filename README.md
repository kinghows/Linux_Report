# Linux_Report
Linux Report is a tool to help trouble shoot application base on linux.

python3.6.8

pip3  install prettytable

Edit application commands in linux_report.ini

A few sample Linux commands have been written in linux_report.ini,You can write commands to monitor business systems.

linux_report.txt & linux_report.html is  execution result demo.

example:

![txt example](https://github.com/kinghows/Linux_Report/blob/master/txt.jpg)

![html example](https://github.com/kinghows/Linux_Report/blob/master/html.jpg)

execute:

python3 linux_report.py

python3 linux_report.py -p linux_report.ini

python3 linux_report.py -p linux_report.ini -s txt >linux_report.txt

python3 linux_report.py -p linux_report.ini -s html >linux_report.html

send email:

python3 SendEmail3.py -p emailset.ini -f linux_report.txt

use crontab regularly perform linux_report.sh,auto generate  report,and send email.

Enjoy it! 

## 好用的DBA系列，喜欢的打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)

- [Logthin：日志精简工具](https://github.com/kinghows/Logthin)

- [Logchart：日志图形化工具](https://github.com/kinghows/Logchart)

- [Linux_Report：自定义Linux 命令生成HTML报告](https://github.com/kinghows/Linux_Report)

