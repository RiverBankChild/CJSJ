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
                num=3
            if(h>=1.5 and h<3.5):
                num=4
            if(h>=3.5 and h<=20.5):
                num=6
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=8
            if(h>=1.5 and h<3.5):
                num=9
            if(h>=3.5 and h<=20.5):
                num=11
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=13
            if(h>=1.5 and h<3.5):
                num=14
            if(h>=3.5 and h<=20.5):
                num=16
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=18
            if(h>=1.5 and h<3.5):
                num=19
            if(h>=3.5 and h<=20.5):
                num=21
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=23
            if(h>=1.5 and h<3.5):
                num=24
            if(h>=3.5 and h<=20.5):
                num=26
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=28
            if(h>=1.5 and h<3.5):
                num=29
            if(h>=3.5 and h<=20.5):
                num=31
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=33
            if(h>=1.5 and h<3.5):
                num=34
            if(h>=3.5 and h<=20.5):
                num=36
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=38
            if(h>=1.5 and h<3.5):
                num=39
            if(h>=3.5 and h<=20.5):
                num=41
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=43
            if(h>=1.5 and h<3.5):
                num=44
            if(h>=3.5 and h<=20.5):
                num=44
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=47
            if(h>=1.5 and h<3.5):
                num=48
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            num=49





    if(open>-9.94 and open <-7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=51
            if(h>=1.5 and h<3.5):
                num=52
            if(h>=3.5 and h<=20.5):
                num=54
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=59
                if(l>=1.5 and l<3.5):
                    num=60
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=62
                if(l>=1.5 and l<3.5):
                    num=63
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=68
                if(l>=1.5 and l<3.5):
                    num=69
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=74
                if(l>=1.5 and l<3.5):
                    num=75
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=77
                if(l>=1.5 and l<3.5):
                    num=78
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=83
                if(l>=1.5 and l<3.5):
                    num=84
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=89
                if(l>=1.5 and l<3.5):
                    num=90
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=92
                if(l>=1.5 and l<3.5):
                    num=93
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=98
                if(l>=1.5 and l<3.5):
                    num=99
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=104
                if(l>=1.5 and l<3.5):
                    num=105
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=107
                if(l>=1.5 and l<3.5):
                    num=108
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=113
                if(l>=1.5 and l<3.5):
                    num=114
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=119
                if(l>=1.5 and l<3.5):
                    num=120
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=122
                if(l>=1.5 and l<3.5):
                    num=123
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=128
                if(l>=1.5 and l<3.5):
                    num=129
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=134
                if(l>=1.5 and l<3.5):
                    num=135
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=137
                if(l>=1.5 and l<3.5):
                    num=138
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=143
                if(l>=1.5 and l<3.5):
                    num=144
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=149
                if(l>=1.5 and l<3.5):
                    num=150
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=152
                if(l>=1.5 and l<3.5):
                    num=153
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=158
                if(l>=1.5 and l<3.5):
                    num=159
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=164
                if(l>=1.5 and l<3.5):
                    num=165
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=167
                if(l>=1.5 and l<3.5):
                    num=168
        if(close>=4 and close<7):
            print("s")
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=176
                if(l>=1.5 and l<3.5):
                    num=177
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=179
                if(l>=1.5 and l<3.5):
                    num=180
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=179
                if(l>=1.5 and l<3.5):
                    num=180
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=185
                if(l>=1.5 and l<3.5):
                    num=186
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=188
                if(l>=1.5 and l<3.5):
                    num=189
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=191
            if(l>=1.5 and l<3.5):
                num=193



    if(open>=-7 and open <-3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=195            
            if(h>=1.5 and h<3.5):
                num=196
            if(h>=3.5 and h<=20.5):
                num=198
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=203
                if(l>=1.5 and l<3.5):
                    num=204
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=206
                if(l>=1.5 and l<3.5):
                    num=207
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=212
                if(l>=1.5 and l<3.5):
                    num=213
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=219
                if(l>=1.5 and l<3.5):
                    num=220
            if(l>=3.5 and l<20.5):
                    num=221
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=223
                if(l>=1.5 and l<3.5):
                    num=224
            if(l>=3.5 and l<20.5):
                    num=225
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=231
                if(l>=1.5 and l<3.5):
                    num=232
            if(l>=3.5 and l<20.5):
                    num=233
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=240
                if(l>=1.5 and l<3.5):
                    num=241
                if(l>=3.5 and l<=20.5):
                    num=243
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=245
                if(l>=1.5 and l<3.5):
                    num=246
                if(l>=3.5 and l<=20.5):
                    num=248
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=255
                if(l>=1.5 and l<3.5):
                    num=256
                if(l>=3.5 and l<=20.5):
                    num=258
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=265
                if(l>=1.5 and l<3.5):
                    num=266
                if(l>=3.5 and l<=20.5):
                    num=268
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=270
                if(l>=1.5 and l<3.5):
                    num=271
                if(l>=3.5 and l<=20.5):
                    num=273
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=280
                if(l>=1.5 and l<3.5):
                    num=281
                if(l>=3.5 and l<=20.5):
                    num=283
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=290
                if(l>=1.5 and l<3.5):
                    num=291
                if(l>=3.5 and l<=20.5):
                    num=293
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=295
                if(l>=1.5 and l<3.5):
                    num=296
                if(l>=3.5 and l<=20.5):
                    num=298
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=305
                if(l>=1.5 and l<3.5):
                    num=306
                if(l>=3.5 and l<=20.5):
                    num=308
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=315
                if(l>=1.5 and l<3.5):
                    num=316
                if(l>=3.5 and l<=20.5):
                    num=318
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=320
                if(l>=1.5 and l<3.5):
                    num=321
                if(l>=3.5 and l<=20.5):
                    num=323
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=330
                if(l>=1.5 and l<3.5):
                    num=331
                if(l>=3.5 and l<=20.5):
                    num=333
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=340
                if(l>=1.5 and l<3.5):
                    num=341
                if(l>=3.5 and l<=20.5):
                    num=343
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=345
                if(l>=1.5 and l<3.5):
                    num=346
                if(l>=3.5 and l<=20.5):
                    num=348
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=355
                if(l>=1.5 and l<3.5):
                    num=356
                if(l>=3.5 and l<=20.5):
                    num=358
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=365
                if(l>=1.5 and l<3.5):
                    num=366
                if(l>=3.5 and l<=20.5):
                    num=368
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=370
                if(l>=1.5 and l<3.5):
                    num=371
                if(l>=3.5 and l<=20.5):
                    num=372
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=379
                if(l>=1.5 and l<3.5):
                    num=380
                if(l>=3.5 and l<=20.5):
                    num=382
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=389
                if(l>=1.5 and l<3.5):
                    num=390
                if(l>=3.5 and l<=20.5):
                    num=392
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=394
                if(l>=1.5 and l<3.5):
                    num=395
                if(l>=3.5 and l<=20.5):
                    num=397
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=394
                if(l>=1.5 and l<3.5):
                    num=395
                if(l>=3.5 and l<=20.5):
                    num=397
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=409
                if(l>=1.5 and l<3.5):
                    num=410
                if(l>=3.5 and l<=20.5):
                    num=412
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=414
                if(l>=1.5 and l<3.5):
                    num=415
                if(l>=3.5 and l<=20.5):
                    num=417
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=419
            if(l>=1.5 and l<3.5):
                num=420
            if(l>=3.5 and l<=20.5):
                num=422




    if(open>=-3 and open <-1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=424
            if(h>=1.5 and h<3.5):
                num=425
            if(h>=3.5 and h<=20.5):
                num=427
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=432
                if(l>=1.5 and l<3.5):
                    num=433
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=435
                if(l>=1.5 and l<3.5):
                    num=436
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=441
                if(l>=1.5 and l<3.5):
                    num=442
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=448
                if(l>=1.5 and l<3.5):
                    num=449
            if(l>=3.5 and l<20.5):
                    num=450
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=452
                if(l>=1.5 and l<3.5):
                    num=453
            if(l>=3.5 and l<20.5):
                    num=454
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=460
                if(l>=1.5 and l<3.5):
                    num=461
            if(l>=3.5 and l<20.5):
                    num=462
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=469
                if(l>=1.5 and l<3.5):
                    num=470
                if(l>=3.5 and l<=20.5):
                    num=472
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=474
                if(l>=1.5 and l<3.5):
                    num=475
                if(l>=3.5 and l<=20.5):
                    num=477
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=484
                if(l>=1.5 and l<3.5):
                    num=485
                if(l>=3.5 and l<=20.5):
                    num=487
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=494
                if(l>=1.5 and l<3.5):
                    num=495
                if(l>=3.5 and l<=20.5):
                    num=497
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=499
                if(l>=1.5 and l<3.5):
                    num=500
                if(l>=3.5 and l<=20.5):
                    num=502
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=509
                if(l>=1.5 and l<3.5):
                    num=510
                if(l>=3.5 and l<=20.5):
                    num=512
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=519
                if(l>=1.5 and l<3.5):
                    num=520
                if(l>=3.5 and l<=20.5):
                    num=522
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=524
                if(l>=1.5 and l<3.5):
                    num=525
                if(l>=3.5 and l<=20.5):
                    num=527
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=534
                if(l>=1.5 and l<3.5):
                    num=535
                if(l>=3.5 and l<=20.5):
                    num=537
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=544
                if(l>=1.5 and l<3.5):
                    num=545
                if(l>=3.5 and l<=20.5):
                    num=547
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=549
                if(l>=1.5 and l<3.5):
                    num=550
                if(l>=3.5 and l<=20.5):
                    num=552
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=559
                if(l>=1.5 and l<3.5):
                    num=560
                if(l>=3.5 and l<=20.5):
                    num=562
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=569
                if(l>=1.5 and l<3.5):
                    num=570
                if(l>=3.5 and l<=20.5):
                    num=572
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=574
                if(l>=1.5 and l<3.5):
                    num=575
                if(l>=3.5 and l<=20.5):
                    num=577
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=584
                if(l>=1.5 and l<3.5):
                    num=585
                if(l>=3.5 and l<=20.5):
                    num=587
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=594
                if(l>=1.5 and l<3.5):
                    num=595
                if(l>=3.5 and l<=20.5):
                    num=597
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=599
                if(l>=1.5 and l<3.5):
                    num=600
                if(l>=3.5 and l<=20.5):
                    num=602
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=609
                if(l>=1.5 and l<3.5):
                    num=610
                if(l>=3.5 and l<=20.5):
                    num=612
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=619
                if(l>=1.5 and l<3.5):
                    num=620
                if(l>=3.5 and l<=20.5):
                    num=622
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=624
                if(l>=1.5 and l<3.5):
                    num=625
                if(l>=3.5 and l<=20.5):
                    num=627
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=624
                if(l>=1.5 and l<3.5):
                    num=625
                if(l>=3.5 and l<=20.5):
                    num=627
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=639
                if(l>=1.5 and l<3.5):
                    num=640
                if(l>=3.5 and l<=20.5):
                    num=642
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=644
                if(l>=1.5 and l<3.5):
                    num=645
                if(l>=3.5 and l<=20.5):
                    num=647
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=649
            if(l>=1.5 and l<3.5):
                num=650
            if(l>=3.5 and l<=20.5):
                num=652



    if(open>=-1 and open <1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=354
            if(h>=1.5 and h<3.5):
                num=655
            if(h>=3.5 and h<=20.5):
                num=657
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=662
                if(l>=1.5 and l<3.5):
                    num=663
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=665
                if(l>=1.5 and l<3.5):
                    num=666
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=671
                if(l>=1.5 and l<3.5):
                    num=672
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=678
                if(l>=1.5 and l<3.5):
                    num=679
            if(l>=3.5 and l<20.5):
                    num=680
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=682
                if(l>=1.5 and l<3.5):
                    num=683
            if(l>=3.5 and l<20.5):
                    num=684
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=690
                if(l>=1.5 and l<3.5):
                    num=691
            if(l>=3.5 and l<20.5):
                    num=692
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=699
                if(l>=1.5 and l<3.5):
                    num=700
                if(l>=3.5 and l<=20.5):
                    num=702
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=704
                if(l>=1.5 and l<3.5):
                    num=705
                if(l>=3.5 and l<=20.5):
                    num=707
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=714
                if(l>=1.5 and l<3.5):
                    num=715
                if(l>=3.5 and l<=20.5):
                    num=717
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=724
                if(l>=1.5 and l<3.5):
                    num=725
                if(l>=3.5 and l<=20.5):
                    num=727
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=729
                if(l>=1.5 and l<3.5):
                    num=730
                if(l>=3.5 and l<=20.5):
                    num=732
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=739
                if(l>=1.5 and l<3.5):
                    num=740
                if(l>=3.5 and l<=20.5):
                    num=742
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=749
                if(l>=1.5 and l<3.5):
                    num=750
                if(l>=3.5 and l<=20.5):
                    num=752
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=754
                if(l>=1.5 and l<3.5):
                    num=755
                if(l>=3.5 and l<=20.5):
                    num=757
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=764
                if(l>=1.5 and l<3.5):
                    num=765
                if(l>=3.5 and l<=20.5):
                    num=767
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=774
                if(l>=1.5 and l<3.5):
                    num=775
                if(l>=3.5 and l<=20.5):
                    num=777
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=779
                if(l>=1.5 and l<3.5):
                    num=780
                if(l>=3.5 and l<=20.5):
                    num=782
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=789
                if(l>=1.5 and l<3.5):
                    num=790
                if(l>=3.5 and l<=20.5):
                    num=792
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=799
                if(l>=1.5 and l<3.5):
                    num=800
                if(l>=3.5 and l<=20.5):
                    num=802
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=804
                if(l>=1.5 and l<3.5):
                    num=805
                if(l>=3.5 and l<=20.5):
                    num=807
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=814
                if(l>=1.5 and l<3.5):
                    num=815
                if(l>=3.5 and l<=20.5):
                    num=817
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=824
                if(l>=1.5 and l<3.5):
                    num=825
                if(l>=3.5 and l<=20.5):
                    num=827
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=829
                if(l>=1.5 and l<3.5):
                    num=830
                if(l>=3.5 and l<=20.5):
                    num=832
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=839
                if(l>=1.5 and l<3.5):
                    num=840
                if(l>=3.5 and l<=20.5):
                    num=842
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=849
                if(l>=1.5 and l<3.5):
                    num=850
                if(l>=3.5 and l<=20.5):
                    num=852
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=854
                if(l>=1.5 and l<3.5):
                    num=855
                if(l>=3.5 and l<=20.5):
                    num=857
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=854
                if(l>=1.5 and l<3.5):
                    num=855
                if(l>=3.5 and l<=20.5):
                    num=857
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=869
                if(l>=1.5 and l<3.5):
                    num=870
                if(l>=3.5 and l<=20.5):
                    num=872
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=874
                if(l>=1.5 and l<3.5):
                    num=875
                if(l>=3.5 and l<=20.5):
                    num=877
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=879
            if(l>=1.5 and l<3.5):
                num=880
            if(l>=3.5 and l<=20.5):
                num=882


    if(open>=1 and open <3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=884
            if(h>=1.5 and h<3.5):
                num=885
            if(h>=3.5 and h<=20.5):
                num=887
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=892
                if(l>=1.5 and l<3.5):
                    num=893
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=895
                if(l>=1.5 and l<3.5):
                    num=896
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=901
                if(l>=1.5 and l<3.5):
                    num=902
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=908
                if(l>=1.5 and l<3.5):
                    num=909
            if(l>=3.5 and l<20.5):
                    num=910
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=912
                if(l>=1.5 and l<3.5):
                    num=913
            if(l>=3.5 and l<20.5):
                    num=914
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=920
                if(l>=1.5 and l<3.5):
                    num=921
            if(l>=3.5 and l<20.5):
                    num=922
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=929
                if(l>=1.5 and l<3.5):
                    num=930
                if(l>=3.5 and l<=20.5):
                    num=932
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=934
                if(l>=1.5 and l<3.5):
                    num=935
                if(l>=3.5 and l<=20.5):
                    num=937
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=944
                if(l>=1.5 and l<3.5):
                    num=945
                if(l>=3.5 and l<=20.5):
                    num=947
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=954
                if(l>=1.5 and l<3.5):
                    num=955
                if(l>=3.5 and l<=20.5):
                    num=957
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=959
                if(l>=1.5 and l<3.5):
                    num=960
                if(l>=3.5 and l<=20.5):
                    num=962
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=969
                if(l>=1.5 and l<3.5):
                    num=970
                if(l>=3.5 and l<=20.5):
                    num=972
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=979
                if(l>=1.5 and l<3.5):
                    num=980
                if(l>=3.5 and l<=20.5):
                    num=982
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=984
                if(l>=1.5 and l<3.5):
                    num=985
                if(l>=3.5 and l<=20.5):
                    num=987
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=994
                if(l>=1.5 and l<3.5):
                    num=995
                if(l>=3.5 and l<=20.5):
                    num=997
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1004
                if(l>=1.5 and l<3.5):
                    num=1005
                if(l>=3.5 and l<=20.5):
                    num=1007
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1009
                if(l>=1.5 and l<3.5):
                    num=1010
                if(l>=3.5 and l<=20.5):
                    num=1012
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1019
                if(l>=1.5 and l<3.5):
                    num=1020
                if(l>=3.5 and l<=20.5):
                    num=1022
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1029
                if(l>=1.5 and l<3.5):
                    num=1030
                if(l>=3.5 and l<=20.5):
                    num=1032
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1034
                if(l>=1.5 and l<3.5):
                    num=1035
                if(l>=3.5 and l<=20.5):
                    num=1037
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1044
                if(l>=1.5 and l<3.5):
                    num=1045
                if(l>=3.5 and l<=20.5):
                    num=1047
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1054
                if(l>=1.5 and l<3.5):
                    num=1055
                if(l>=3.5 and l<=20.5):
                    num=1057
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1059
                if(l>=1.5 and l<3.5):
                    num=1060
                if(l>=3.5 and l<=20.5):
                    num=1062
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1069
                if(l>=1.5 and l<3.5):
                    num=1070
                if(l>=3.5 and l<=20.5):
                    num=1072
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1079
                if(l>=1.5 and l<3.5):
                    num=1080
                if(l>=3.5 and l<=20.5):
                    num=1082
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1084
                if(l>=1.5 and l<3.5):
                    num=1085
                if(l>=3.5 and l<=20.5):
                    num=1087
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1099
                if(l>=1.5 and l<3.5):
                    num=1100
                if(l>=3.5 and l<=20.5):
                    num=1102
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1104
                if(l>=1.5 and l<3.5):
                    num=1105
                if(l>=3.5 and l<=20.5):
                    num=1107
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1109
            if(l>=1.5 and l<3.5):
                num=1110
            if(l>=3.5 and l<=20.5):
                num=1112




    if(open>=3 and open <7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=1114
            if(h>=1.5 and h<3.5):
                num=1115
            if(h>=3.5 and h<=20.5):
                num=1117
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1122
                if(l>=1.5 and l<3.5):
                    num=1123
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1125
                if(l>=1.5 and l<3.5):
                    num=1126
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1131
                if(l>=1.5 and l<3.5):
                    num=1132
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1138
                if(l>=1.5 and l<3.5):
                    num=1139
                if(l>=3.5 and l<20.5):
                    num=1140
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1142
                if(l>=1.5 and l<3.5):
                    num=1143
                if(l>=3.5 and l<20.5):
                    num=1144
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1150
                if(l>=1.5 and l<3.5):
                    num=1151
                if(l>=3.5 and l<20.5):
                    num=1152
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1159
                if(l>=1.5 and l<3.5):
                    num=1160
                if(l>=3.5 and l<=20.5):
                    num=1162
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1164
                if(l>=1.5 and l<3.5):
                    num=1165
                if(l>=3.5 and l<=20.5):
                    num=1167
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1174
                if(l>=1.5 and l<3.5):
                    num=1175
                if(l>=3.5 and l<=20.5):
                    num=1177
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1184
                if(l>=1.5 and l<3.5):
                    num=1185
                if(l>=3.5 and l<=20.5):
                    num=1187
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1189
                if(l>=1.5 and l<3.5):
                    num=1190
                if(l>=3.5 and l<=20.5):
                    num=1192
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1199
                if(l>=1.5 and l<3.5):
                    num=1200
                if(l>=3.5 and l<=20.5):
                    num=1202
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1209
                if(l>=1.5 and l<3.5):
                    num=1210
                if(l>=3.5 and l<=20.5):
                    num=1212
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1214
                if(l>=1.5 and l<3.5):
                    num=1215
                if(l>=3.5 and l<=20.5):
                    num=1217
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1224
                if(l>=1.5 and l<3.5):
                    num=1225
                if(l>=3.5 and l<=20.5):
                    num=1227
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1234
                if(l>=1.5 and l<3.5):
                    num=1235
                if(l>=3.5 and l<=20.5):
                    num=1237
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1239
                if(l>=1.5 and l<3.5):
                    num=1240
                if(l>=3.5 and l<=20.5):
                    num=1242
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1249
                if(l>=1.5 and l<3.5):
                    num=1250
                if(l>=3.5 and l<=20.5):
                    num=1252
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1259
                if(l>=1.5 and l<3.5):
                    num=1260
                if(l>=3.5 and l<=20.5):
                    num=1262
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1264
                if(l>=1.5 and l<3.5):
                    num=1265
                if(l>=3.5 and l<=20.5):
                    num=1267
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1274
                if(l>=1.5 and l<3.5):
                    num=1275
                if(l>=3.5 and l<=20.5):
                    num=1277
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1284
                if(l>=1.5 and l<3.5):
                    num=1285
                if(l>=3.5 and l<=20.5):
                    num=1287
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1289
                if(l>=1.5 and l<3.5):
                    num=1290
                if(l>=3.5 and l<=20.5):
                    num=1292
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1299
                if(l>=1.5 and l<3.5):
                    num=1300
                if(l>=3.5 and l<=20.5):
                    num=1302
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1309
                if(l>=1.5 and l<3.5):
                    num=1310
                if(l>=3.5 and l<=20.5):
                    num=1312
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1314
                if(l>=1.5 and l<3.5):
                    num=1315
                if(l>=3.5 and l<=20.5):
                    num=1317
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=1314
                if(l>=1.5 and l<3.5):
                    num=1315
                if(l>=3.5 and l<=20.5):
                    num=1317
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1329
                if(l>=1.5 and l<3.5):
                    num=1330
                if(l>=3.5 and l<=20.5):
                    num=1332
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1334
                if(l>=1.5 and l<3.5):
                    num=1335
                if(l>=3.5 and l<=20.5):
                    num=1337
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1339
            if(l>=1.5 and l<3.5):
                num=1340
            if(l>=3.5 and l<=20.5):
                num=1342



    if(open>=7 and open <9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=1344
            if(h>=1.5 and h<3.5):
                num=1345
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1350
                if(l>=1.5 and l<3.5):
                    num=1351
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1353
                if(l>=1.5 and l<3.5):
                    num=1354
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1360
                if(l>=1.5 and l<3.5):
                    num=1361
                if(l>=3.5 and l<20.5):
                    num=1362
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1364
                if(l>=1.5 and l<3.5):
                    num=1365
                if(l>=3.5 and l<20.5):
                    num=1366
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1373
                if(l>=1.5 and l<3.5):
                    num=1374
                if(l>=3.5 and l<=20.5):
                    num=1376
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1378
                if(l>=1.5 and l<3.5):
                    num=1379
                if(l>=3.5 and l<=20.5):
                    num=1381
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1388
                if(l>=1.5 and l<3.5):
                    num=1389
                if(l>=3.5 and l<=20.5):
                    num=1391
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1393
                if(l>=1.5 and l<3.5):
                    num=1394
                if(l>=3.5 and l<=20.5):
                    num=1396
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1403
                if(l>=1.5 and l<3.5):
                    num=1404
                if(l>=3.5 and l<=20.5):
                    num=1406
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1408
                if(l>=1.5 and l<3.5):
                    num=1409
                if(l>=3.5 and l<=20.5):
                    num=1411
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1418
                if(l>=1.5 and l<3.5):
                    num=1419
                if(l>=3.5 and l<=20.5):
                    num=1421
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1423
                if(l>=1.5 and l<3.5):
                    num=1424
                if(l>=3.5 and l<=20.5):
                    num=1426
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1433
                if(l>=1.5 and l<3.5):
                    num=1434
                if(l>=3.5 and l<=20.5):
                    num=1436
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1438
                if(l>=1.5 and l<3.5):
                    num=1439
                if(l>=3.5 and l<=20.5):
                    num=1441
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1448
                if(l>=1.5 and l<3.5):
                    num=1449
                if(l>=3.5 and l<=20.5):
                    num=1451
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1453
                if(l>=1.5 and l<3.5):
                    num=1454
                if(l>=3.5 and l<=20.5):
                    num=1456
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1463
                if(l>=1.5 and l<3.5):
                    num=1464
                if(l>=3.5 and l<=20.5):
                    num=1466
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1468
                if(l>=1.5 and l<3.5):
                    num=1469
                if(l>=3.5 and l<=20.5):
                    num=1471
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=1478
                if(l>=1.5 and l<3.5):
                    num=1479
                if(l>=3.5 and l<=20.5):
                    num=1481
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=1483
                if(l>=1.5 and l<3.5):
                    num=1484
                if(l>=3.5 and l<=20.5):
                    num=1486
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1488
            if(l>=1.5 and l<3.5):
                num=1489
            if(l>=3.5 and l<=20.5):
                num=1491



    if(open>=9.94 and open <=10.6):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            num=1492
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1494
            if(l>=1.5 and l<3.5):
                num=1495
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1497
            if(l>=1.5 and l<3.5):
                num=1498
            if(l>=3.5 and l<20.5):
                num=1499
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1501
            if(l>=1.5 and l<3.5):
                num=1502
            if(l>=3.5 and l<=20.5):
                num=1504
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1506
            if(l>=1.5 and l<3.5):
                num=1507
            if(l>=3.5 and l<=20.5):
                num=1509
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1511
            if(l>=1.5 and l<3.5):
                num=1512
            if(l>=3.5 and l<=20.5):
                num=1514
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1516
            if(l>=1.5 and l<3.5):
                num=1517
            if(l>=3.5 and l<=20.5):
                num=1519
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1521
            if(l>=1.5 and l<3.5):
                num=1522
            if(l>=3.5 and l<=20.5):
                num=1524
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1526
            if(l>=1.5 and l<3.5):
                num=1527
            if(l>=3.5 and l<=20.5):
                num=1529
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1531
            if(l>=1.5 and l<3.5):
                num=1532
            if(l>=3.5 and l<=20.5):
                num=1534
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1536
            if(l>=1.5 and l<3.5):
                num=1537
            if(l>=3.5 and l<=20.5):
                num=1539
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=1541
            if(l>=1.5 and l<3.5):
                num=1542
            if(l>=3.5 and l<=20.5):
                num=1544
    return num


