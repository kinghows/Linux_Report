#!/bin/sh
report_base=/services/script
datetime=`date +%Y-%m-%d_%H-%M`
python3 $report_base/linux_report.py -p $report_base/linux_report.ini  -s html>$report_base/linux_report_$datetime.html
