'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
除权最好一个月一次
@author: Administrator
'''

import pymysql
import jqdatasdk as jq
from jqdatasdk import finance
import time
from _datetime import datetime
 
#jqdata认证
jq.auth('13401179853','king179853')

print("...............开始修正除权数据..............................")
#建立连接# 获取游标
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg',
    charset='utf8'
)
cursor = connect.cursor()


#定义编码方法
def js(open,high,low,close):   
    d=0
    x=0
    if(open>=close):
        d=open
        x=close
    if(open<close):
        d=close
        x=open
    
    h=high-d
    l=x-low
    
    return h,l



#openzl=[[-10.6,-9.94],[-9.94,-7],[-7,-3],[-3,-1],[-1,1],[1,3],[3,7],[7,9.94],[9.94,10.6]]
#closezl=[[-10.6,-9.94],[-9.94,-7],[-7,-4],[-4,-2],[-2,-1],[-1,0],[0,1],[1,2],[2,4],[4,7],[7,9.94],[9.94,10.6]]
#normzl=[[0,1.5],[1.5,3.5],[3.5,20.5]]
def bm(open,high,low,close):
    num=0
    if(open>=-10.6 and open <=-9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            num=1
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=2
            if(h>=1.5 and h<3.5):
                num=3
            if(h>=3.5 and h<=20.5):
                num=4
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=5
            if(h>=1.5 and h<3.5):
                num=6
            if(h>=3.5 and h<=20.5):
                num=7
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=8
            if(h>=1.5 and h<3.5):
                num=9
            if(h>=3.5 and h<=20.5):
                num=10
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=11
            if(h>=1.5 and h<3.5):
                num=12
            if(h>=3.5 and h<=20.5):
                num=13
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=14
            if(h>=1.5 and h<3.5):
                num=15
            if(h>=3.5 and h<=20.5):
                num=16
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=17
            if(h>=1.5 and h<3.5):
                num=18
            if(h>=3.5 and h<=20.5):
                num=19
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=20
            if(h>=1.5 and h<3.5):
                num=21
            if(h>=3.5 and h<=20.5):
                num=22
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=23
            if(h>=1.5 and h<3.5):
                num=24
            if(h>=3.5 and h<=20.5):
                num=25
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=26
            if(h>=1.5 and h<3.5):
                num=27
            if(h>=3.5 and h<=20.5):
                num=28
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=29
            if(h>=1.5 and h<3.5):
                num=30
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            num=31





    if(open>-9.94 and open <-7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=32
            if(h>=1.5 and h<3.5):
                num=33
            if(h>=3.5 and h<=20.5):
                num=34
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=35
                if(l>=1.5 and l<3.5):
                    num=36
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=37
                if(l>=1.5 and l<3.5):
                    num=38
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=39
                if(l>=1.5 and l<3.5):
                    num=40
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=41
                if(l>=1.5 and l<3.5):
                    num=42
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=43
                if(l>=1.5 and l<3.5):
                    num=44
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=45
                if(l>=1.5 and l<3.5):
                    num=46
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=47
                if(l>=1.5 and l<3.5):
                    num=48
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=49
                if(l>=1.5 and l<3.5):
                    num=50
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=51
                if(l>=1.5 and l<3.5):
                    num=52
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=53
                if(l>=1.5 and l<3.5):
                    num=54
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=55
                if(l>=1.5 and l<3.5):
                    num=56
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=57
                if(l>=1.5 and l<3.5):
                    num=58
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=59
                if(l>=1.5 and l<3.5):
                    num=60
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=61
                if(l>=1.5 and l<3.5):
                    num=62
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=63
                if(l>=1.5 and l<3.5):
                    num=64
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=65
                if(l>=1.5 and l<3.5):
                    num=66
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=67
                if(l>=1.5 and l<3.5):
                    num=68
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=69
                if(l>=1.5 and l<3.5):
                    num=70
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=71
                if(l>=1.5 and l<3.5):
                    num=72
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=73
                if(l>=1.5 and l<3.5):
                    num=74
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=75
                if(l>=1.5 and l<3.5):
                    num=76
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=77
                if(l>=1.5 and l<3.5):
                    num=78
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=79
                if(l>=1.5 and l<3.5):
                    num=80
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=81
                if(l>=1.5 and l<3.5):
                    num=82
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=83
                if(l>=1.5 and l<3.5):
                    num=84
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=85
                if(l>=1.5 and l<3.5):
                    num=86
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=87
                if(l>=1.5 and l<3.5):
                    num=88
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=89
                if(l>=1.5 and l<3.5):
                    num=90
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=91
                if(l>=1.5 and l<3.5):
                    num=92
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=93
            if(l>=1.5 and l<3.5):
                num=94



    if(open>=-7 and open <-3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=95
            if(h>=1.5 and h<3.5):
                num=96
            if(h>=3.5 and h<=20.5):
                num=97
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=98
                if(l>=1.5 and l<3.5):
                    num=99
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=100
                if(l>=1.5 and l<3.5):
                    num=101
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=102
                if(l>=1.5 and l<3.5):
                    num=103
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=104
                if(l>=1.5 and l<3.5):
                    num=105
                if(l>=3.5 and l<20.5):
                    num=106
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=107
                if(l>=1.5 and l<3.5):
                    num=108
                if(l>=3.5 and l<20.5):
                    num=109
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=110
                if(l>=1.5 and l<3.5):
                    num=111
                if(l>=3.5 and l<20.5):
                    num=112
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=113
                if(l>=1.5 and l<3.5):
                    num=114
                if(l>=3.5 and l<=20.5):
                    num=115
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=116
                if(l>=1.5 and l<3.5):
                    num=117
                if(l>=3.5 and l<=20.5):
                    num=118
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=119
                if(l>=1.5 and l<3.5):
                    num=120
                if(l>=3.5 and l<=20.5):
                    num=121
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=122
                if(l>=1.5 and l<3.5):
                    num=123
                if(l>=3.5 and l<=20.5):
                    num=124
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=125
                if(l>=1.5 and l<3.5):
                    num=126
                if(l>=3.5 and l<=20.5):
                    num=127
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=128
                if(l>=1.5 and l<3.5):
                    num=129
                if(l>=3.5 and l<=20.5):
                    num=130
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=131
                if(l>=1.5 and l<3.5):
                    num=132
                if(l>=3.5 and l<=20.5):
                    num=133
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=134
                if(l>=1.5 and l<3.5):
                    num=135
                if(l>=3.5 and l<=20.5):
                    num=136
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=137
                if(l>=1.5 and l<3.5):
                    num=138
                if(l>=3.5 and l<=20.5):
                    num=139
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=140
                if(l>=1.5 and l<3.5):
                    num=141
                if(l>=3.5 and l<=20.5):
                    num=142
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=143
                if(l>=1.5 and l<3.5):
                    num=144
                if(l>=3.5 and l<=20.5):
                    num=145
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=146
                if(l>=1.5 and l<3.5):
                    num=147
                if(l>=3.5 and l<=20.5):
                    num=148
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=149
                if(l>=1.5 and l<3.5):
                    num=150
                if(l>=3.5 and l<=20.5):
                    num=151
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=152
                if(l>=1.5 and l<3.5):
                    num=153
                if(l>=3.5 and l<=20.5):
                    num=154
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=155
                if(l>=1.5 and l<3.5):
                    num=156
                if(l>=3.5 and l<=20.5):
                    num=157
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=158
                if(l>=1.5 and l<3.5):
                    num=159
                if(l>=3.5 and l<=20.5):
                    num=160
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=161
                if(l>=1.5 and l<3.5):
                    num=162
                if(l>=3.5 and l<=20.5):
                    num=163
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=164
                if(l>=1.5 and l<3.5):
                    num=165
                if(l>=3.5 and l<=20.5):
                    num=166
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=167
                if(l>=1.5 and l<3.5):
                    num=168
                if(l>=3.5 and l<=20.5):
                    num=169
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=170
                if(l>=1.5 and l<3.5):
                    num=171
                if(l>=3.5 and l<=20.5):
                    num=172
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=173
                if(l>=1.5 and l<3.5):
                    num=174
                if(l>=3.5 and l<=20.5):
                    num=175
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=176
                if(l>=1.5 and l<3.5):
                    num=177
                if(l>=3.5 and l<=20.5):
                    num=178
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=179
                if(l>=1.5 and l<3.5):
                    num=180
                if(l>=3.5 and l<=20.5):
                    num=181
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=182
            if(l>=1.5 and l<3.5):
                num=183
            if(l>=3.5 and l<=20.5):
                num=184




    if(open>=-3 and open <-1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=185
            if(h>=1.5 and h<3.5):
                num=186
            if(h>=3.5 and h<=20.5):
                num=187
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=188
                if(l>=1.5 and l<3.5):
                    num=189
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=190
                if(l>=1.5 and l<3.5):
                    num=191
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=192
                if(l>=1.5 and l<3.5):
                    num=193
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=194
                if(l>=1.5 and l<3.5):
                    num=195
                if(l>=3.5 and l<20.5):
                    num=196
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=197
                if(l>=1.5 and l<3.5):
                    num=198
                if(l>=3.5 and l<20.5):
                    num=199
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=200
                if(l>=1.5 and l<3.5):
                    num=201
                if(l>=3.5 and l<20.5):
                    num=202
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=203
                if(l>=1.5 and l<3.5):
                    num=204
                if(l>=3.5 and l<=20.5):
                    num=205
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=206
                if(l>=1.5 and l<3.5):
                    num=207
                if(l>=3.5 and l<=20.5):
                    num=208
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=209
                if(l>=1.5 and l<3.5):
                    num=210
                if(l>=3.5 and l<=20.5):
                    num=211
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=212
                if(l>=1.5 and l<3.5):
                    num=213
                if(l>=3.5 and l<=20.5):
                    num=214
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=215
                if(l>=1.5 and l<3.5):
                    num=216
                if(l>=3.5 and l<=20.5):
                    num=217
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=218
                if(l>=1.5 and l<3.5):
                    num=219
                if(l>=3.5 and l<=20.5):
                    num=220
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=221
                if(l>=1.5 and l<3.5):
                    num=222
                if(l>=3.5 and l<=20.5):
                    num=223
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=224
                if(l>=1.5 and l<3.5):
                    num=225
                if(l>=3.5 and l<=20.5):
                    num=226
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=227
                if(l>=1.5 and l<3.5):
                    num=228
                if(l>=3.5 and l<=20.5):
                    num=229
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=230
                if(l>=1.5 and l<3.5):
                    num=231
                if(l>=3.5 and l<=20.5):
                    num=232
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=233
                if(l>=1.5 and l<3.5):
                    num=234
                if(l>=3.5 and l<=20.5):
                    num=235
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=236
                if(l>=1.5 and l<3.5):
                    num=237
                if(l>=3.5 and l<=20.5):
                    num=238
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=239
                if(l>=1.5 and l<3.5):
                    num=240
                if(l>=3.5 and l<=20.5):
                    num=241
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=242
                if(l>=1.5 and l<3.5):
                    num=243
                if(l>=3.5 and l<=20.5):
                    num=244
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=245
                if(l>=1.5 and l<3.5):
                    num=246
                if(l>=3.5 and l<=20.5):
                    num=247
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=248
                if(l>=1.5 and l<3.5):
                    num=249
                if(l>=3.5 and l<=20.5):
                    num=250
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=251
                if(l>=1.5 and l<3.5):
                    num=252
                if(l>=3.5 and l<=20.5):
                    num=253
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=254
                if(l>=1.5 and l<3.5):
                    num=255
                if(l>=3.5 and l<=20.5):
                    num=256
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=257
                if(l>=1.5 and l<3.5):
                    num=258
                if(l>=3.5 and l<=20.5):
                    num=259
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=260
                if(l>=1.5 and l<3.5):
                    num=261
                if(l>=3.5 and l<=20.5):
                    num=262
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=263
                if(l>=1.5 and l<3.5):
                    num=264
                if(l>=3.5 and l<=20.5):
                    num=265
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=266
                if(l>=1.5 and l<3.5):
                    num=267
                if(l>=3.5 and l<=20.5):
                    num=268
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=269
                if(l>=1.5 and l<3.5):
                    num=270
                if(l>=3.5 and l<=20.5):
                    num=271
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=272
            if(l>=1.5 and l<3.5):
                num=273
            if(l>=3.5 and l<=20.5):
                num=274



    if(open>=-1 and open <1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=275
            if(h>=1.5 and h<3.5):
                num=276
            if(h>=3.5 and h<=20.5):
                num=277
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=278
                if(l>=1.5 and l<3.5):
                    num=279
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=280
                if(l>=1.5 and l<3.5):
                    num=281
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=282
                if(l>=1.5 and l<3.5):
                    num=283
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=284
                if(l>=1.5 and l<3.5):
                    num=285
                if(l>=3.5 and l<20.5):
                    num=286
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=287
                if(l>=1.5 and l<3.5):
                    num=288
                if(l>=3.5 and l<20.5):
                    num=289
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=290
                if(l>=1.5 and l<3.5):
                    num=291
                if(l>=3.5 and l<20.5):
                    num=292
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=293
                if(l>=1.5 and l<3.5):
                    num=294
                if(l>=3.5 and l<=20.5):
                    num=295
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=296
                if(l>=1.5 and l<3.5):
                    num=297
                if(l>=3.5 and l<=20.5):
                    num=298
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=299
                if(l>=1.5 and l<3.5):
                    num=300
                if(l>=3.5 and l<=20.5):
                    num=301
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=302
                if(l>=1.5 and l<3.5):
                    num=303
                if(l>=3.5 and l<=20.5):
                    num=304
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=305
                if(l>=1.5 and l<3.5):
                    num=306
                if(l>=3.5 and l<=20.5):
                    num=307
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=308
                if(l>=1.5 and l<3.5):
                    num=309
                if(l>=3.5 and l<=20.5):
                    num=310
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=311
                if(l>=1.5 and l<3.5):
                    num=312
                if(l>=3.5 and l<=20.5):
                    num=313
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=314
                if(l>=1.5 and l<3.5):
                    num=315
                if(l>=3.5 and l<=20.5):
                    num=316
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=317
                if(l>=1.5 and l<3.5):
                    num=318
                if(l>=3.5 and l<=20.5):
                    num=319
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=320
                if(l>=1.5 and l<3.5):
                    num=321
                if(l>=3.5 and l<=20.5):
                    num=322
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=323
                if(l>=1.5 and l<3.5):
                    num=324
                if(l>=3.5 and l<=20.5):
                    num=325
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=326
                if(l>=1.5 and l<3.5):
                    num=327
                if(l>=3.5 and l<=20.5):
                    num=328
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=329
                if(l>=1.5 and l<3.5):
                    num=330
                if(l>=3.5 and l<=20.5):
                    num=331
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=332
                if(l>=1.5 and l<3.5):
                    num=333
                if(l>=3.5 and l<=20.5):
                    num=334
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=335
                if(l>=1.5 and l<3.5):
                    num=336
                if(l>=3.5 and l<=20.5):
                    num=337
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=338
                if(l>=1.5 and l<3.5):
                    num=339
                if(l>=3.5 and l<=20.5):
                    num=340
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=341
                if(l>=1.5 and l<3.5):
                    num=342
                if(l>=3.5 and l<=20.5):
                    num=343
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=344
                if(l>=1.5 and l<3.5):
                    num=345
                if(l>=3.5 and l<=20.5):
                    num=346
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=347
                if(l>=1.5 and l<3.5):
                    num=348
                if(l>=3.5 and l<=20.5):
                    num=349
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=350
                if(l>=1.5 and l<3.5):
                    num=351
                if(l>=3.5 and l<=20.5):
                    num=352
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=353
                if(l>=1.5 and l<3.5):
                    num=354
                if(l>=3.5 and l<=20.5):
                    num=355
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=356
                if(l>=1.5 and l<3.5):
                    num=357
                if(l>=3.5 and l<=20.5):
                    num=358
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=359
                if(l>=1.5 and l<3.5):
                    num=360
                if(l>=3.5 and l<=20.5):
                    num=361
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=362
            if(l>=1.5 and l<3.5):
                num=363
            if(l>=3.5 and l<=20.5):
                num=364


    if(open>=1 and open <3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=365
            if(h>=1.5 and h<3.5):
                num=366
            if(h>=3.5 and h<=20.5):
                num=367
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=368
                if(l>=1.5 and l<3.5):
                    num=369
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=370
                if(l>=1.5 and l<3.5):
                    num=371
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=372
                if(l>=1.5 and l<3.5):
                    num=373
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=374
                if(l>=1.5 and l<3.5):
                    num=375
                if(l>=3.5 and l<20.5):
                    num=376
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=377
                if(l>=1.5 and l<3.5):
                    num=378
                if(l>=3.5 and l<20.5):
                    num=379
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=380
                if(l>=1.5 and l<3.5):
                    num=381
                if(l>=3.5 and l<20.5):
                    num=382
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=383
                if(l>=1.5 and l<3.5):
                    num=384
                if(l>=3.5 and l<=20.5):
                    num=385
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=386
                if(l>=1.5 and l<3.5):
                    num=387
                if(l>=3.5 and l<=20.5):
                    num=388
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=389
                if(l>=1.5 and l<3.5):
                    num=390
                if(l>=3.5 and l<=20.5):
                    num=391
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=392
                if(l>=1.5 and l<3.5):
                    num=393
                if(l>=3.5 and l<=20.5):
                    num=394
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=395
                if(l>=1.5 and l<3.5):
                    num=396
                if(l>=3.5 and l<=20.5):
                    num=397
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=398
                if(l>=1.5 and l<3.5):
                    num=399
                if(l>=3.5 and l<=20.5):
                    num=400
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=401
                if(l>=1.5 and l<3.5):
                    num=402
                if(l>=3.5 and l<=20.5):
                    num=403
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=404
                if(l>=1.5 and l<3.5):
                    num=405
                if(l>=3.5 and l<=20.5):
                    num=406
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=407
                if(l>=1.5 and l<3.5):
                    num=408
                if(l>=3.5 and l<=20.5):
                    num=409
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=410
                if(l>=1.5 and l<3.5):
                    num=411
                if(l>=3.5 and l<=20.5):
                    num=412
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=413
                if(l>=1.5 and l<3.5):
                    num=414
                if(l>=3.5 and l<=20.5):
                    num=415
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=416
                if(l>=1.5 and l<3.5):
                    num=417
                if(l>=3.5 and l<=20.5):
                    num=418
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=419
                if(l>=1.5 and l<3.5):
                    num=420
                if(l>=3.5 and l<=20.5):
                    num=421
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=422
                if(l>=1.5 and l<3.5):
                    num=423
                if(l>=3.5 and l<=20.5):
                    num=424
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=425
                if(l>=1.5 and l<3.5):
                    num=426
                if(l>=3.5 and l<=20.5):
                    num=427
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=428
                if(l>=1.5 and l<3.5):
                    num=429
                if(l>=3.5 and l<=20.5):
                    num=430
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=431
                if(l>=1.5 and l<3.5):
                    num=432
                if(l>=3.5 and l<=20.5):
                    num=433
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=434
                if(l>=1.5 and l<3.5):
                    num=435
                if(l>=3.5 and l<=20.5):
                    num=436
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=437
                if(l>=1.5 and l<3.5):
                    num=438
                if(l>=3.5 and l<=20.5):
                    num=439
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=440
                if(l>=1.5 and l<3.5):
                    num=441
                if(l>=3.5 and l<=20.5):
                    num=442
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=443
                if(l>=1.5 and l<3.5):
                    num=444
                if(l>=3.5 and l<=20.5):
                    num=445
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=446
                if(l>=1.5 and l<3.5):
                    num=447
                if(l>=3.5 and l<=20.5):
                    num=448
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=449
                if(l>=1.5 and l<3.5):
                    num=450
                if(l>=3.5 and l<=20.5):
                    num=451
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=452
            if(l>=1.5 and l<3.5):
                num=453
            if(l>=3.5 and l<=20.5):
                num=454




    if(open>=3 and open <7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=455
            if(h>=1.5 and h<3.5):
                num=456
            if(h>=3.5 and h<=20.5):
                num=457
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=458
                if(l>=1.5 and l<3.5):
                    num=459
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=460
                if(l>=1.5 and l<3.5):
                    num=461
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=462
                if(l>=1.5 and l<3.5):
                    num=463
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=464
                if(l>=1.5 and l<3.5):
                    num=465
                if(l>=3.5 and l<20.5):
                    num=466
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=467
                if(l>=1.5 and l<3.5):
                    num=468
                if(l>=3.5 and l<20.5):
                    num=469
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=470
                if(l>=1.5 and l<3.5):
                    num=471
                if(l>=3.5 and l<20.5):
                    num=472
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=473
                if(l>=1.5 and l<3.5):
                    num=474
                if(l>=3.5 and l<=20.5):
                    num=475
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=476
                if(l>=1.5 and l<3.5):
                    num=477
                if(l>=3.5 and l<=20.5):
                    num=478
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=479
                if(l>=1.5 and l<3.5):
                    num=480
                if(l>=3.5 and l<=20.5):
                    num=481
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=482
                if(l>=1.5 and l<3.5):
                    num=483
                if(l>=3.5 and l<=20.5):
                    num=484
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=485
                if(l>=1.5 and l<3.5):
                    num=486
                if(l>=3.5 and l<=20.5):
                    num=487
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=488
                if(l>=1.5 and l<3.5):
                    num=489
                if(l>=3.5 and l<=20.5):
                    num=490
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=491
                if(l>=1.5 and l<3.5):
                    num=492
                if(l>=3.5 and l<=20.5):
                    num=493
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=494
                if(l>=1.5 and l<3.5):
                    num=495
                if(l>=3.5 and l<=20.5):
                    num=496
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=497
                if(l>=1.5 and l<3.5):
                    num=498
                if(l>=3.5 and l<=20.5):
                    num=499
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=500
                if(l>=1.5 and l<3.5):
                    num=501
                if(l>=3.5 and l<=20.5):
                    num=502
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=503
                if(l>=1.5 and l<3.5):
                    num=504
                if(l>=3.5 and l<=20.5):
                    num=505
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=506
                if(l>=1.5 and l<3.5):
                    num=507
                if(l>=3.5 and l<=20.5):
                    num=508
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=509
                if(l>=1.5 and l<3.5):
                    num=510
                if(l>=3.5 and l<=20.5):
                    num=511
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=512
                if(l>=1.5 and l<3.5):
                    num=513
                if(l>=3.5 and l<=20.5):
                    num=514
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=515
                if(l>=1.5 and l<3.5):
                    num=516
                if(l>=3.5 and l<=20.5):
                    num=517
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=518
                if(l>=1.5 and l<3.5):
                    num=519
                if(l>=3.5 and l<=20.5):
                    num=520
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=521
                if(l>=1.5 and l<3.5):
                    num=522
                if(l>=3.5 and l<=20.5):
                    num=523
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=524
                if(l>=1.5 and l<3.5):
                    num=525
                if(l>=3.5 and l<=20.5):
                    num=526
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=527
                if(l>=1.5 and l<3.5):
                    num=528
                if(l>=3.5 and l<=20.5):
                    num=529
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=530
                if(l>=1.5 and l<3.5):
                    num=531
                if(l>=3.5 and l<=20.5):
                    num=532
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=533
                if(l>=1.5 and l<3.5):
                    num=534
                if(l>=3.5 and l<=20.5):
                    num=535
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=536
                if(l>=1.5 and l<3.5):
                    num=537
                if(l>=3.5 and l<=20.5):
                    num=538
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=539
                if(l>=1.5 and l<3.5):
                    num=540
                if(l>=3.5 and l<=20.5):
                    num=541
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=542
            if(l>=1.5 and l<3.5):
                num=543
            if(l>=3.5 and l<=20.5):
                num=544



    if(open>=7 and open <9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=545
            if(h>=1.5 and h<3.5):
                num=546
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=547
                if(l>=1.5 and l<3.5):
                    num=548
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=549
                if(l>=1.5 and l<3.5):
                    num=550
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=551
                if(l>=1.5 and l<3.5):
                    num=552
                if(l>=3.5 and l<20.5):
                    num=553
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=554
                if(l>=1.5 and l<3.5):
                    num=555
                if(l>=3.5 and l<20.5):
                    num=556
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=557
                if(l>=1.5 and l<3.5):
                    num=558
                if(l>=3.5 and l<=20.5):
                    num=559
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=560
                if(l>=1.5 and l<3.5):
                    num=561
                if(l>=3.5 and l<=20.5):
                    num=562
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=563
                if(l>=1.5 and l<3.5):
                    num=564
                if(l>=3.5 and l<=20.5):
                    num=565
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=566
                if(l>=1.5 and l<3.5):
                    num=567
                if(l>=3.5 and l<=20.5):
                    num=568
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=569
                if(l>=1.5 and l<3.5):
                    num=570
                if(l>=3.5 and l<=20.5):
                    num=571
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=572
                if(l>=1.5 and l<3.5):
                    num=573
                if(l>=3.5 and l<=20.5):
                    num=574
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=575
                if(l>=1.5 and l<3.5):
                    num=576
                if(l>=3.5 and l<=20.5):
                    num=577
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=578
                if(l>=1.5 and l<3.5):
                    num=579
                if(l>=3.5 and l<=20.5):
                    num=580
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=581
                if(l>=1.5 and l<3.5):
                    num=582
                if(l>=3.5 and l<=20.5):
                    num=583
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=584
                if(l>=1.5 and l<3.5):
                    num=585
                if(l>=3.5 and l<=20.5):
                    num=586
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=587
                if(l>=1.5 and l<3.5):
                    num=588
                if(l>=3.5 and l<=20.5):
                    num=589
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=590
                if(l>=1.5 and l<3.5):
                    num=591
                if(l>=3.5 and l<=20.5):
                    num=592
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=593
                if(l>=1.5 and l<3.5):
                    num=594
                if(l>=3.5 and l<=20.5):
                    num=595
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=596
                if(l>=1.5 and l<3.5):
                    num=597
                if(l>=3.5 and l<=20.5):
                    num=598
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=599
                if(l>=1.5 and l<3.5):
                    num=600
                if(l>=3.5 and l<=20.5):
                    num=601
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=602
                if(l>=1.5 and l<3.5):
                    num=603
                if(l>=3.5 and l<=20.5):
                    num=604
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=605
            if(l>=1.5 and l<3.5):
                num=606
            if(l>=3.5 and l<=20.5):
                num=607



    if(open>=9.94 and open <=10.6):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            num=608
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=609
            if(l>=1.5 and l<3.5):
                num=610
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=611
            if(l>=1.5 and l<3.5):
                num=612
            if(l>=3.5 and l<20.5):
                num=613
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=614
            if(l>=1.5 and l<3.5):
                num=615
            if(l>=3.5 and l<=20.5):
                num=616
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=617
            if(l>=1.5 and l<3.5):
                num=618
            if(l>=3.5 and l<=20.5):
                num=619
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=620
            if(l>=1.5 and l<3.5):
                num=621
            if(l>=3.5 and l<=20.5):
                num=622
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=623
            if(l>=1.5 and l<3.5):
                num=624
            if(l>=3.5 and l<=20.5):
                num=625
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=626
            if(l>=1.5 and l<3.5):
                num=627
            if(l>=3.5 and l<=20.5):
                num=628
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=629
            if(l>=1.5 and l<3.5):
                num=630
            if(l>=3.5 and l<=20.5):
                num=631
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=632
            if(l>=1.5 and l<3.5):
                num=633
            if(l>=3.5 and l<=20.5):
                num=634
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=635
            if(l>=1.5 and l<3.5):
                num=636
            if(l>=3.5 and l<=20.5):
                num=637
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=638
            if(l>=1.5 and l<3.5):
                num=639
            if(l>=3.5 and l<=20.5):
                num=640
    return num













#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print('今天是'+d)

#获取最新日期表
date_new_list=[]
sql = "SELECT date FROM rqb order by id "
cursor.execute(sql)
for c in cursor.fetchall():
    date_new_list.append(c[0]) 


#获取报告期数据
rq_list=['2015-03-31','2015-06-30','2015-09-30','2015-12-31',
         '2016-03-31','2016-06-30','2016-09-30','2016-12-31',
         '2017-03-31','2017-06-30','2017-09-30','2017-12-31',
         '2018-03-31','2018-06-30','2018-09-30','2018-12-31',
         '2019-03-31','2019-06-30','2019-09-30','2019-12-31',
         '2020-03-31','2020-06-30','2020-09-30','2020-12-31']
rq_int_list=[20150331,20150630,20150930,20151231,
         20160331,20160630,20160930,20161231,
         20170331,20170630,20170930,20171231,
         20180331,20180630,20180930,20181231,
         20190331,20190630,20190930,20191231,
         20200331,20200630,20200930,20201231]





#获取需要除权的表

dm_list=[]
tjts=256
dm_update_list=[]
dm=''
open=0
high=0
low=0
close=0
qyt_close_list=[]
dt_open_list=[]
dt_high_list=[]
dt_low_list=[]
dt_close_list=[]
open_list=[]
high_list=[]
low_list=[]
close_list=[]



sql = "SELECT dm  FROM kxfzb where tag1='备选'  order by id "
cursor.execute(sql)
for a in cursor.fetchall():
    dm_list.append(a[0])
print(len(dm_list))
    


for k in range(0,len(dm_list)) :


    dm='tb'+dm_list[k]

    print(dm)

    qyt_close_list=[]
    dt_open_list=[]
    dt_high_list=[]
    dt_low_list=[]
    dt_close_list=[]
    date_dt_list=[]
    open_list=[]
    high_list=[]
    low_list=[]
    close_list=[]



    sql = "select t.close from (select id ,close from %s order by id desc limit %d) t order by t.id limit %d"
    data = (dm,tjts+1,tjts)
    cursor.execute(sql % data)
    for a in cursor.fetchall():
        qyt_close_list.append(a[0]) 

    sql = "select t.open,t.high,t.low,t.close,t.date from (select id,date,open,high,low,close from %s order by id desc limit %d) t order by t.id "
    data = (dm,tjts)
    cursor.execute(sql % data)
    for a in cursor.fetchall():
        dt_open_list.append(a[0])
        dt_high_list.append(a[1])
        dt_low_list.append(a[2])
        dt_close_list.append(a[3])
        date_dt_list.append(a[4])

    for i in range(tjts):
        open_list.append((dt_open_list[i]-qyt_close_list[i])*100/qyt_close_list[i])
        high_list.append((dt_high_list[i]-qyt_close_list[i])*100/qyt_close_list[i])
        low_list.append((dt_low_list[i]-qyt_close_list[i])*100/qyt_close_list[i])
        close_list.append((dt_close_list[i]-qyt_close_list[i])*100/qyt_close_list[i])


    for i in range(tjts):
        open=open_list[i]
        high=high_list[i]
        low=low_list[i]
        close=close_list[i]
        num=0
        num=bm(open,high,low,close)

        if(num==0):
            print(dm,date_dt_list[i],open,high,low,close)
            dm_update_list.append(dm[2:])


dm_cq_list=[]
dm_cq_list=dm_update_list

#dm_cq_list=['603909']
print(dm_cq_list)        
print("共需要更新",len(dm_cq_list),'张表')



#清空除权表
print("开始清空除权表数据....................")
for v in range(len(dm_cq_list)):
    sql_1 = "truncate table %s"
    data = ('TB'+dm_cq_list[v])
    try:
        cursor.execute(sql_1 % data)  
    except Exception as e:
        connect.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        connect.commit()  # 事务提交
        print('TB'+dm_cq_list[v],'数据清空成功')


#3.向新增加的表中插入数据
print("开始向除权表中插入数据...................................................")
dm_insert_sh_list=[]
for s in range(len(dm_cq_list)):
    if dm_cq_list[s].startswith('6'):
        t=dm_cq_list[s]+'.XSHG'
    else:
        t=dm_cq_list[s]+'.XSHE'        
    dm_insert_sh_list.append(t)
for q in range(0, len(dm_cq_list)):
    #获取收盘价
    insert_df=jq.get_price(dm_insert_sh_list[q],  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
    insert_df.reset_index(inplace=True,drop=False)
    insert_list=insert_df.values.tolist()
    for s in range(len(insert_list)):
        sql = "INSERT INTO %s (date,open,close,high,low,cjl) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )" 
        date = datetime.date(datetime.fromtimestamp(insert_list[s][0].timestamp()))       
        data = ('TB'+dm_cq_list[q],date,insert_list[s][1],insert_list[s][2],insert_list[s][3],insert_list[s][4],insert_list[s][5])
        cursor.execute(sql % data)
        connect.commit()
    print('TB'+dm_insert_sh_list[q][:6],'收盘价数据获取完成')
    
    #获取市值
    for u in range(len(date_new_list)):
        df_volandincome = jq.get_fundamentals(jq.query(
        jq.valuation.code, 
        jq.valuation.circulating_market_cap, 
        jq.valuation.pe_ratio, 
        jq.income.total_operating_revenue,
        jq.income.np_parent_company_owners 
        ).filter(
        jq.valuation.code == dm_insert_sh_list[q]
        ), date=date_new_list[u])
        volandincome_list=df_volandincome.values.tolist() 
        sql = "update %s set dm='%s' , ltsz=%.2f ,  syl=%.2f  ,  ys=%.2f  ,  jlr=%.2f  where date='%s'"
        try:
            data=('TB'+volandincome_list[0][0][:6],volandincome_list[0][0][:6],volandincome_list[0][1],volandincome_list[0][2],volandincome_list[0][3],volandincome_list[0][4],date_new_list[u])
            cursor.execute(sql % data)
        except Exception as e:
            connect.rollback()  # 事务回滚
            continue
        else:
            connect.commit()  # 事务提交
    print('TB'+dm_insert_sh_list[q][:6],'市值数据获取完成')
    
    
    #获取资金流向
    zjl_df=jq.get_money_flow(dm_insert_sh_list[q], start_date='2015-01-01', end_date=d, fields=['date','change_pct','net_amount_xl','net_amount_l','net_amount_m','net_amount_s'])
    zjl_list=zjl_df.values.tolist()
    for p in range(0,len(zjl_list)):
        sql = "update %s set zdf=%.2f , cdd=%.2f ,  dd=%.2f  ,  zd=%.2f  ,  xd=%.2f  where date='%s'"
        data=('TB'+dm_cq_list[q],zjl_list[p][1],zjl_list[p][2],zjl_list[p][3],zjl_list[p][4],zjl_list[p][5],datetime.date(datetime.fromtimestamp(zjl_list[p][0].timestamp())))
        cursor.execute(sql % data)
        connect.commit()  # 事务提交
    print('TB'+dm_insert_sh_list[q][:6],'资金流数据获取完成')
    
    
    
    #获取流通股东   
    date_int_list=[]
    sql2 = "SELECT date FROM rqb order by id "
    cursor.execute(sql2)
    for row in cursor.fetchall():
        p=int(row[0].replace('-','').replace('\'', ''))        
        date_int_list.append(p) 
    for x in range(len(rq_list)): 
        ltgd_df=finance.run_query(jq.query(
            
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code,
        finance.STK_SHAREHOLDER_FLOATING_TOP10.shareholder_rank,
        finance.STK_SHAREHOLDER_FLOATING_TOP10.share_ratio
        ).filter(
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code==dm_insert_sh_list[q],
        finance.STK_SHAREHOLDER_FLOATING_TOP10.end_date==rq_list[x]  
        ))
        for z in range(len(date_new_list)):
            if date_int_list[z]>rq_int_list[x] and date_int_list[z]<=rq_int_list[x+1]:
                sql = "  update %s set lt_1=%.2f , lt_2=%.2f  ,lt_3=%.2f  ,lt_4=%.2f  ,lt_5=%.2f  ,lt_6=%.2f  ,lt_7=%.2f  ,lt_8=%.2f  ,lt_9=%.2f  ,lt_10=%.2f    where date='%s'"
                try:
                    data=('TB'+dm_cq_list[q],ltgd_df.iloc[0]['share_ratio'],ltgd_df.iloc[1]['share_ratio'],ltgd_df.iloc[2]['share_ratio'],ltgd_df.iloc[3]['share_ratio'],ltgd_df.iloc[4]['share_ratio'],ltgd_df.iloc[5]['share_ratio'],ltgd_df.iloc[6]['share_ratio'],ltgd_df.iloc[7]['share_ratio'],ltgd_df.iloc[8]['share_ratio'],ltgd_df.iloc[9]['share_ratio'],date_new_list[z])
                    cursor.execute(sql % data)
                except Exception as e:
                    connect.rollback()  # 事务回滚
                else:
                    connect.commit()  # 事务提交
    print('TB'+dm_insert_sh_list[q][:6],'流通股东数据获取完成')  
print('除权所有数据插入完毕....................................')   
print(d,'除权完成***********************************************')  




# 关闭连接
cursor.close()
connect.close()