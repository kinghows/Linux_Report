#!/bin/sh
PATH="/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin:$PATH"
report_base=/var/log/linux_report
datetime=`date +%Y-%m-%d_%H-%M`
python3 $report_base/linux_report.py -p $report_base/linux_report.ini  -s txt>$report_base/linux_report_$datetime.log
python $report_base/SendEmail.py -p $report_base/emailset.ini -f $report_base/linux_report_$datetime.log
find $report_base -mtime +30 -name "linux_report_*.log" -exec rm -rf {} \;
