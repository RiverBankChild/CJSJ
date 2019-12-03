def js(open,high,low,close):   
    h=0
    l=0
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



#openzl=[[-10.51,-9.96],[-9.96,-7],[-7,-3],[-3,-1],[-1,1],[1,3],[3,7],[7,9.96],[9.96,10.51]]
#closezl=[[-10.51,-9.96],[-9.96,-7],[-7,-4],[-4,-2],[-2,-1],[-1,0],[0,1],[1,2],[2,4],[4,7],[7,9.96],[9.96,10.51]]
#normzl=[[0,0.05],[0.05,1.5],[1.5,3.5],[3.5,6.5],[6.5,20.5]]
def bm(open,high,low,close):
    num=0
    if(open>=-10.51 and open <=-9.96):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            num=1
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=2
            if(h>0.05 and h<1.5):
                num=3
            if(h>=1.5 and h<3.5):
                num=4
            if(h>=3.5 and h<6.5):
                num=5
            if(h>=6.5 and h<=20.5):
                num=6
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=7
            if(h>0.05 and h<1.5):
                num=8
            if(h>=1.5 and h<3.5):
                num=9
            if(h>=3.5 and h<6.5):
                num=10
            if(h>=6.5 and h<=20.5):
                num=11
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=12
            if(h>0.05 and h<1.5):
                num=13
            if(h>=1.5 and h<3.5):
                num=14
            if(h>=3.5 and h<6.5):
                num=15
            if(h>=6.5 and h<=20.5):
                num=16
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=17
            if(h>0.05 and h<1.5):
                num=18
            if(h>=1.5 and h<3.5):
                num=19
            if(h>=3.5 and h<6.5):
                num=20
            if(h>=6.5 and h<=20.5):
                num=21
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=22
            if(h>0.05 and h<1.5):
                num=23
            if(h>=1.5 and h<3.5):
                num=24
            if(h>=3.5 and h<6.5):
                num=25
            if(h>=6.5 and h<=20.5):
                num=26
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=27
            if(h>0.05 and h<1.5):
                num=28
            if(h>=1.5 and h<3.5):
                num=29
            if(h>=3.5 and h<6.5):
                num=30
            if(h>=6.5 and h<=20.5):
                num=31
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=32
            if(h>0.05 and h<1.5):
                num=33
            if(h>=1.5 and h<3.5):
                num=34
            if(h>=3.5 and h<6.5):
                num=35
            if(h>=6.5 and h<=20.5):
                num=36
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=37
            if(h>0.05 and h<1.5):
                num=38
            if(h>=1.5 and h<3.5):
                num=39
            if(h>=3.5 and h<6.5):
                num=40
            if(h>=6.5 and h<=20.5):
                num=41
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=42
            if(h>0.05 and h<1.5):
                num=43
            if(h>=1.5 and h<3.5):
                num=44
            if(h>=3.5 and h<6.5):
                num=45
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=46
            if(h>0.05 and h<1.5):
                num=47
            if(h>=1.5 and h<3.5):
                num=48
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=49





    if(open>-9.96 and open <-7):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=50
            if(h>0.05 and h<1.5):
                num=51
            if(h>=1.5 and h<3.5):
                num=52
            if(h>=3.5 and h<6.5):
                num=53
            if(h>=6.5 and h<=20.5):
                num=54
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=55
                if(l>0.05 and l<1.5):
                    num=56
                if(l>=1.5 and l<3.5):
                    num=57
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=58
                if(l>0.05 and l<1.5):
                    num=59
                if(l>=1.5 and l<3.5):
                    num=60
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=61
                if(l>0.05 and l<1.5):
                    num=62
                if(l>=1.5 and l<3.5):
                    num=63
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=64
                if(l>0.05 and l<1.5):
                    num=65
                if(l>=1.5 and l<3.5):
                    num=66
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=67
                if(l>0.05 and l<1.5):
                    num=68
                if(l>=1.5 and l<3.5):
                    num=69
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=70
                if(l>0.05 and l<1.5):
                    num=71
                if(l>=1.5 and l<3.5):
                    num=72
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=73
                if(l>0.05 and l<1.5):
                    num=74
                if(l>=1.5 and l<3.5):
                    num=75
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=76
                if(l>0.05 and l<1.5):
                    num=77
                if(l>=1.5 and l<3.5):
                    num=78
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=79
                if(l>0.05 and l<1.5):
                    num=80
                if(l>=1.5 and l<3.5):
                    num=81
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=82
                if(l>0.05 and l<1.5):
                    num=83
                if(l>=1.5 and l<3.5):
                    num=84
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=85
                if(l>0.05 and l<1.5):
                    num=86
                if(l>=1.5 and l<3.5):
                    num=87
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=88
                if(l>0.05 and l<1.5):
                    num=89
                if(l>=1.5 and l<3.5):
                    num=90
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=91
                if(l>0.05 and l<1.5):
                    num=92
                if(l>=1.5 and l<3.5):
                    num=93
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=94
                if(l>0.05 and l<1.5):
                    num=95
                if(l>=1.5 and l<3.5):
                    num=96
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=97
                if(l>0.05 and l<1.5):
                    num=98
                if(l>=1.5 and l<3.5):
                    num=99
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=100
                if(l>0.05 and l<1.5):
                    num=101
                if(l>=1.5 and l<3.5):
                    num=102
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=103
                if(l>0.05 and l<1.5):
                    num=104
                if(l>=1.5 and l<3.5):
                    num=105
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=106
                if(l>0.05 and l<1.5):
                    num=107
                if(l>=1.5 and l<3.5):
                    num=108
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=109
                if(l>0.05 and l<1.5):
                    num=110
                if(l>=1.5 and l<3.5):
                    num=111
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=112
                if(l>0.05 and l<1.5):
                    num=113
                if(l>=1.5 and l<3.5):
                    num=114
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=115
                if(l>0.05 and l<1.5):
                    num=116
                if(l>=1.5 and l<3.5):
                    num=117
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=118
                if(l>0.05 and l<1.5):
                    num=119
                if(l>=1.5 and l<3.5):
                    num=120
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=121
                if(l>0.05 and l<1.5):
                    num=122
                if(l>=1.5 and l<3.5):
                    num=123
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=124
                if(l>0.05 and l<1.5):
                    num=125
                if(l>=1.5 and l<3.5):
                    num=126
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=127
                if(l>0.05 and l<1.5):
                    num=128
                if(l>=1.5 and l<3.5):
                    num=129
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=130
                if(l>0.05 and l<1.5):
                    num=131
                if(l>=1.5 and l<3.5):
                    num=132
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=133
                if(l>0.05 and l<1.5):
                    num=134
                if(l>=1.5 and l<3.5):
                    num=135
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=136
                if(l>0.05 and l<1.5):
                    num=137
                if(l>=1.5 and l<3.5):
                    num=138
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=139
                if(l>0.05 and l<1.5):
                    num=140
                if(l>=1.5 and l<3.5):
                    num=141
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=142
                if(l>0.05 and l<1.5):
                    num=143
                if(l>=1.5 and l<3.5):
                    num=144
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=145
                if(l>0.05 and l<1.5):
                    num=146
                if(l>=1.5 and l<3.5):
                    num=147
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=148
                if(l>0.05 and l<1.5):
                    num=149
                if(l>=1.5 and l<3.5):
                    num=150
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=151
                if(l>0.05 and l<1.5):
                    num=152
                if(l>=1.5 and l<3.5):
                    num=153
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=154
                if(l>0.05 and l<1.5):
                    num=155
                if(l>=1.5 and l<3.5):
                    num=156
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=157
                if(l>0.05 and l<1.5):
                    num=158
                if(l>=1.5 and l<3.5):
                    num=159
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=160
                if(l>0.05 and l<1.5):
                    num=161
                if(l>=1.5 and l<3.5):
                    num=162
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=163
                if(l>0.05 and l<1.5):
                    num=164
                if(l>=1.5 and l<3.5):
                    num=165
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=166
                if(l>0.05 and l<1.5):
                    num=167
                if(l>=1.5 and l<3.5):
                    num=168
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=169
                if(l>0.05 and l<1.5):
                    num=170
                if(l>=1.5 and l<3.5):
                    num=171
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=172
                if(l>0.05 and l<1.5):
                    num=173
                if(l>=1.5 and l<3.5):
                    num=174
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=175
                if(l>0.05 and l<1.5):
                    num=176
                if(l>=1.5 and l<3.5):
                    num=177
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=178
                if(l>0.05 and l<1.5):
                    num=179
                if(l>=1.5 and l<3.5):
                    num=180
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1545
                if(l>0.05 and l<1.5):
                    num=1546
                if(l>=1.5 and l<3.5):
                    num=1547
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=181
                if(l>0.05 and l<1.5):
                    num=182
                if(l>=1.5 and l<3.5):
                    num=183
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=184
                if(l>0.05 and l<1.5):
                    num=185
                if(l>=1.5 and l<3.5):
                    num=186
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=187
                if(l>0.05 and l<1.5):
                    num=188
                if(l>=1.5 and l<3.5):
                    num=189
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=190
                if(l>0.05 and l<1.5):
                    num=191
                if(l>=1.5 and l<3.5):
                    num=193



    if(open>=-7 and open <-3):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=194
            if(h>0.05 and h<1.5):
                num=195            
            if(h>=1.5 and h<3.5):
                num=196
            if(h>=3.5 and h<6.5):
                num=197
            if(h>=6.5 and h<=20.5):
                num=198
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=199
                if(l>0.05 and l<1.5):
                    num=200
                if(l>=1.5 and l<3.5):
                    num=201
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=202
                if(l>0.05 and l<1.5):
                    num=203
                if(l>=1.5 and l<3.5):
                    num=204
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=205
                if(l>0.05 and l<1.5):
                    num=206
                if(l>=1.5 and l<3.5):
                    num=207
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=208
                if(l>0.05 and l<1.5):
                    num=209
                if(l>=1.5 and l<3.5):
                    num=210
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=211
                if(l>0.05 and l<1.5):
                    num=212
                if(l>=1.5 and l<3.5):
                    num=213
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=214
                if(l>0.05 and l<1.5):
                    num=215
                if(l>=1.5 and l<3.5):
                    num=216
                if(l>=3.5 and l<6.5):
                    num=217
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=218
                if(l>0.05 and l<1.5):
                    num=219
                if(l>=1.5 and l<3.5):
                    num=220
                if(l>=3.5 and l<6.5):
                    num=221
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=222
                if(l>0.05 and l<1.5):
                    num=223
                if(l>=1.5 and l<3.5):
                    num=224
                if(l>=3.5 and l<6.5):
                    num=225
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=226
                if(l>0.05 and l<1.5):
                    num=227
                if(l>=1.5 and l<3.5):
                    num=228
                if(l>=3.5 and l<6.5):
                    num=229
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=230
                if(l>0.05 and l<1.5):
                    num=231
                if(l>=1.5 and l<3.5):
                    num=232
                if(l>=3.5 and l<6.5):
                    num=233
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=234
                if(l>0.05 and l<1.5):
                    num=235
                if(l>=1.5 and l<3.5):
                    num=236
                if(l>=3.5 and l<6.5):
                    num=237
                if(l>=6.5 and l<=20.5):
                    num=238
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=239
                if(l>0.05 and l<1.5):
                    num=240
                if(l>=1.5 and l<3.5):
                    num=241
                if(l>=3.5 and l<6.5):
                    num=242
                if(l>=6.5 and l<=20.5):
                    num=243
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=244
                if(l>0.05 and l<1.5):
                    num=245
                if(l>=1.5 and l<3.5):
                    num=246
                if(l>=3.5 and l<6.5):
                    num=247
                if(l>=6.5 and l<=20.5):
                    num=248
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=249
                if(l>0.05 and l<1.5):
                    num=250
                if(l>=1.5 and l<3.5):
                    num=251
                if(l>=3.5 and l<6.5):
                    num=252
                if(l>=6.5 and l<=20.5):
                    num=253
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=254
                if(l>0.05 and l<1.5):
                    num=255
                if(l>=1.5 and l<3.5):
                    num=256
                if(l>=3.5 and l<6.5):
                    num=257
                if(l>=6.5 and l<=20.5):
                    num=258
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=259
                if(l>0.05 and l<1.5):
                    num=260
                if(l>=1.5 and l<3.5):
                    num=261
                if(l>=3.5 and l<6.5):
                    num=262
                if(l>=6.5 and l<=20.5):
                    num=263
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=264
                if(l>0.05 and l<1.5):
                    num=265
                if(l>=1.5 and l<3.5):
                    num=266
                if(l>=3.5 and l<6.5):
                    num=267
                if(l>=6.5 and l<=20.5):
                    num=268
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=269
                if(l>0.05 and l<1.5):
                    num=270
                if(l>=1.5 and l<3.5):
                    num=271
                if(l>=3.5 and l<6.5):
                    num=272
                if(l>=6.5 and l<=20.5):
                    num=273
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=274
                if(l>0.05 and l<1.5):
                    num=275
                if(l>=1.5 and l<3.5):
                    num=276
                if(l>=3.5 and l<6.5):
                    num=277
                if(l>=6.5 and l<=20.5):
                    num=278
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=279
                if(l>0.05 and l<1.5):
                    num=280
                if(l>=1.5 and l<3.5):
                    num=281
                if(l>=3.5 and l<6.5):
                    num=282
                if(l>=6.5 and l<=20.5):
                    num=283
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=284
                if(l>0.05 and l<1.5):
                    num=285
                if(l>=1.5 and l<3.5):
                    num=286
                if(l>=3.5 and l<6.5):
                    num=287
                if(l>=6.5 and l<=20.5):
                    num=288
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=289
                if(l>0.05 and l<1.5):
                    num=290
                if(l>=1.5 and l<3.5):
                    num=291
                if(l>=3.5 and l<6.5):
                    num=292
                if(l>=6.5 and l<=20.5):
                    num=293
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=294
                if(l>0.05 and l<1.5):
                    num=295
                if(l>=1.5 and l<3.5):
                    num=296
                if(l>=3.5 and l<6.5):
                    num=297
                if(l>=6.5 and l<=20.5):
                    num=298
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=299
                if(l>0.05 and l<1.5):
                    num=300
                if(l>=1.5 and l<3.5):
                    num=301
                if(l>=3.5 and l<6.5):
                    num=302
                if(l>=6.5 and l<=20.5):
                    num=303
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=304
                if(l>0.05 and l<1.5):
                    num=305
                if(l>=1.5 and l<3.5):
                    num=306
                if(l>=3.5 and l<6.5):
                    num=307
                if(l>=6.5 and l<=20.5):
                    num=308
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=309
                if(l>0.05 and l<1.5):
                    num=310
                if(l>=1.5 and l<3.5):
                    num=311
                if(l>=3.5 and l<6.5):
                    num=312
                if(l>=6.5 and l<=20.5):
                    num=313
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=314
                if(l>0.05 and l<1.5):
                    num=315
                if(l>=1.5 and l<3.5):
                    num=316
                if(l>=3.5 and l<6.5):
                    num=317
                if(l>=6.5 and l<=20.5):
                    num=318
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=319
                if(l>0.05 and l<1.5):
                    num=320
                if(l>=1.5 and l<3.5):
                    num=321
                if(l>=3.5 and l<6.5):
                    num=322
                if(l>=6.5 and l<=20.5):
                    num=323
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=324
                if(l>0.05 and l<1.5):
                    num=325
                if(l>=1.5 and l<3.5):
                    num=326
                if(l>=3.5 and l<6.5):
                    num=327
                if(l>=6.5 and l<=20.5):
                    num=328
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=329
                if(l>0.05 and l<1.5):
                    num=330
                if(l>=1.5 and l<3.5):
                    num=331
                if(l>=3.5 and l<6.5):
                    num=332
                if(l>=6.5 and l<=20.5):
                    num=333
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=334
                if(l>0.05 and l<1.5):
                    num=335
                if(l>=1.5 and l<3.5):
                    num=336
                if(l>=3.5 and l<6.5):
                    num=337
                if(l>=6.5 and l<=20.5):
                    num=338
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=339
                if(l>0.05 and l<1.5):
                    num=340
                if(l>=1.5 and l<3.5):
                    num=341
                if(l>=3.5 and l<6.5):
                    num=342
                if(l>=6.5 and l<=20.5):
                    num=343
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=344
                if(l>0.05 and l<1.5):
                    num=345
                if(l>=1.5 and l<3.5):
                    num=346
                if(l>=3.5 and l<6.5):
                    num=347
                if(l>=6.5 and l<=20.5):
                    num=348
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=349
                if(l>0.05 and l<1.5):
                    num=350
                if(l>=1.5 and l<3.5):
                    num=351
                if(l>=3.5 and l<6.5):
                    num=352
                if(l>=6.5 and l<=20.5):
                    num=353
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=354
                if(l>0.05 and l<1.5):
                    num=355
                if(l>=1.5 and l<3.5):
                    num=356
                if(l>=3.5 and l<6.5):
                    num=357
                if(l>=6.5 and l<=20.5):
                    num=358
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=359
                if(l>0.05 and l<1.5):
                    num=360
                if(l>=1.5 and l<3.5):
                    num=361
                if(l>=3.5 and l<6.5):
                    num=362
                if(l>=6.5 and l<=20.5):
                    num=363
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=364
                if(l>0.05 and l<1.5):
                    num=365
                if(l>=1.5 and l<3.5):
                    num=366
                if(l>=3.5 and l<6.5):
                    num=367
                if(l>=6.5 and l<=20.5):
                    num=368
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=369
                if(l>0.05 and l<1.5):
                    num=370
                if(l>=1.5 and l<3.5):
                    num=371
                if(l>=3.5 and l<6.5):
                    num=225
                if(l>=6.5 and l<=20.5):
                    num=372
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=373
                if(l>0.05 and l<1.5):
                    num=374
                if(l>=1.5 and l<3.5):
                    num=375
                if(l>=3.5 and l<6.5):
                    num=376
                if(l>=6.5 and l<=20.5):
                    num=377
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=378
                if(l>0.05 and l<1.5):
                    num=379
                if(l>=1.5 and l<3.5):
                    num=380
                if(l>=3.5 and l<6.5):
                    num=381
                if(l>=6.5 and l<=20.5):
                    num=382
        if(close>=4 and close<7):          
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=383
                if(l>0.05 and l<1.5):
                    num=384
                if(l>=1.5 and l<3.5):
                    num=385
                if(l>=3.5 and l<6.5):
                    num=386
                if(l>=6.5 and l<=20.5):
                    num=387
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=388
                if(l>0.05 and l<1.5):
                    num=389
                if(l>=1.5 and l<3.5):
                    num=390
                if(l>=3.5 and l<6.5):
                    num=391
                if(l>=6.5 and l<=20.5):
                    num=392
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=393
                if(l>0.05 and l<1.5):
                    num=394
                if(l>=1.5 and l<3.5):
                    num=395
                if(l>=3.5 and l<6.5):
                    num=396
                if(l>=6.5 and l<=20.5):
                    num=397
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=398
                if(l>0.05 and l<1.5):
                    num=399
                if(l>=1.5 and l<3.5):
                    num=400
                if(l>=3.5 and l<6.5):
                    num=401
                if(l>=6.5 and l<=20.5):
                    num=402
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=403
                if(l>0.05 and l<1.5):
                    num=404
                if(l>=1.5 and l<3.5):
                    num=405
                if(l>=3.5 and l<6.5):
                    num=406
                if(l>=6.5 and l<=20.5):
                    num=407
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=408
                if(l>0.05 and l<1.5):
                    num=409
                if(l>=1.5 and l<3.5):
                    num=410
                if(l>=3.5 and l<6.5):
                    num=411
                if(l>=6.5 and l<=20.5):
                    num=412
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=413
                if(l>0.05 and l<1.5):
                    num=414
                if(l>=1.5 and l<3.5):
                    num=415
                if(l>=3.5 and l<6.5):
                    num=416
                if(l>=6.5 and l<=20.5):
                    num=417
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=418
            if(l>0.05 and l<1.5):
                num=419
            if(l>=1.5 and l<3.5):
                num=420
            if(l>=3.5 and l<6.5):
                num=421
            if(l>=6.5 and l<=20.5):
                num=422




    if(open>=-3 and open <-1):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=423
            if(h>0.05 and h<1.5):
                num=424
            if(h>=1.5 and h<3.5):
                num=425
            if(h>=3.5 and h<6.5):
                num=426
            if(h>=6.5 and h<=20.5):
                num=427
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=428
                if(l>0.05 and l<1.5):
                    num=429
                if(l>=1.5 and l<3.5):
                    num=430
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=431
                if(l>0.05 and l<1.5):
                    num=432
                if(l>=1.5 and l<3.5):
                    num=433
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=434
                if(l>0.05 and l<1.5):
                    num=435
                if(l>=1.5 and l<3.5):
                    num=436
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=437
                if(l>0.05 and l<1.5):
                    num=438
                if(l>=1.5 and l<3.5):
                    num=439
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=440
                if(l>0.05 and l<1.5):
                    num=441
                if(l>=1.5 and l<3.5):
                    num=442
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=443
                if(l>0.05 and l<1.5):
                    num=444
                if(l>=1.5 and l<3.5):
                    num=445
                if(l>=3.5 and l<6.5):
                    num=446
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=447
                if(l>0.05 and l<1.5):
                    num=448
                if(l>=1.5 and l<3.5):
                    num=449
                if(l>=3.5 and l<6.5):
                    num=450
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=451
                if(l>0.05 and l<1.5):
                    num=452
                if(l>=1.5 and l<3.5):
                    num=453
                if(l>=3.5 and l<6.5):
                    num=454
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=455
                if(l>0.05 and l<1.5):
                    num=456
                if(l>=1.5 and l<3.5):
                    num=457
                if(l>=3.5 and l<6.5):
                    num=458
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=459
                if(l>0.05 and l<1.5):
                    num=460
                if(l>=1.5 and l<3.5):
                    num=461
                if(l>=3.5 and l<6.5):
                    num=462
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=463
                if(l>0.05 and l<1.5):
                    num=464
                if(l>=1.5 and l<3.5):
                    num=465
                if(l>=3.5 and l<6.5):
                    num=466
                if(l>=6.5 and l<=20.5):
                    num=467
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=468
                if(l>0.05 and l<1.5):
                    num=469
                if(l>=1.5 and l<3.5):
                    num=470
                if(l>=3.5 and l<6.5):
                    num=471
                if(l>=6.5 and l<=20.5):
                    num=472
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=473
                if(l>0.05 and l<1.5):
                    num=474
                if(l>=1.5 and l<3.5):
                    num=475
                if(l>=3.5 and l<6.5):
                    num=476
                if(l>=6.5 and l<=20.5):
                    num=477
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=478
                if(l>0.05 and l<1.5):
                    num=479
                if(l>=1.5 and l<3.5):
                    num=480
                if(l>=3.5 and l<6.5):
                    num=481
                if(l>=6.5 and l<=20.5):
                    num=482
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=483
                if(l>0.05 and l<1.5):
                    num=484
                if(l>=1.5 and l<3.5):
                    num=485
                if(l>=3.5 and l<6.5):
                    num=486
                if(l>=6.5 and l<=20.5):
                    num=487
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=488
                if(l>0.05 and l<1.5):
                    num=489
                if(l>=1.5 and l<3.5):
                    num=490
                if(l>=3.5 and l<6.5):
                    num=491
                if(l>=6.5 and l<=20.5):
                    num=492
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=493
                if(l>0.05 and l<1.5):
                    num=494
                if(l>=1.5 and l<3.5):
                    num=495
                if(l>=3.5 and l<6.5):
                    num=496
                if(l>=6.5 and l<=20.5):
                    num=497
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=498
                if(l>0.05 and l<1.5):
                    num=499
                if(l>=1.5 and l<3.5):
                    num=500
                if(l>=3.5 and l<6.5):
                    num=501
                if(l>=6.5 and l<=20.5):
                    num=502
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=503
                if(l>0.05 and l<1.5):
                    num=504
                if(l>=1.5 and l<3.5):
                    num=505
                if(l>=3.5 and l<6.5):
                    num=506
                if(l>=6.5 and l<=20.5):
                    num=507
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=508
                if(l>0.05 and l<1.5):
                    num=509
                if(l>=1.5 and l<3.5):
                    num=510
                if(l>=3.5 and l<6.5):
                    num=511
                if(l>=6.5 and l<=20.5):
                    num=512
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=513
                if(l>0.05 and l<1.5):
                    num=514
                if(l>=1.5 and l<3.5):
                    num=515
                if(l>=3.5 and l<6.5):
                    num=516
                if(l>=6.5 and l<=20.5):
                    num=517
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=518
                if(l>0.05 and l<1.5):
                    num=519
                if(l>=1.5 and l<3.5):
                    num=520
                if(l>=3.5 and l<6.5):
                    num=521
                if(l>=6.5 and l<=20.5):
                    num=522
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=523
                if(l>0.05 and l<1.5):
                    num=524
                if(l>=1.5 and l<3.5):
                    num=525
                if(l>=3.5 and l<6.5):
                    num=526
                if(l>=6.5 and l<=20.5):
                    num=527
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=528
                if(l>0.05 and l<1.5):
                    num=529
                if(l>=1.5 and l<3.5):
                    num=530
                if(l>=3.5 and l<6.5):
                    num=531
                if(l>=6.5 and l<=20.5):
                    num=532
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=533
                if(l>0.05 and l<1.5):
                    num=534
                if(l>=1.5 and l<3.5):
                    num=535
                if(l>=3.5 and l<6.5):
                    num=536
                if(l>=6.5 and l<=20.5):
                    num=537
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=538
                if(l>0.05 and l<1.5):
                    num=539
                if(l>=1.5 and l<3.5):
                    num=540
                if(l>=3.5 and l<6.5):
                    num=541
                if(l>=6.5 and l<=20.5):
                    num=542
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=543
                if(l>0.05 and l<1.5):
                    num=544
                if(l>=1.5 and l<3.5):
                    num=545
                if(l>=3.5 and l<6.5):
                    num=546
                if(l>=6.5 and l<=20.5):
                    num=547
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=548
                if(l>0.05 and l<1.5):
                    num=549
                if(l>=1.5 and l<3.5):
                    num=550
                if(l>=3.5 and l<6.5):
                    num=551
                if(l>=6.5 and l<=20.5):
                    num=552
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=553
                if(l>0.05 and l<1.5):
                    num=554
                if(l>=1.5 and l<3.5):
                    num=555
                if(l>=3.5 and l<6.5):
                    num=556
                if(l>=6.5 and l<=20.5):
                    num=557
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=558
                if(l>0.05 and l<1.5):
                    num=559
                if(l>=1.5 and l<3.5):
                    num=560
                if(l>=3.5 and l<6.5):
                    num=561
                if(l>=6.5 and l<=20.5):
                    num=562
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=563
                if(l>0.05 and l<1.5):
                    num=564
                if(l>=1.5 and l<3.5):
                    num=565
                if(l>=3.5 and l<6.5):
                    num=566
                if(l>=6.5 and l<=20.5):
                    num=567
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=568
                if(l>0.05 and l<1.5):
                    num=569
                if(l>=1.5 and l<3.5):
                    num=570
                if(l>=3.5 and l<6.5):
                    num=571
                if(l>=6.5 and l<=20.5):
                    num=572
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=573
                if(l>0.05 and l<1.5):
                    num=574
                if(l>=1.5 and l<3.5):
                    num=575
                if(l>=3.5 and l<6.5):
                    num=576
                if(l>=6.5 and l<=20.5):
                    num=577
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=578
                if(l>0.05 and l<1.5):
                    num=579
                if(l>=1.5 and l<3.5):
                    num=580
                if(l>=3.5 and l<6.5):
                    num=581
                if(l>=6.5 and l<=20.5):
                    num=582
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=583
                if(l>0.05 and l<1.5):
                    num=584
                if(l>=1.5 and l<3.5):
                    num=585
                if(l>=3.5 and l<6.5):
                    num=586
                if(l>=6.5 and l<=20.5):
                    num=587
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=588
                if(l>0.05 and l<1.5):
                    num=589
                if(l>=1.5 and l<3.5):
                    num=590
                if(l>=3.5 and l<6.5):
                    num=591
                if(l>=6.5 and l<=20.5):
                    num=592
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=593
                if(l>0.05 and l<1.5):
                    num=594
                if(l>=1.5 and l<3.5):
                    num=595
                if(l>=3.5 and l<6.5):
                    num=596
                if(l>=6.5 and l<=20.5):
                    num=597
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=598
                if(l>0.05 and l<1.5):
                    num=599
                if(l>=1.5 and l<3.5):
                    num=600
                if(l>=3.5 and l<6.5):
                    num=601
                if(l>=6.5 and l<=20.5):
                    num=602
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=603
                if(l>0.05 and l<1.5):
                    num=604
                if(l>=1.5 and l<3.5):
                    num=605
                if(l>=3.5 and l<6.5):
                    num=606
                if(l>=6.5 and l<=20.5):
                    num=607
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=608
                if(l>0.05 and l<1.5):
                    num=609
                if(l>=1.5 and l<3.5):
                    num=610
                if(l>=3.5 and l<6.5):
                    num=611
                if(l>=6.5 and l<=20.5):
                    num=612
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=613
                if(l>0.05 and l<1.5):
                    num=614
                if(l>=1.5 and l<3.5):
                    num=615
                if(l>=3.5 and l<6.5):
                    num=616
                if(l>=6.5 and l<=20.5):
                    num=617
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=618
                if(l>0.05 and l<1.5):
                    num=619
                if(l>=1.5 and l<3.5):
                    num=620
                if(l>=3.5 and l<6.5):
                    num=621
                if(l>=6.5 and l<=20.5):
                    num=622
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=623
                if(l>0.05 and l<1.5):
                    num=624
                if(l>=1.5 and l<3.5):
                    num=625
                if(l>=3.5 and l<6.5):
                    num=626
                if(l>=6.5 and l<=20.5):
                    num=627
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=628
                if(l>0.05 and l<1.5):
                    num=629
                if(l>=1.5 and l<3.5):
                    num=630
                if(l>=3.5 and l<6.5):
                    num=631
                if(l>=6.5 and l<=20.5):
                    num=632
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=633
                if(l>0.05 and l<1.5):
                    num=634
                if(l>=1.5 and l<3.5):
                    num=635
                if(l>=3.5 and l<6.5):
                    num=636
                if(l>=6.5 and l<=20.5):
                    num=637
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=638
                if(l>0.05 and l<1.5):
                    num=639
                if(l>=1.5 and l<3.5):
                    num=640
                if(l>=3.5 and l<6.5):
                    num=641
                if(l>=6.5 and l<=20.5):
                    num=642
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=643
                if(l>0.05 and l<1.5):
                    num=644
                if(l>=1.5 and l<3.5):
                    num=645
                if(l>=3.5 and l<6.5):
                    num=646
                if(l>=6.5 and l<=20.5):
                    num=647
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=648
            if(l>0.05 and l<1.5):
                num=649
            if(l>=1.5 and l<3.5):
                num=650
            if(l>=3.5 and l<6.5):
                num=651
            if(l>=6.5 and l<=20.5):
                num=652



    if(open>=-1 and open <1):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=653
            if(h>0.05 and h<1.5):
                num=354
            if(h>=1.5 and h<3.5):
                num=655
            if(h>=3.5 and h<6.5):
                num=656
            if(h>=6.5 and h<=20.5):
                num=657
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=658
                if(l>0.05 and l<1.5):
                    num=659
                if(l>=1.5 and l<3.5):
                    num=660
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=661
                if(l>0.05 and l<1.5):
                    num=662
                if(l>=1.5 and l<3.5):
                    num=663
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=664
                if(l>0.05 and l<1.5):
                    num=665
                if(l>=1.5 and l<3.5):
                    num=666
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=667
                if(l>0.05 and l<1.5):
                    num=668
                if(l>=1.5 and l<3.5):
                    num=669
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=670
                if(l>0.05 and l<1.5):
                    num=671
                if(l>=1.5 and l<3.5):
                    num=672
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=673
                if(l>0.05 and l<1.5):
                    num=674
                if(l>=1.5 and l<3.5):
                    num=675
                if(l>=3.5 and l<6.5):
                    num=676
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=677
                if(l>0.05 and l<1.5):
                    num=678
                if(l>=1.5 and l<3.5):
                    num=679
                if(l>=3.5 and l<6.5):
                    num=680
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=681
                if(l>0.05 and l<1.5):
                    num=682
                if(l>=1.5 and l<3.5):
                    num=683
                if(l>=3.5 and l<6.5):
                    num=684
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=685
                if(l>0.05 and l<1.5):
                    num=686
                if(l>=1.5 and l<3.5):
                    num=687
                if(l>=3.5 and l<6.5):
                    num=688
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=689
                if(l>0.05 and l<1.5):
                    num=690
                if(l>=1.5 and l<3.5):
                    num=691
                if(l>=3.5 and l<6.5):
                    num=692
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=693
                if(l>0.05 and l<1.5):
                    num=694
                if(l>=1.5 and l<3.5):
                    num=695
                if(l>=3.5 and l<6.5):
                    num=696
                if(l>=6.5 and l<=20.5):
                    num=697
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=698
                if(l>0.05 and l<1.5):
                    num=699
                if(l>=1.5 and l<3.5):
                    num=700
                if(l>=3.5 and l<6.5):
                    num=701
                if(l>=6.5 and l<=20.5):
                    num=702
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=703
                if(l>0.05 and l<1.5):
                    num=704
                if(l>=1.5 and l<3.5):
                    num=705
                if(l>=3.5 and l<6.5):
                    num=706
                if(l>=6.5 and l<=20.5):
                    num=707
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=708
                if(l>0.05 and l<1.5):
                    num=709
                if(l>=1.5 and l<3.5):
                    num=710
                if(l>=3.5 and l<6.5):
                    num=711
                if(l>=6.5 and l<=20.5):
                    num=712
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=713
                if(l>0.05 and l<1.5):
                    num=714
                if(l>=1.5 and l<3.5):
                    num=715
                if(l>=3.5 and l<6.5):
                    num=716
                if(l>=6.5 and l<=20.5):
                    num=717
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=718
                if(l>0.05 and l<1.5):
                    num=719
                if(l>=1.5 and l<3.5):
                    num=720
                if(l>=3.5 and l<6.5):
                    num=721
                if(l>=6.5 and l<=20.5):
                    num=722
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=723
                if(l>0.05 and l<1.5):
                    num=724
                if(l>=1.5 and l<3.5):
                    num=725
                if(l>=3.5 and l<6.5):
                    num=726
                if(l>=6.5 and l<=20.5):
                    num=727
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=728
                if(l>0.05 and l<1.5):
                    num=729
                if(l>=1.5 and l<3.5):
                    num=730
                if(l>=3.5 and l<6.5):
                    num=731
                if(l>=6.5 and l<=20.5):
                    num=732
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=733
                if(l>0.05 and l<1.5):
                    num=734
                if(l>=1.5 and l<3.5):
                    num=735
                if(l>=3.5 and l<6.5):
                    num=736
                if(l>=6.5 and l<=20.5):
                    num=737
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=738
                if(l>0.05 and l<1.5):
                    num=739
                if(l>=1.5 and l<3.5):
                    num=740
                if(l>=3.5 and l<6.5):
                    num=741
                if(l>=6.5 and l<=20.5):
                    num=742
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=743
                if(l>0.05 and l<1.5):
                    num=744
                if(l>=1.5 and l<3.5):
                    num=745
                if(l>=3.5 and l<6.5):
                    num=746
                if(l>=6.5 and l<=20.5):
                    num=747
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=748
                if(l>0.05 and l<1.5):
                    num=749
                if(l>=1.5 and l<3.5):
                    num=750
                if(l>=3.5 and l<6.5):
                    num=751
                if(l>=6.5 and l<=20.5):
                    num=752
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=753
                if(l>0.05 and l<1.5):
                    num=754
                if(l>=1.5 and l<3.5):
                    num=755
                if(l>=3.5 and l<6.5):
                    num=756
                if(l>=6.5 and l<=20.5):
                    num=757
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=758
                if(l>0.05 and l<1.5):
                    num=759
                if(l>=1.5 and l<3.5):
                    num=760
                if(l>=3.5 and l<6.5):
                    num=761
                if(l>=6.5 and l<=20.5):
                    num=762
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=763
                if(l>0.05 and l<1.5):
                    num=764
                if(l>=1.5 and l<3.5):
                    num=765
                if(l>=3.5 and l<6.5):
                    num=766
                if(l>=6.5 and l<=20.5):
                    num=767
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=768
                if(l>0.05 and l<1.5):
                    num=769
                if(l>=1.5 and l<3.5):
                    num=770
                if(l>=3.5 and l<6.5):
                    num=771
                if(l>=6.5 and l<=20.5):
                    num=772
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=773
                if(l>0.05 and l<1.5):
                    num=774
                if(l>=1.5 and l<3.5):
                    num=775
                if(l>=3.5 and l<6.5):
                    num=776
                if(l>=6.5 and l<=20.5):
                    num=777
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=778
                if(l>0.05 and l<1.5):
                    num=779
                if(l>=1.5 and l<3.5):
                    num=780
                if(l>=3.5 and l<6.5):
                    num=781
                if(l>=6.5 and l<=20.5):
                    num=782
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=783
                if(l>0.05 and l<1.5):
                    num=784
                if(l>=1.5 and l<3.5):
                    num=785
                if(l>=3.5 and l<6.5):
                    num=786
                if(l>=6.5 and l<=20.5):
                    num=787
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=788
                if(l>0.05 and l<1.5):
                    num=789
                if(l>=1.5 and l<3.5):
                    num=790
                if(l>=3.5 and l<6.5):
                    num=791
                if(l>=6.5 and l<=20.5):
                    num=792
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=793
                if(l>0.05 and l<1.5):
                    num=794
                if(l>=1.5 and l<3.5):
                    num=795
                if(l>=3.5 and l<6.5):
                    num=796
                if(l>=6.5 and l<=20.5):
                    num=797
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=798
                if(l>0.05 and l<1.5):
                    num=799
                if(l>=1.5 and l<3.5):
                    num=800
                if(l>=3.5 and l<6.5):
                    num=801
                if(l>=6.5 and l<=20.5):
                    num=802
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=803
                if(l>0.05 and l<1.5):
                    num=804
                if(l>=1.5 and l<3.5):
                    num=805
                if(l>=3.5 and l<6.5):
                    num=806
                if(l>=6.5 and l<=20.5):
                    num=807
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=808
                if(l>0.05 and l<1.5):
                    num=809
                if(l>=1.5 and l<3.5):
                    num=810
                if(l>=3.5 and l<6.5):
                    num=811
                if(l>=6.5 and l<=20.5):
                    num=812
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=813
                if(l>0.05 and l<1.5):
                    num=814
                if(l>=1.5 and l<3.5):
                    num=815
                if(l>=3.5 and l<6.5):
                    num=816
                if(l>=6.5 and l<=20.5):
                    num=817
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=818
                if(l>0.05 and l<1.5):
                    num=819
                if(l>=1.5 and l<3.5):
                    num=820
                if(l>=3.5 and l<6.5):
                    num=821
                if(l>=6.5 and l<=20.5):
                    num=822
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=823
                if(l>0.05 and l<1.5):
                    num=824
                if(l>=1.5 and l<3.5):
                    num=825
                if(l>=3.5 and l<6.5):
                    num=826
                if(l>=6.5 and l<=20.5):
                    num=827
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=828
                if(l>0.05 and l<1.5):
                    num=829
                if(l>=1.5 and l<3.5):
                    num=830
                if(l>=3.5 and l<6.5):
                    num=831
                if(l>=6.5 and l<=20.5):
                    num=832
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=833
                if(l>0.05 and l<1.5):
                    num=834
                if(l>=1.5 and l<3.5):
                    num=835
                if(l>=3.5 and l<6.5):
                    num=836
                if(l>=6.5 and l<=20.5):
                    num=837
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=838
                if(l>0.05 and l<1.5):
                    num=839
                if(l>=1.5 and l<3.5):
                    num=840
                if(l>=3.5 and l<6.5):
                    num=841
                if(l>=6.5 and l<=20.5):
                    num=842
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=843
                if(l>0.05 and l<1.5):
                    num=844
                if(l>=1.5 and l<3.5):
                    num=845
                if(l>=3.5 and l<6.5):
                    num=846
                if(l>=6.5 and l<=20.5):
                    num=847
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=848
                if(l>0.05 and l<1.5):
                    num=849
                if(l>=1.5 and l<3.5):
                    num=850
                if(l>=3.5 and l<6.5):
                    num=851
                if(l>=6.5 and l<=20.5):
                    num=852
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=853
                if(l>0.05 and l<1.5):
                    num=854
                if(l>=1.5 and l<3.5):
                    num=855
                if(l>=3.5 and l<6.5):
                    num=856
                if(l>=6.5 and l<=20.5):
                    num=857
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=858
                if(l>0.05 and l<1.5):
                    num=859
                if(l>=1.5 and l<3.5):
                    num=860
                if(l>=3.5 and l<6.5):
                    num=861
                if(l>=6.5 and l<=20.5):
                    num=862
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=863
                if(l>0.05 and l<1.5):
                    num=864
                if(l>=1.5 and l<3.5):
                    num=865
                if(l>=3.5 and l<6.5):
                    num=866
                if(l>=6.5 and l<=20.5):
                    num=867
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=868
                if(l>0.05 and l<1.5):
                    num=869
                if(l>=1.5 and l<3.5):
                    num=870
                if(l>=3.5 and l<6.5):
                    num=871
                if(l>=6.5 and l<=20.5):
                    num=872
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=873
                if(l>0.05 and l<1.5):
                    num=874
                if(l>=1.5 and l<3.5):
                    num=875
                if(l>=3.5 and l<6.5):
                    num=876
                if(l>=6.5 and l<=20.5):
                    num=877
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=878
            if(l>0.05 and l<1.5):
                num=879
            if(l>=1.5 and l<3.5):
                num=880
            if(l>=3.5 and l<6.5):
                num=881
            if(l>=6.5 and l<=20.5):
                num=882



    if(open>=1 and open <3):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=883
            if(h>0.05 and h<1.5):
                num=884
            if(h>=1.5 and h<3.5):
                num=885
            if(h>=3.5 and h<6.5):
                num=886
            if(h>=6.5 and h<=20.5):
                num=887
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=888
                if(l>0.05 and l<1.5):
                    num=889
                if(l>=1.5 and l<3.5):
                    num=890
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=891
                if(l>0.05 and l<1.5):
                    num=892
                if(l>=1.5 and l<3.5):
                    num=893
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=894
                if(l>0.05 and l<1.5):
                    num=895
                if(l>=1.5 and l<3.5):
                    num=896
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=897
                if(l>0.05 and l<1.5):
                    num=898
                if(l>=1.5 and l<3.5):
                    num=899
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=900
                if(l>0.05 and l<1.5):
                    num=901
                if(l>=1.5 and l<3.5):
                    num=902
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=903
                if(l>0.05 and l<1.5):
                    num=904
                if(l>=1.5 and l<3.5):
                    num=905
                if(l>=3.5 and l<6.5):
                    num=906
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=907
                if(l>0.05 and l<1.5):
                    num=908
                if(l>=1.5 and l<3.5):
                    num=909
                if(l>=3.5 and l<6.5):
                    num=910
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=911
                if(l>0.05 and l<1.5):
                    num=912
                if(l>=1.5 and l<3.5):
                    num=913
                if(l>=3.5 and l<6.5):
                    num=914
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=915
                if(l>0.05 and l<1.5):
                    num=916
                if(l>=1.5 and l<3.5):
                    num=917
                if(l>=3.5 and l<6.5):
                    num=918
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=919
                if(l>0.05 and l<1.5):
                    num=920
                if(l>=1.5 and l<3.5):
                    num=921
                if(l>=3.5 and l<6.5):
                    num=922
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=923
                if(l>0.05 and l<1.5):
                    num=924
                if(l>=1.5 and l<3.5):
                    num=925
                if(l>=3.5 and l<6.5):
                    num=926
                if(l>=6.5 and l<=20.5):
                    num=927
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=928
                if(l>0.05 and l<1.5):
                    num=929
                if(l>=1.5 and l<3.5):
                    num=930
                if(l>=3.5 and l<6.5):
                    num=931
                if(l>=6.5 and l<=20.5):
                    num=932
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=933
                if(l>0.05 and l<1.5):
                    num=934
                if(l>=1.5 and l<3.5):
                    num=935
                if(l>=3.5 and l<6.5):
                    num=936
                if(l>=6.5 and l<=20.5):
                    num=937
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=938
                if(l>0.05 and l<1.5):
                    num=939
                if(l>=1.5 and l<3.5):
                    num=940
                if(l>=3.5 and l<6.5):
                    num=941
                if(l>=6.5 and l<=20.5):
                    num=942
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=943
                if(l>0.05 and l<1.5):
                    num=944
                if(l>=1.5 and l<3.5):
                    num=945
                if(l>=3.5 and l<6.5):
                    num=946
                if(l>=6.5 and l<=20.5):
                    num=947
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=948
                if(l>0.05 and l<1.5):
                    num=949
                if(l>=1.5 and l<3.5):
                    num=950
                if(l>=3.5 and l<6.5):
                    num=951
                if(l>=6.5 and l<=20.5):
                    num=952
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=953
                if(l>0.05 and l<1.5):
                    num=954
                if(l>=1.5 and l<3.5):
                    num=955
                if(l>=3.5 and l<6.5):
                    num=956
                if(l>=6.5 and l<=20.5):
                    num=957
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=958
                if(l>0.05 and l<1.5):
                    num=959
                if(l>=1.5 and l<3.5):
                    num=960
                if(l>=3.5 and l<6.5):
                    num=961
                if(l>=6.5 and l<=20.5):
                    num=962
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=963
                if(l>0.05 and l<1.5):
                    num=964
                if(l>=1.5 and l<3.5):
                    num=965
                if(l>=3.5 and l<6.5):
                    num=966
                if(l>=6.5 and l<=20.5):
                    num=967
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=968
                if(l>0.05 and l<1.5):
                    num=969
                if(l>=1.5 and l<3.5):
                    num=970
                if(l>=3.5 and l<6.5):
                    num=971
                if(l>=6.5 and l<=20.5):
                    num=972
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=973
                if(l>0.05 and l<1.5):
                    num=974
                if(l>=1.5 and l<3.5):
                    num=975
                if(l>=3.5 and l<6.5):
                    num=976
                if(l>=6.5 and l<=20.5):
                    num=977
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=978
                if(l>0.05 and l<1.5):
                    num=979
                if(l>=1.5 and l<3.5):
                    num=980
                if(l>=3.5 and l<6.5):
                    num=981
                if(l>=6.5 and l<=20.5):
                    num=982
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=983
                if(l>0.05 and l<1.5):
                    num=984
                if(l>=1.5 and l<3.5):
                    num=985
                if(l>=3.5 and l<6.5):
                    num=986
                if(l>=6.5 and l<=20.5):
                    num=987
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=988
                if(l>0.05 and l<1.5):
                    num=989
                if(l>=1.5 and l<3.5):
                    num=990
                if(l>=3.5 and l<6.5):
                    num=991
                if(l>=6.5 and l<=20.5):
                    num=992
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=993
                if(l>0.05 and l<1.5):
                    num=994
                if(l>=1.5 and l<3.5):
                    num=995
                if(l>=3.5 and l<6.5):
                    num=996
                if(l>=6.5 and l<=20.5):
                    num=997
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=998
                if(l>0.05 and l<1.5):
                    num=999
                if(l>=1.5 and l<3.5):
                    num=1000
                if(l>=3.5 and l<6.5):
                    num=1001
                if(l>=6.5 and l<=20.5):
                    num=1002
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1003
                if(l>0.05 and l<1.5):
                    num=1004
                if(l>=1.5 and l<3.5):
                    num=1005
                if(l>=3.5 and l<6.5):
                    num=1006
                if(l>=6.5 and l<=20.5):
                    num=1007
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1008
                if(l>0.05 and l<1.5):
                    num=1009
                if(l>=1.5 and l<3.5):
                    num=1010
                if(l>=3.5 and l<6.5):
                    num=1011
                if(l>=6.5 and l<=20.5):
                    num=1012
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1013
                if(l>0.05 and l<1.5):
                    num=1014
                if(l>=1.5 and l<3.5):
                    num=1015
                if(l>=3.5 and l<6.5):
                    num=1016
                if(l>=6.5 and l<=20.5):
                    num=1017
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1018
                if(l>0.05 and l<1.5):
                    num=1019
                if(l>=1.5 and l<3.5):
                    num=1020
                if(l>=3.5 and l<6.5):
                    num=1021
                if(l>=6.5 and l<=20.5):
                    num=1022
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1023
                if(l>0.05 and l<1.5):
                    num=1024
                if(l>=1.5 and l<3.5):
                    num=1025
                if(l>=3.5 and l<6.5):
                    num=1026
                if(l>=6.5 and l<=20.5):
                    num=1027
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1028
                if(l>0.05 and l<1.5):
                    num=1029
                if(l>=1.5 and l<3.5):
                    num=1030
                if(l>=3.5 and l<6.5):
                    num=1031
                if(l>=6.5 and l<=20.5):
                    num=1032
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1033
                if(l>0.05 and l<1.5):
                    num=1034
                if(l>=1.5 and l<3.5):
                    num=1035
                if(l>=3.5 and l<6.5):
                    num=1036
                if(l>=6.5 and l<=20.5):
                    num=1037
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1038
                if(l>0.05 and l<1.5):
                    num=1039
                if(l>=1.5 and l<3.5):
                    num=1040
                if(l>=3.5 and l<6.5):
                    num=1041
                if(l>=6.5 and l<=20.5):
                    num=1042
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1043
                if(l>0.05 and l<1.5):
                    num=1044
                if(l>=1.5 and l<3.5):
                    num=1045
                if(l>=3.5 and l<6.5):
                    num=1046
                if(l>=6.5 and l<=20.5):
                    num=1047
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1048
                if(l>0.05 and l<1.5):
                    num=1049
                if(l>=1.5 and l<3.5):
                    num=1050
                if(l>=3.5 and l<6.5):
                    num=1051
                if(l>=6.5 and l<=20.5):
                    num=1052
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1053
                if(l>0.05 and l<1.5):
                    num=1054
                if(l>=1.5 and l<3.5):
                    num=1055
                if(l>=3.5 and l<6.5):
                    num=1056
                if(l>=6.5 and l<=20.5):
                    num=1057
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1058
                if(l>0.05 and l<1.5):
                    num=1059
                if(l>=1.5 and l<3.5):
                    num=1060
                if(l>=3.5 and l<6.5):
                    num=1061
                if(l>=6.5 and l<=20.5):
                    num=1062
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1063
                if(l>0.05 and l<1.5):
                    num=1064
                if(l>=1.5 and l<3.5):
                    num=1065
                if(l>=3.5 and l<6.5):
                    num=1066
                if(l>=6.5 and l<=20.5):
                    num=1067
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1068
                if(l>0.05 and l<1.5):
                    num=1069
                if(l>=1.5 and l<3.5):
                    num=1070
                if(l>=3.5 and l<6.5):
                    num=1071
                if(l>=6.5 and l<=20.5):
                    num=1072
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1073
                if(l>0.05 and l<1.5):
                    num=1074
                if(l>=1.5 and l<3.5):
                    num=1075
                if(l>=3.5 and l<6.5):
                    num=1076
                if(l>=6.5 and l<=20.5):
                    num=1077
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1078
                if(l>0.05 and l<1.5):
                    num=1079
                if(l>=1.5 and l<3.5):
                    num=1080
                if(l>=3.5 and l<6.5):
                    num=1081
                if(l>=6.5 and l<=20.5):
                    num=1082
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1083
                if(l>0.05 and l<1.5):
                    num=1084
                if(l>=1.5 and l<3.5):
                    num=1085
                if(l>=3.5 and l<6.5):
                    num=1086
                if(l>=6.5 and l<=20.5):
                    num=1087
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1088
                if(l>0.05 and l<1.5):
                    num=1089
                if(l>=1.5 and l<3.5):
                    num=1090
                if(l>=3.5 and l<6.5):
                    num=1091
                if(l>=6.5 and l<=20.5):
                    num=1092
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1093
                if(l>0.05 and l<1.5):
                    num=1094
                if(l>=1.5 and l<3.5):
                    num=1095
                if(l>=3.5 and l<6.5):
                    num=1096
                if(l>=6.5 and l<=20.5):
                    num=1097
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1098
                if(l>0.05 and l<1.5):
                    num=1099
                if(l>=1.5 and l<3.5):
                    num=1100
                if(l>=3.5 and l<6.5):
                    num=1101
                if(l>=6.5 and l<=20.5):
                    num=1102
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1103
                if(l>0.05 and l<1.5):
                    num=1104
                if(l>=1.5 and l<3.5):
                    num=1105
                if(l>=3.5 and l<6.5):
                    num=1106
                if(l>=6.5 and l<=20.5):
                    num=1107
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1108
            if(l>0.05 and l<1.5):
                num=1109
            if(l>=1.5 and l<3.5):
                num=1110
            if(l>=3.5 and l<6.5):
                num=1110
            if(l>=6.5 and l<=20.5):
                num=1112




    if(open>=3 and open <7):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=1113
            if(h>0.05 and h<1.5):
                num=1114
            if(h>=1.5 and h<3.5):
                num=1115
            if(h>=3.5 and h<6.5):
                num=1116
            if(h>=6.5 and h<=20.5):
                num=1117
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1118
                if(l>0.05 and l<1.5):
                    num=1119
                if(l>=1.5 and l<3.5):
                    num=1120
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1121
                if(l>0.05 and l<1.5):
                    num=1122
                if(l>=1.5 and l<3.5):
                    num=1123
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1124
                if(l>0.05 and l<1.5):
                    num=1125
                if(l>=1.5 and l<3.5):
                    num=1126
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1127
                if(l>0.05 and l<1.5):
                    num=1128
                if(l>=1.5 and l<3.5):
                    num=1129
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1130
                if(l>0.05 and l<1.5):
                    num=1131
                if(l>=1.5 and l<3.5):
                    num=1132
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1133
                if(l>0.05 and l<1.5):
                    num=1134
                if(l>=1.5 and l<3.5):
                    num=1135
                if(l>=3.5 and l<6.5):
                    num=1136
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1137
                if(l>0.05 and l<1.5):
                    num=1138
                if(l>=1.5 and l<3.5):
                    num=1139
                if(l>=3.5 and l<6.5):
                    num=1140
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1141
                if(l>0.05 and l<1.5):
                    num=1142
                if(l>=1.5 and l<3.5):
                    num=1143
                if(l>=3.5 and l<6.5):
                    num=1144
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1145
                if(l>0.05 and l<1.5):
                    num=1146
                if(l>=1.5 and l<3.5):
                    num=1147
                if(l>=3.5 and l<6.5):
                    num=1148
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1149
                if(l>0.05 and l<1.5):
                    num=1150
                if(l>=1.5 and l<3.5):
                    num=1151
                if(l>=3.5 and l<6.5):
                    num=1152
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1153
                if(l>0.05 and l<1.5):
                    num=1154
                if(l>=1.5 and l<3.5):
                    num=1155
                if(l>=3.5 and l<6.5):
                    num=1156
                if(l>=6.5 and l<=20.5):
                    num=1157
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1158
                if(l>0.05 and l<1.5):
                    num=1159
                if(l>=1.5 and l<3.5):
                    num=1160
                if(l>=3.5 and l<6.5):
                    num=1161
                if(l>=6.5 and l<=20.5):
                    num=1162
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1163
                if(l>0.05 and l<1.5):
                    num=1164
                if(l>=1.5 and l<3.5):
                    num=1165
                if(l>=3.5 and l<6.5):
                    num=1166
                if(l>=6.5 and l<=20.5):
                    num=1167
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1168
                if(l>0.05 and l<1.5):
                    num=1169
                if(l>=1.5 and l<3.5):
                    num=1170
                if(l>=3.5 and l<6.5):
                    num=1171
                if(l>=6.5 and l<=20.5):
                    num=1172
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1173
                if(l>0.05 and l<1.5):
                    num=1174
                if(l>=1.5 and l<3.5):
                    num=1175
                if(l>=3.5 and l<6.5):
                    num=1176
                if(l>=6.5 and l<=20.5):
                    num=1177
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1178
                if(l>0.05 and l<1.5):
                    num=1179
                if(l>=1.5 and l<3.5):
                    num=1180
                if(l>=3.5 and l<6.5):
                    num=1181
                if(l>=6.5 and l<=20.5):
                    num=1182
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1183
                if(l>0.05 and l<1.5):
                    num=1184
                if(l>=1.5 and l<3.5):
                    num=1185
                if(l>=3.5 and l<6.5):
                    num=1186
                if(l>=6.5 and l<=20.5):
                    num=1187
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1188
                if(l>0.05 and l<1.5):
                    num=1189
                if(l>=1.5 and l<3.5):
                    num=1190
                if(l>=3.5 and l<6.5):
                    num=1191
                if(l>=6.5 and l<=20.5):
                    num=1192
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1193
                if(l>0.05 and l<1.5):
                    num=1194
                if(l>=1.5 and l<3.5):
                    num=1195
                if(l>=3.5 and l<6.5):
                    num=1196
                if(l>=6.5 and l<=20.5):
                    num=1197
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1198
                if(l>0.05 and l<1.5):
                    num=1199
                if(l>=1.5 and l<3.5):
                    num=1200
                if(l>=3.5 and l<6.5):
                    num=1201
                if(l>=6.5 and l<=20.5):
                    num=1202
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1203
                if(l>0.05 and l<1.5):
                    num=1204
                if(l>=1.5 and l<3.5):
                    num=1205
                if(l>=3.5 and l<6.5):
                    num=1206
                if(l>=6.5 and l<=20.5):
                    num=1207
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1208
                if(l>0.05 and l<1.5):
                    num=1209
                if(l>=1.5 and l<3.5):
                    num=1210
                if(l>=3.5 and l<6.5):
                    num=1211
                if(l>=6.5 and l<=20.5):
                    num=1212
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1213
                if(l>0.05 and l<1.5):
                    num=1214
                if(l>=1.5 and l<3.5):
                    num=1215
                if(l>=3.5 and l<6.5):
                    num=1216
                if(l>=6.5 and l<=20.5):
                    num=1217
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1218
                if(l>0.05 and l<1.5):
                    num=1219
                if(l>=1.5 and l<3.5):
                    num=1220
                if(l>=3.5 and l<6.5):
                    num=1221
                if(l>=6.5 and l<=20.5):
                    num=1222
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1223
                if(l>0.05 and l<1.5):
                    num=1224
                if(l>=1.5 and l<3.5):
                    num=1225
                if(l>=3.5 and l<6.5):
                    num=1226
                if(l>=6.5 and l<=20.5):
                    num=1227
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1228
                if(l>0.05 and l<1.5):
                    num=1229
                if(l>=1.5 and l<3.5):
                    num=1230
                if(l>=3.5 and l<6.5):
                    num=1231
                if(l>=6.5 and l<=20.5):
                    num=1232
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1233
                if(l>0.05 and l<1.5):
                    num=1234
                if(l>=1.5 and l<3.5):
                    num=1235
                if(l>=3.5 and l<6.5):
                    num=1236
                if(l>=6.5 and l<=20.5):
                    num=1237
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1238
                if(l>0.05 and l<1.5):
                    num=1239
                if(l>=1.5 and l<3.5):
                    num=1240
                if(l>=3.5 and l<6.5):
                    num=1241
                if(l>=6.5 and l<=20.5):
                    num=1242
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1243
                if(l>0.05 and l<1.5):
                    num=1244
                if(l>=1.5 and l<3.5):
                    num=1245
                if(l>=3.5 and l<6.5):
                    num=1246
                if(l>=6.5 and l<=20.5):
                    num=1247
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1248
                if(l>0.05 and l<1.5):
                    num=1249
                if(l>=1.5 and l<3.5):
                    num=1250
                if(l>=3.5 and l<6.5):
                    num=1251
                if(l>=6.5 and l<=20.5):
                    num=1252
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1253
                if(l>0.05 and l<1.5):
                    num=1254
                if(l>=1.5 and l<3.5):
                    num=1255
                if(l>=3.5 and l<6.5):
                    num=1256
                if(l>=6.5 and l<=20.5):
                    num=1257
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1258
                if(l>0.05 and l<1.5):
                    num=1259
                if(l>=1.5 and l<3.5):
                    num=1260
                if(l>=3.5 and l<6.5):
                    num=1261
                if(l>=6.5 and l<=20.5):
                    num=1262
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1263
                if(l>0.05 and l<1.5):
                    num=1264
                if(l>=1.5 and l<3.5):
                    num=1265
                if(l>=3.5 and l<6.5):
                    num=1266
                if(l>=6.5 and l<=20.5):
                    num=1267
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1268
                if(l>0.05 and l<1.5):
                    num=1269
                if(l>=1.5 and l<3.5):
                    num=1270
                if(l>=3.5 and l<6.5):
                    num=1271
                if(l>=6.5 and l<=20.5):
                    num=1272
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1273
                if(l>0.05 and l<1.5):
                    num=1274
                if(l>=1.5 and l<3.5):
                    num=1275
                if(l>=3.5 and l<6.5):
                    num=1276
                if(l>=6.5 and l<=20.5):
                    num=1277
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1278
                if(l>0.05 and l<1.5):
                    num=1279
                if(l>=1.5 and l<3.5):
                    num=1280
                if(l>=3.5 and l<6.5):
                    num=1281
                if(l>=6.5 and l<=20.5):
                    num=1282
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1283
                if(l>0.05 and l<1.5):
                    num=1284
                if(l>=1.5 and l<3.5):
                    num=1285
                if(l>=3.5 and l<6.5):
                    num=1286
                if(l>=6.5 and l<=20.5):
                    num=1287
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1288
                if(l>0.05 and l<1.5):
                    num=1289
                if(l>=1.5 and l<3.5):
                    num=1290
                if(l>=3.5 and l<6.5):
                    num=1291
                if(l>=6.5 and l<=20.5):
                    num=1292
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1293
                if(l>0.05 and l<1.5):
                    num=1294
                if(l>=1.5 and l<3.5):
                    num=1295
                if(l>=3.5 and l<6.5):
                    num=1296
                if(l>=6.5 and l<=20.5):
                    num=1297
            if(h>=6.5 and h<=20.5):
                if(l>=0 and l<=0.05):
                    num=1298
                if(l>0.05 and l<1.5):
                    num=1299
                if(l>=1.5 and l<3.5):
                    num=1300
                if(l>=3.5 and l<6.5):
                    num=1301
                if(l>=6.5 and l<=20.5):
                    num=1302
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1303
                if(l>0.05 and l<1.5):
                    num=1304
                if(l>=1.5 and l<3.5):
                    num=1305
                if(l>=3.5 and l<6.5):
                    num=1306
                if(l>=6.5 and l<=20.5):
                    num=1307
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1308
                if(l>0.05 and l<1.5):
                    num=1309
                if(l>=1.5 and l<3.5):
                    num=1310
                if(l>=3.5 and l<6.5):
                    num=1311
                if(l>=6.5 and l<=20.5):
                    num=1312
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1313
                if(l>0.05 and l<1.5):
                    num=1314
                if(l>=1.5 and l<3.5):
                    num=1315
                if(l>=3.5 and l<6.5):
                    num=1316
                if(l>=6.5 and l<=20.5):
                    num=1317
            if(h>=3.5 and h<6.5):
                if(l>=0 and l<=0.05):
                    num=1318
                if(l>0.05 and l<1.5):
                    num=1319
                if(l>=1.5 and l<3.5):
                    num=1320
                if(l>=3.5 and l<6.5):
                    num=1321
                if(l>=6.5 and l<=20.5):
                    num=1322
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1323
                if(l>0.05 and l<1.5):
                    num=1324
                if(l>=1.5 and l<3.5):
                    num=1325
                if(l>=3.5 and l<6.5):
                    num=1326
                if(l>=6.5 and l<=20.5):
                    num=1327
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1328
                if(l>0.05 and l<1.5):
                    num=1329
                if(l>=1.5 and l<3.5):
                    num=1330
                if(l>=3.5 and l<6.5):
                    num=1331
                if(l>=6.5 and l<=20.5):
                    num=1332
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1333
                if(l>0.05 and l<1.5):
                    num=1334
                if(l>=1.5 and l<3.5):
                    num=1335
                if(l>=3.5 and l<6.5):
                    num=1336
                if(l>=6.5 and l<=20.5):
                    num=1337
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1338
            if(l>0.05 and l<1.5):
                num=1339
            if(l>=1.5 and l<3.5):
                num=1340
            if(l>=3.5 and l<6.5):
                num=1341
            if(l>=6.5 and l<=20.5):
                num=1342



    if(open>=7 and open <9.96):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                num=1343
            if(h>0.05 and h<1.5):
                num=1344
            if(h>=1.5 and h<3.5):
                num=1345
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1346
                if(l>0.05 and l<1.5):
                    num=1347
                if(l>=1.5 and l<3.5):
                    num=1348
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1349
                if(l>0.05 and l<1.5):
                    num=1350
                if(l>=1.5 and l<3.5):
                    num=1351
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1352
                if(l>0.05 and l<1.5):
                    num=1353
                if(l>=1.5 and l<3.5):
                    num=1354
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1355
                if(l>0.05 and l<1.5):
                    num=1356
                if(l>=1.5 and l<3.5):
                    num=1357
                if(l>=3.5 and l<6.5):
                    num=1358
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1359
                if(l>0.05 and l<1.5):
                    num=1360
                if(l>=1.5 and l<3.5):
                    num=1361
                if(l>=3.5 and l<6.5):
                    num=1362
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1363
                if(l>0.05 and l<1.5):
                    num=1364
                if(l>=1.5 and l<3.5):
                    num=1365
                if(l>=3.5 and l<6.5):
                    num=1366
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1367
                if(l>0.05 and l<1.5):
                    num=1368
                if(l>=1.5 and l<3.5):
                    num=1369
                if(l>=3.5 and l<6.5):
                    num=1370
                if(l>=6.5 and l<=20.5):
                    num=1371
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1372
                if(l>0.05 and l<1.5):
                    num=1373
                if(l>=1.5 and l<3.5):
                    num=1374
                if(l>=3.5 and l<6.5):
                    num=1375
                if(l>=6.5 and l<=20.5):
                    num=1376
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1377
                if(l>0.05 and l<1.5):
                    num=1378
                if(l>=1.5 and l<3.5):
                    num=1379
                if(l>=3.5 and l<6.5):
                    num=1380
                if(l>=6.5 and l<=20.5):
                    num=1381
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1382
                if(l>0.05 and l<1.5):
                    num=1383
                if(l>=1.5 and l<3.5):
                    num=1384
                if(l>=3.5 and l<6.5):
                    num=1385
                if(l>=6.5 and l<=20.5):
                    num=1386
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1387
                if(l>0.05 and l<1.5):
                    num=1388
                if(l>=1.5 and l<3.5):
                    num=1389
                if(l>=3.5 and l<6.5):
                    num=1390
                if(l>=6.5 and l<=20.5):
                    num=1391
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1392
                if(l>0.05 and l<1.5):
                    num=1393
                if(l>=1.5 and l<3.5):
                    num=1394
                if(l>=3.5 and l<6.5):
                    num=1395
                if(l>=6.5 and l<=20.5):
                    num=1396
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1397
                if(l>0.05 and l<1.5):
                    num=1398
                if(l>=1.5 and l<3.5):
                    num=1399
                if(l>=3.5 and l<6.5):
                    num=1400
                if(l>=6.5 and l<=20.5):
                    num=1401
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1402
                if(l>0.05 and l<1.5):
                    num=1403
                if(l>=1.5 and l<3.5):
                    num=1404
                if(l>=3.5 and l<6.5):
                    num=1405
                if(l>=6.5 and l<=20.5):
                    num=1406
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1407
                if(l>0.05 and l<1.5):
                    num=1408
                if(l>=1.5 and l<3.5):
                    num=1409
                if(l>=3.5 and l<6.5):
                    num=1410
                if(l>=6.5 and l<=20.5):
                    num=1411
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1412
                if(l>0.05 and l<1.5):
                    num=1413
                if(l>=1.5 and l<3.5):
                    num=1414
                if(l>=3.5 and l<6.5):
                    num=1415
                if(l>=6.5 and l<=20.5):
                    num=1416
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1417
                if(l>0.05 and l<1.5):
                    num=1418
                if(l>=1.5 and l<3.5):
                    num=1419
                if(l>=3.5 and l<6.5):
                    num=1420
                if(l>=6.5 and l<=20.5):
                    num=1421
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1422
                if(l>0.05 and l<1.5):
                    num=1423
                if(l>=1.5 and l<3.5):
                    num=1424
                if(l>=3.5 and l<6.5):
                    num=1425
                if(l>=6.5 and l<=20.5):
                    num=1426
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1427
                if(l>0.05 and l<1.5):
                    num=1428
                if(l>=1.5 and l<3.5):
                    num=1429
                if(l>=3.5 and l<6.5):
                    num=1430
                if(l>=6.5 and l<=20.5):
                    num=1431
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1432
                if(l>0.05 and l<1.5):
                    num=1433
                if(l>=1.5 and l<3.5):
                    num=1434
                if(l>=3.5 and l<6.5):
                    num=1435
                if(l>=6.5 and l<=20.5):
                    num=1436
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1437
                if(l>0.05 and l<1.5):
                    num=1438
                if(l>=1.5 and l<3.5):
                    num=1439
                if(l>=3.5 and l<6.5):
                    num=1440
                if(l>=6.5 and l<=20.5):
                    num=1441
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1442
                if(l>0.05 and l<1.5):
                    num=1443
                if(l>=1.5 and l<3.5):
                    num=1444
                if(l>=3.5 and l<6.5):
                    num=1445
                if(l>=6.5 and l<=20.5):
                    num=1446
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1447
                if(l>0.05 and l<1.5):
                    num=1448
                if(l>=1.5 and l<3.5):
                    num=1449
                if(l>=3.5 and l<6.5):
                    num=1450
                if(l>=6.5 and l<=20.5):
                    num=1451
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1452
                if(l>0.05 and l<1.5):
                    num=1453
                if(l>=1.5 and l<3.5):
                    num=1454
                if(l>=3.5 and l<6.5):
                    num=1455
                if(l>=6.5 and l<=20.5):
                    num=1456
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1457
                if(l>0.05 and l<1.5):
                    num=1458
                if(l>=1.5 and l<3.5):
                    num=1459
                if(l>=3.5 and l<6.5):
                    num=1460
                if(l>=6.5 and l<=20.5):
                    num=1461
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1462
                if(l>0.05 and l<1.5):
                    num=1463
                if(l>=1.5 and l<3.5):
                    num=1464
                if(l>=3.5 and l<6.5):
                    num=1465
                if(l>=6.5 and l<=20.5):
                    num=1466
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1467
                if(l>0.05 and l<1.5):
                    num=1468
                if(l>=1.5 and l<3.5):
                    num=1469
                if(l>=3.5 and l<6.5):
                    num=1470
                if(l>=6.5 and l<=20.5):
                    num=1471
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(h>=0 and h<=0.05):
                if(l>=0 and l<=0.05):
                    num=1472
                if(l>0.05 and l<1.5):
                    num=1473
                if(l>=1.5 and l<3.5):
                    num=1474
                if(l>=3.5 and l<6.5):
                    num=1475
                if(l>=6.5 and l<=20.5):
                    num=1476
            if(h>0.05 and h<1.5):
                if(l>=0 and l<=0.05):
                    num=1477
                if(l>0.05 and l<1.5):
                    num=1478
                if(l>=1.5 and l<3.5):
                    num=1479
                if(l>=3.5 and l<6.5):
                    num=1480
                if(l>=6.5 and l<=20.5):
                    num=1481
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<=0.05):
                    num=1482
                if(l>0.05 and l<1.5):
                    num=1483
                if(l>=1.5 and l<3.5):
                    num=1484
                if(l>=3.5 and l<6.5):
                    num=1485
                if(l>=6.5 and l<=20.5):
                    num=1486
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1487
            if(l>0.05 and l<1.5):
                num=1488
            if(l>=1.5 and l<3.5):
                num=1489
            if(l>=3.5 and l<6.5):
                num=1490
            if(l>=6.5 and l<=20.5):
                num=1491



    if(open>=9.96 and open <=10.51):
        if(close>=-10.5 and close<=-9.96):
            h,l=js(open,high,low,close)
            num=1492
        if(close>-9.96 and close<-7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1493
            if(l>0.05 and l<1.5):
                num=1494
            if(l>=1.5 and l<3.5):
                num=1495
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1496
            if(l>0.05 and l<1.5):
                num=1497
            if(l>=1.5 and l<3.5):
                num=1498
            if(l>=3.5 and l<6.5):
                num=1499
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1500
            if(l>0.05 and l<1.5):
                num=1501
            if(l>=1.5 and l<3.5):
                num=1502
            if(l>=3.5 and l<6.5):
                num=1503
            if(l>=6.5 and l<=20.5):
                num=1504
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1505
            if(l>0.05 and l<1.5):
                num=1506
            if(l>=1.5 and l<3.5):
                num=1507
            if(l>=3.5 and l<6.5):
                num=1508
            if(l>=6.5 and l<=20.5):
                num=1509
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1510
            if(l>0.05 and l<1.5):
                num=1511
            if(l>=1.5 and l<3.5):
                num=1512
            if(l>=3.5 and l<6.5):
                num=1513
            if(l>=6.5 and l<=20.5):
                num=1514
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1515
            if(l>0.05 and l<1.5):
                num=1516
            if(l>=1.5 and l<3.5):
                num=1517
            if(l>=3.5 and l<6.5):
                num=1518
            if(l>=6.5 and l<=20.5):
                num=1519
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1520
            if(l>0.05 and l<1.5):
                num=1521
            if(l>=1.5 and l<3.5):
                num=1522
            if(l>=3.5 and l<6.5):
                num=1523
            if(l>=6.5 and l<=20.5):
                num=1524
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1525
            if(l>0.05 and l<1.5):
                num=1526
            if(l>=1.5 and l<3.5):
                num=1527
            if(l>=3.5 and l<6.5):
                num=1528
            if(l>=6.5 and l<=20.5):
                num=1529
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1530
            if(l>0.05 and l<1.5):
                num=1531
            if(l>=1.5 and l<3.5):
                num=1532
            if(l>=3.5 and l<6.5):
                num=1533
            if(l>=6.5 and l<=20.5):
                num=1534
        if(close>=7 and close<9.96):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1535
            if(l>0.05 and l<1.5):
                num=1536
            if(l>=1.5 and l<3.5):
                num=1537
            if(l>=3.5 and l<6.5):
                num=1538
            if(l>=6.5 and l<=20.5):
                num=1539
        if(close>=9.96 and close<=10.51):
            h,l=js(open,high,low,close)
            if(l>=0 and l<=0.05):
                num=1540
            if(l>0.05 and l<1.5):
                num=1541
            if(l>=1.5 and l<3.5):
                num=1542
            if(l>=3.5 and l<6.5):
                num=1543
            if(l>=6.5 and l<=20.5):
                num=1544
    return num



#tb000890 -7.602339181286544 8.771929824561411 -7.602339181286544 4.385964912280699


#print(bm(-7.602339181286544, 8.771929824561411, -7.602339181286544, 4.385964912280699))
