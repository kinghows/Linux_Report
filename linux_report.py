#!/usr/local/bin/python
# coding: utf-8

# Linux_Report V1.0.0 for python3
# Trouble shoot application base on Linux
# Copyright (C) 2021-2021 Kinghow - Kinghow@hotmail.com
# Git repository available at https://github.com/kinghows/Linux_Report


import getopt
import sys
import configparser
import math
import time
import os
import prettytable
import platform
import glob
import re
from collections import OrderedDict
from collections import namedtuple
from warnings import filterwarnings

tab1="="
tab2="*"
linesize=104

def f_print_title(title):
    print ()
    print (int((linesize-4)/2 - int(len(title)/2)) * tab1, title, int((linesize-4)/2+1 - int(len(title)/2)) * tab1)
    print ()

def f_print_table_txt(rows, title, style):
    field_names = []
    fields = []
    f_print_title(title)
    table = prettytable.PrettyTable()
    for row in rows[1:]:
        table.add_row(row)
    if style not in (0,-1):
        for k in style.keys():
            field_names.append(style[k].split(',')[0])
        table.field_names = field_names
        for k in style.keys():
            table.align[style[k].split(',')[0]] = style[k].split(',')[1]
        for k in style.keys():
            if style[k].split(',')[1] != 'n':
                fields.append(style[k].split(',')[0])
        print(table.get_string(fields = fields))
    else:
        table.header =False
        print(table)

def f_print_table_html(rows, title, style):
    print ("""<p /><h3 class="awr"><a class="awr" name="99999"></a>""" + title + "</h3><p />")
    print ("""<table border="1">""")

    print ("""<tr>""",end='')
    for k in style.keys():
        if style[k].split(',')[1] != 'n':
            v = style[k]
            print ("""<th class="awrbg">""",end='')
            print (v.split(',')[0],end='')
            print ("""</th>""",end='')
    print ("""</tr>""")

    linenum = 0
    for row in rows:
        k = 0
        linenum += 1
        print ("<tr>",end='')
        if linenum % 2 == 0:
            classs='awrc'
        else:
            classs='awrnc'

        for col in row:
            k += 1
            if style[k].split(',')[1] == 'r':
                print ("""<td align="right" class='"""+classs+"'>"+str(col)+"</td>",end='')
            elif style[k].split(',')[1] == 'l':
                print ("""<td class='"""+classs+"'>"+str(col)+"</td>",end='')
        print ("</tr>")
    print ("""</table>
<br /><a class="awr" href="#top">Back to Top</a>
<p />
<p />
        """)

def f_print_table(rows,title,style,save_as):
    if save_as == "txt":
        f_print_table_txt(rows, title, style)
    elif save_as == "html":
        f_print_table_html(rows, title, style)

def f_print_cmd(title, cmd, style,save_as):
    rows =[]
    for line in os.popen(cmd).readlines():
        rows.append(line.strip().split())
    
    if strstyle!='0':
        del rows[0]
    style = eval(style)
    f_print_table(rows, title, style,save_as)

def f_print_caption(report_title,save_as):
    if save_as == "txt":
        print (tab2 * linesize)
        print (tab2, report_title.center(linesize - 4), tab2)
        print (tab2 * linesize)
    elif save_as == "html":
        print ("""
<html><head><title>Linux_Report V1.0.0  https://github.com/kinghows/Linux_Report </title>
<style type=\"text/css\">
body.awr {font:bold 10pt Arial,Helvetica,Geneva,sans-serif;color:black; background:White;}
pre.awr  {font:8pt Courier;color:black; background:White;}
h1.awr   {font:bold 20pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;border-bottom:1px solid #cccc99;margin-top:0pt; margin-bottom:0pt;padding:0px 0px 0px 0px;}
h2.awr   {font:bold 18pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}
h3.awr {font:bold 16pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}
li.awr {font: 8pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;}
th.awrnobg {font:bold 8pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;padding-left:4px; padding-right:4px;padding-bottom:2px}
th.awrbg {font:bold 8pt Arial,Helvetica,Geneva,sans-serif; color:White; background:#0066CC;padding-left:4px; padding-right:4px;padding-bottom:2px}
td.awrnc {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;}
td.awrc    {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;}
td.awrnclb {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-left: thin solid black;}
td.awrncbb {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-left: thin solid black;border-right: thin solid black;}
td.awrncrb {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-right: thin solid black;}
td.awrcrb    {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-right: thin solid black;}
td.awrclb    {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-left: thin solid black;}
td.awrcbb    {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-left: thin solid black;border-right: thin solid black;}
a.awr {font:bold 8pt Arial,Helvetica,sans-serif;color:#663300; vertical-align:top;margin-top:0pt; margin-bottom:0pt;}
td.awrnct {font:8pt Arial,Helvetica,Geneva,sans-serif;border-top: thin solid black;color:black;background:White;vertical-align:top;}
td.awrct   {font:8pt Arial,Helvetica,Geneva,sans-serif;border-top: thin solid black;color:black;background:#FFFFCC; vertical-align:top;}
td.awrnclbt  {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-top: thin solid black;border-left: thin solid black;}
td.awrncbbt  {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-left: thin solid black;border-right: thin solid black;border-top: thin solid black;}
td.awrncrbt {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;border-top: thin solid black;border-right: thin solid black;}
td.awrcrbt     {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-top: thin solid black;border-right: thin solid black;}
td.awrclbt     {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-top: thin solid black;border-left: thin solid black;}
td.awrcbbt   {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;border-top: thin solid black;border-left: thin solid black;border-right: thin solid black;}
table.tdiff {  border_collapse: collapse; }
</style></head><body class="awr">
<h1 class="awr">
       """)
        print (report_title)
        print ("</h1>")


def f_print_ending(save_as):
    if save_as == "txt":
        f_print_title('--@--  End  --@--')
    elif save_as == "html":
        print ("""
    <p />
    End of Report
    </body></html>
             """)

def size(device):
    nr_sectors = open(device+'/size').read().rstrip('\n')
    sect_size = open(device+'/queue/hw_sector_size').read().rstrip('\n')
    return (float(nr_sectors)*float(sect_size))/(1024.0*1024.0*1024.0)

def f_print_linux_info(save_as):
    title = "Linux info"
    style = {1: 'Linux,l',2: 'Info,l'}
    rows =[]
    #version
    rows.append(["Version",platform.uname()[0]+' '+platform.uname()[2]+' '+platform.uname()[4]])
    #cpu
    cpu_count = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    cpu_count +=1
    rows.append(["CPU",model_name + ' X '+str(cpu_count)])
    #mem
    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    rows.append(["Memory",'Total: {0}'.format(meminfo['MemTotal'])+' Free: {0}'.format(meminfo['MemFree'])])
    #net
    with open('/proc/net/dev') as f:
        net_dump = f.readlines()
    device_data = {}
    data = namedtuple('data', ['rx', 'tx'])
    for line in net_dump[2:]:
        line = line.split(':')
        if line[0].strip() != 'lo':
            device_data[line[0].strip()] = data(float(line[1].split()[0]) / (1024.0 * 1024.0),
                                                float(line[1].split()[8]) / (1024.0 * 1024.0))
    for dev in device_data.keys():
        rows.append(["Net",'{0}: {1} MiB {2} MiB'.format(dev, device_data[dev].rx, device_data[dev].tx)])
    #Device
    dev_pattern = ['sd.*', 'mmcblk*']
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                rows.append(["Device",'{0}, Size: {1} GiB'.format(device, size(device))])
    #process
    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)
    rows.append(["Processes",'Total number of running : {0}'.format(len(pids))])

    f_print_table(rows, title, style,save_as)

if __name__=="__main__":
    config_file="linux_report.ini"
    option = []
    save_as = "txt"
    report_title=""
    report_count = 0

    opts, args = getopt.getopt(sys.argv[1:], "p:s:")
    for o,v in opts:
        if o == "-p":
            config_file = v
        elif o == "-s":
            save_as = v

    config = configparser.ConfigParser()
    config.read(config_file)
    report_title = config.get("report", "report_title")
    report_count = int(config.get("report", "report_count"))

    f_print_caption(report_title,save_as)

    if config.get("option","linux_info")=='ON':
        f_print_linux_info(save_as)

    n = 1
    while n <= report_count:
        switch = config.get ( "report", "switch"+str(n))
        if switch == 'ON':
            title = config.get ( "report", "title"+str(n))
            cmd = config.get ( "report", "cmd"+str(n))
            strstyle = config.get ( "report", "style"+str(n))
            f_print_cmd(title, cmd, strstyle,save_as)
        n += 1

    f_print_ending(save_as)