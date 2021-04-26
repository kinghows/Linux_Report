# Linux_Report
Linux Report is a tool to help trouble shoot application base on linux.

pip install prettytable

if no internet:

rpm -ivh python36-3.6.8-2.0.1.module+el8.3.0+el8+9688+bb1990d3.x86_64.rpm

tar -zxvf  setuptools_scm-5.0.2.tar.gz

cd /.../setuptools_scm-5.0.2/

python3 setup.py build

python3 setup.py install

tar -zxvf  prettytable-2.1.0.tar.gz

cd /.../prettytable-2.1.0/

python3 setup.py build

python3 setup.py install

Edit application commands in linux_report.ini

execute:

python3 linux_report.py

python3 linux_report.py -p linux_report.ini

python3 linux_report.py -p linux_report.ini -s txt >linux_report.txt

python3 linux_report.py -p linux_report.ini -s html >linux_report.html

use crontab regularly perform linux_report.sh,auto generate  report,and send email.

Enjoy it! 

## 好用的DBA系列，喜欢的打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)

- [Logthin：日志精简工具](https://github.com/kinghows/Logthin)

- [Linux_Report：自定义Linux 命令生成HTML报告](https://github.com/kinghows/Linux_Report)

