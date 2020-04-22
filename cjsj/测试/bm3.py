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

    if(open>=-10.6 and open<=-9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-1.0
            if(h>=1.5 and h<3.5):
                num=-0.99688476
            if(h>=3.5 and h<=20.5):
                num=-0.9937695
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.9906543
            if(h>=1.5 and h<3.5):
                num=-0.98753905
            if(h>=3.5 and h<=20.5):
                num=-0.9844238
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.9813086
            if(h>=1.5 and h<3.5):
                num=-0.97819334
            if(h>=3.5 and h<=20.5):
                num=-0.9750781
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.97196287
            if(h>=1.5 and h<3.5):
                num=-0.96884763
            if(h>=3.5 and h<=20.5):
                num=-0.9657324
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.96261716
            if(h>=1.5 and h<3.5):
                num=-0.9595019
            if(h>=3.5 and h<=20.5):
                num=-0.9563867
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.95327145
            if(h>=1.5 and h<3.5):
                num=-0.9501562
            if(h>=3.5 and h<=20.5):
                num=-0.947041
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.94392574
            if(h>=1.5 and h<3.5):
                num=-0.9408105
            if(h>=3.5 and h<=20.5):
                num=-0.93769526
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.93458
            if(h>=1.5 and h<3.5):
                num=-0.9314648
            if(h>=3.5 and h<=20.5):
                num=-0.92834955
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.9252343
            if(h>=1.5 and h<3.5):
                num=-0.9221191
            if(h>=3.5 and h<=20.5):
                num=-0.91900384
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.9158886
            if(h>=1.5 and h<3.5):
                num=-0.9127734
            if(h>=3.5 and h<=20.5):
                num=-0.90965813
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.9065429
            if(h>=1.5 and h<3.5):
                num=-0.90342766
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            num=-0.9003124





    if(open>-9.94 and open<-7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.8971972
            if(h>=1.5 and h<3.5):
                num=-0.89408195
            if(h>=3.5 and h<=20.5):
                num=-0.8909667
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.8878515
                if(l>=1.5 and l<3.5):
                    num=-0.88473624
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.881621
                if(l>=1.5 and l<3.5):
                    num=-0.87850577
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.8753905
                if(l>=1.5 and l<3.5):
                    num=-0.8722753
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.86916006
                if(l>=1.5 and l<3.5):
                    num=-0.8660448
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.8629296
                if(l>=1.5 and l<3.5):
                    num=-0.85981435
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.8566991
                if(l>=1.5 and l<3.5):
                    num=-0.8535839
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.85046864
                if(l>=1.5 and l<3.5):
                    num=-0.8473534
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.84423816
                if(l>=1.5 and l<3.5):
                    num=-0.8411229
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.8380077
                if(l>=1.5 and l<3.5):
                    num=-0.83489245
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.8317772
                if(l>=1.5 and l<3.5):
                    num=-0.828662
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.82554674
                if(l>=1.5 and l<3.5):
                    num=-0.8224315
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.81931627
                if(l>=1.5 and l<3.5):
                    num=-0.81620103
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.8130858
                if(l>=1.5 and l<3.5):
                    num=-0.80997056
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.8068553
                if(l>=1.5 and l<3.5):
                    num=-0.8037401
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.80062485
                if(l>=1.5 and l<3.5):
                    num=-0.7975096
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.7943944
                if(l>=1.5 and l<3.5):
                    num=-0.79127914
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.7881639
                if(l>=1.5 and l<3.5):
                    num=-0.78504866
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.7819334
                if(l>=1.5 and l<3.5):
                    num=-0.7788182
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.77570295
                if(l>=1.5 and l<3.5):
                    num=-0.7725877
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.7694725
                if(l>=1.5 and l<3.5):
                    num=-0.76635724
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.763242
                if(l>=1.5 and l<3.5):
                    num=-0.76012677
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.75701153
                if(l>=1.5 and l<3.5):
                    num=-0.7538963
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.75078106
                if(l>=1.5 and l<3.5):
                    num=-0.7476658
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.7445506
                if(l>=1.5 and l<3.5):
                    num=-0.74143535
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.7383201
                if(l>=1.5 and l<3.5):
                    num=-0.7352049
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.73208964
                if(l>=1.5 and l<3.5):
                    num=-0.7289744
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.72585917
                if(l>=1.5 and l<3.5):
                    num=-0.7227439
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.7196287
                if(l>=1.5 and l<3.5):
                    num=-0.71651345
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.7133982
                if(l>=1.5 and l<3.5):
                    num=-0.710283
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=-0.70716774
            if(l>=1.5 and l<3.5):
                num=-0.7040525



    if(open>=-7 and open<-3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.7009373
            if(h>=1.5 and h<3.5):
                num=-0.69782203
            if(h>=3.5 and h<=20.5):
                num=-0.6947068
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.69159156
                if(l>=1.5 and l<3.5):
                    num=-0.6884763
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.6853611
                if(l>=1.5 and l<3.5):
                    num=-0.68224585
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.6791306
                if(l>=1.5 and l<3.5):
                    num=-0.6760154
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.67290014
                if(l>=1.5 and l<3.5):
                    num=-0.6697849
                if(l>=3.5 and l<20.5):
                    num=-0.66666967
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.66355443
                if(l>=1.5 and l<3.5):
                    num=-0.6604392
                if(l>=3.5 and l<20.5):
                    num=-0.65732396
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.6542087
                if(l>=1.5 and l<3.5):
                    num=-0.6510935
                if(l>=3.5 and l<20.5):
                    num=-0.64797825
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.644863
                if(l>=1.5 and l<3.5):
                    num=-0.6417478
                if(l>=3.5 and l<=20.5):
                    num=-0.63863254
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.6355173
                if(l>=1.5 and l<3.5):
                    num=-0.63240206
                if(l>=3.5 and l<=20.5):
                    num=-0.6292868
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.6261716
                if(l>=1.5 and l<3.5):
                    num=-0.62305635
                if(l>=3.5 and l<=20.5):
                    num=-0.6199411
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.6168259
                if(l>=1.5 and l<3.5):
                    num=-0.61371064
                if(l>=3.5 and l<=20.5):
                    num=-0.6105954
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.60748017
                if(l>=1.5 and l<3.5):
                    num=-0.60436493
                if(l>=3.5 and l<=20.5):
                    num=-0.6012497
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.59813446
                if(l>=1.5 and l<3.5):
                    num=-0.5950192
                if(l>=3.5 and l<=20.5):
                    num=-0.591904
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.58878875
                if(l>=1.5 and l<3.5):
                    num=-0.5856735
                if(l>=3.5 and l<=20.5):
                    num=-0.5825583
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.57944304
                if(l>=1.5 and l<3.5):
                    num=-0.5763278
                if(l>=3.5 and l<=20.5):
                    num=-0.57321256
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.5700973
                if(l>=1.5 and l<3.5):
                    num=-0.5669821
                if(l>=3.5 and l<=20.5):
                    num=-0.56386685
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.5607516
                if(l>=1.5 and l<3.5):
                    num=-0.5576364
                if(l>=3.5 and l<=20.5):
                    num=-0.55452114
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.5514059
                if(l>=1.5 and l<3.5):
                    num=-0.54829067
                if(l>=3.5 and l<=20.5):
                    num=-0.54517543
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.5420602
                if(l>=1.5 and l<3.5):
                    num=-0.53894496
                if(l>=3.5 and l<=20.5):
                    num=-0.5358297
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.5327145
                if(l>=1.5 and l<3.5):
                    num=-0.52959925
                if(l>=3.5 and l<=20.5):
                    num=-0.526484
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.5233688
                if(l>=1.5 and l<3.5):
                    num=-0.52025354
                if(l>=3.5 and l<=20.5):
                    num=-0.5171383
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.51402307
                if(l>=1.5 and l<3.5):
                    num=-0.5109078
                if(l>=3.5 and l<=20.5):
                    num=-0.5077926
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.50467736
                if(l>=1.5 and l<3.5):
                    num=-0.5015621
                if(l>=3.5 and l<=20.5):
                    num=-0.49844685
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.4953316
                if(l>=1.5 and l<3.5):
                    num=-0.49221632
                if(l>=3.5 and l<=20.5):
                    num=-0.48910105
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.4859858
                if(l>=1.5 and l<3.5):
                    num=-0.48287052
                if(l>=3.5 and l<=20.5):
                    num=-0.47975525
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.47664
                if(l>=1.5 and l<3.5):
                    num=-0.47352472
                if(l>=3.5 and l<=20.5):
                    num=-0.47040945
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.4672942
                if(l>=1.5 and l<3.5):
                    num=-0.46417892
                if(l>=3.5 and l<=20.5):
                    num=-0.46106365
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.4579484
                if(l>=1.5 and l<3.5):
                    num=-0.45483312
                if(l>=3.5 and l<=20.5):
                    num=-0.45171785
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.4486026
                if(l>=1.5 and l<3.5):
                    num=-0.44548732
                if(l>=3.5 and l<=20.5):
                    num=-0.44237205
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.4392568
                if(l>=1.5 and l<3.5):
                    num=-0.43614152
                if(l>=3.5 and l<=20.5):
                    num=-0.43302625
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=-0.429911
            if(l>=1.5 and l<3.5):
                num=-0.42679572
            if(l>=3.5 and l<=20.5):
                num=-0.42368045




    if(open>=-3 and open<-1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.4205652
            if(h>=1.5 and h<3.5):
                num=-0.41744992
            if(h>=3.5 and h<=20.5):
                num=-0.41433465
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.4112194
                if(l>=1.5 and l<3.5):
                    num=-0.40810412
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.40498886
                if(l>=1.5 and l<3.5):
                    num=-0.4018736
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.39875832
                if(l>=1.5 and l<3.5):
                    num=-0.39564306
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.3925278
                if(l>=1.5 and l<3.5):
                    num=-0.38941252
                if(l>=3.5 and l<20.5):
                    num=-0.38629726
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.383182
                if(l>=1.5 and l<3.5):
                    num=-0.38006672
                if(l>=3.5 and l<20.5):
                    num=-0.37695146
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.3738362
                if(l>=1.5 and l<3.5):
                    num=-0.37072092
                if(l>=3.5 and l<20.5):
                    num=-0.36760566
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.3644904
                if(l>=1.5 and l<3.5):
                    num=-0.36137512
                if(l>=3.5 and l<=20.5):
                    num=-0.35825986
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.3551446
                if(l>=1.5 and l<3.5):
                    num=-0.35202932
                if(l>=3.5 and l<=20.5):
                    num=-0.34891406
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.3457988
                if(l>=1.5 and l<3.5):
                    num=-0.34268352
                if(l>=3.5 and l<=20.5):
                    num=-0.33956826
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.336453
                if(l>=1.5 and l<3.5):
                    num=-0.33333772
                if(l>=3.5 and l<=20.5):
                    num=-0.33022246
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.3271072
                if(l>=1.5 and l<3.5):
                    num=-0.32399192
                if(l>=3.5 and l<=20.5):
                    num=-0.32087666
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.3177614
                if(l>=1.5 and l<3.5):
                    num=-0.31464612
                if(l>=3.5 and l<=20.5):
                    num=-0.31153086
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.3084156
                if(l>=1.5 and l<3.5):
                    num=-0.30530033
                if(l>=3.5 and l<=20.5):
                    num=-0.30218506
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.2990698
                if(l>=1.5 and l<3.5):
                    num=-0.29595453
                if(l>=3.5 and l<=20.5):
                    num=-0.29283926
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.289724
                if(l>=1.5 and l<3.5):
                    num=-0.28660873
                if(l>=3.5 and l<=20.5):
                    num=-0.28349346
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.2803782
                if(l>=1.5 and l<3.5):
                    num=-0.27726293
                if(l>=3.5 and l<=20.5):
                    num=-0.27414766
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.2710324
                if(l>=1.5 and l<3.5):
                    num=-0.26791713
                if(l>=3.5 and l<=20.5):
                    num=-0.26480186
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.2616866
                if(l>=1.5 and l<3.5):
                    num=-0.25857133
                if(l>=3.5 and l<=20.5):
                    num=-0.25545606
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.2523408
                if(l>=1.5 and l<3.5):
                    num=-0.24922553
                if(l>=3.5 and l<=20.5):
                    num=-0.24611026
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.242995
                if(l>=1.5 and l<3.5):
                    num=-0.23987973
                if(l>=3.5 and l<=20.5):
                    num=-0.23676446
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.2336492
                if(l>=1.5 and l<3.5):
                    num=-0.23053393
                if(l>=3.5 and l<=20.5):
                    num=-0.22741866
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.2243034
                if(l>=1.5 and l<3.5):
                    num=-0.22118813
                if(l>=3.5 and l<=20.5):
                    num=-0.21807286
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.2149576
                if(l>=1.5 and l<3.5):
                    num=-0.21184233
                if(l>=3.5 and l<=20.5):
                    num=-0.20872706
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.2056118
                if(l>=1.5 and l<3.5):
                    num=-0.20249653
                if(l>=3.5 and l<=20.5):
                    num=-0.19938126
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.196266
                if(l>=1.5 and l<3.5):
                    num=-0.19315073
                if(l>=3.5 and l<=20.5):
                    num=-0.19003546
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.1869202
                if(l>=1.5 and l<3.5):
                    num=-0.18380493
                if(l>=3.5 and l<=20.5):
                    num=-0.18068966
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.1775744
                if(l>=1.5 and l<3.5):
                    num=-0.17445913
                if(l>=3.5 and l<=20.5):
                    num=-0.17134386
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.1682286
                if(l>=1.5 and l<3.5):
                    num=-0.16511333
                if(l>=3.5 and l<=20.5):
                    num=-0.16199806
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.1588828
                if(l>=1.5 and l<3.5):
                    num=-0.15576753
                if(l>=3.5 and l<=20.5):
                    num=-0.15265226
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=-0.149537
            if(l>=1.5 and l<3.5):
                num=-0.14642173
            if(l>=3.5 and l<=20.5):
                num=-0.14330646



    if(open>=-1 and open<1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=-0.1401912
            if(h>=1.5 and h<3.5):
                num=-0.13707593
            if(h>=3.5 and h<=20.5):
                num=-0.13396066
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.1308454
                if(l>=1.5 and l<3.5):
                    num=-0.12773013
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.124614865
                if(l>=1.5 and l<3.5):
                    num=-0.1214996
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.11838433
                if(l>=1.5 and l<3.5):
                    num=-0.115269065
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.1121538
                if(l>=1.5 and l<3.5):
                    num=-0.10903853
                if(l>=3.5 and l<20.5):
                    num=-0.105923265
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.102808
                if(l>=1.5 and l<3.5):
                    num=-0.09969273
                if(l>=3.5 and l<20.5):
                    num=-0.096577466
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.0934622
                if(l>=1.5 and l<3.5):
                    num=-0.09034693
                if(l>=3.5 and l<20.5):
                    num=-0.087231666
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.0841164
                if(l>=1.5 and l<3.5):
                    num=-0.08100113
                if(l>=3.5 and l<=20.5):
                    num=-0.077885866
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.0747706
                if(l>=1.5 and l<3.5):
                    num=-0.07165533
                if(l>=3.5 and l<=20.5):
                    num=-0.06854007
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.0654248
                if(l>=1.5 and l<3.5):
                    num=-0.062309533
                if(l>=3.5 and l<=20.5):
                    num=-0.059194267
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.056079
                if(l>=1.5 and l<3.5):
                    num=-0.052963734
                if(l>=3.5 and l<=20.5):
                    num=-0.049848467
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.0467332
                if(l>=1.5 and l<3.5):
                    num=-0.043617934
                if(l>=3.5 and l<=20.5):
                    num=-0.040502667
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.0373874
                if(l>=1.5 and l<3.5):
                    num=-0.034272134
                if(l>=3.5 and l<=20.5):
                    num=-0.03115687
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=-0.028041605
                if(l>=1.5 and l<3.5):
                    num=-0.02492634
                if(l>=3.5 and l<=20.5):
                    num=-0.021811076
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=-0.01869581
                if(l>=1.5 and l<3.5):
                    num=-0.015580546
                if(l>=3.5 and l<=20.5):
                    num=-0.012465281
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=-0.009350017
                if(l>=1.5 and l<3.5):
                    num=-0.006234752
                if(l>=3.5 and l<=20.5):
                    num=-0.0031194873
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.0031152647
                if(l>=1.5 and l<3.5):
                    num=0.0062305294
                if(l>=3.5 and l<=20.5):
                    num=0.009345794
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.012461059
                if(l>=1.5 and l<3.5):
                    num=0.0155763235
                if(l>=3.5 and l<=20.5):
                    num=0.018691588
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.021806853
                if(l>=1.5 and l<3.5):
                    num=0.024922118
                if(l>=3.5 and l<=20.5):
                    num=0.028037382
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.031152647
                if(l>=1.5 and l<3.5):
                    num=0.03426791
                if(l>=3.5 and l<=20.5):
                    num=0.037383176
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.040498443
                if(l>=1.5 and l<3.5):
                    num=0.04361371
                if(l>=3.5 and l<=20.5):
                    num=0.046728976
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.049844243
                if(l>=1.5 and l<3.5):
                    num=0.05295951
                if(l>=3.5 and l<=20.5):
                    num=0.056074776
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.059190042
                if(l>=1.5 and l<3.5):
                    num=0.06230531
                if(l>=3.5 and l<=20.5):
                    num=0.065420575
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.06853584
                if(l>=1.5 and l<3.5):
                    num=0.07165111
                if(l>=3.5 and l<=20.5):
                    num=0.074766375
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.07788164
                if(l>=1.5 and l<3.5):
                    num=0.08099691
                if(l>=3.5 and l<=20.5):
                    num=0.084112175
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.08722744
                if(l>=1.5 and l<3.5):
                    num=0.09034271
                if(l>=3.5 and l<=20.5):
                    num=0.093457974
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.09657324
                if(l>=1.5 and l<3.5):
                    num=0.09968851
                if(l>=3.5 and l<=20.5):
                    num=0.102803774
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.10591904
                if(l>=1.5 and l<3.5):
                    num=0.10903431
                if(l>=3.5 and l<=20.5):
                    num=0.112149574
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.11526484
                if(l>=1.5 and l<3.5):
                    num=0.11838011
                if(l>=3.5 and l<=20.5):
                    num=0.12149537
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.12461064
                if(l>=1.5 and l<3.5):
                    num=0.1277259
                if(l>=3.5 and l<=20.5):
                    num=0.13084117
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.13395643
            if(l>=1.5 and l<3.5):
                num=0.1370717
            if(l>=3.5 and l<=20.5):
                num=0.14018697


    if(open>=1 and open<3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=0.14330223
            if(h>=1.5 and h<3.5):
                num=0.1464175
            if(h>=3.5 and h<=20.5):
                num=0.14953277
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.15264803
                if(l>=1.5 and l<3.5):
                    num=0.1557633
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.15887856
                if(l>=1.5 and l<3.5):
                    num=0.16199383
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.1651091
                if(l>=1.5 and l<3.5):
                    num=0.16822436
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.17133963
                if(l>=1.5 and l<3.5):
                    num=0.1744549
                if(l>=3.5 and l<20.5):
                    num=0.17757016
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.18068543
                if(l>=1.5 and l<3.5):
                    num=0.1838007
                if(l>=3.5 and l<20.5):
                    num=0.18691596
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.19003123
                if(l>=1.5 and l<3.5):
                    num=0.1931465
                if(l>=3.5 and l<20.5):
                    num=0.19626176
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.19937703
                if(l>=1.5 and l<3.5):
                    num=0.2024923
                if(l>=3.5 and l<=20.5):
                    num=0.20560756
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.20872283
                if(l>=1.5 and l<3.5):
                    num=0.2118381
                if(l>=3.5 and l<=20.5):
                    num=0.21495336
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.21806863
                if(l>=1.5 and l<3.5):
                    num=0.2211839
                if(l>=3.5 and l<=20.5):
                    num=0.22429916
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.22741443
                if(l>=1.5 and l<3.5):
                    num=0.2305297
                if(l>=3.5 and l<=20.5):
                    num=0.23364496
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.23676023
                if(l>=1.5 and l<3.5):
                    num=0.2398755
                if(l>=3.5 and l<=20.5):
                    num=0.24299076
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.24610603
                if(l>=1.5 and l<3.5):
                    num=0.2492213
                if(l>=3.5 and l<=20.5):
                    num=0.25233656
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.25545183
                if(l>=1.5 and l<3.5):
                    num=0.2585671
                if(l>=3.5 and l<=20.5):
                    num=0.26168236
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.26479763
                if(l>=1.5 and l<3.5):
                    num=0.2679129
                if(l>=3.5 and l<=20.5):
                    num=0.27102816
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.27414343
                if(l>=1.5 and l<3.5):
                    num=0.2772587
                if(l>=3.5 and l<=20.5):
                    num=0.28037396
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.28348923
                if(l>=1.5 and l<3.5):
                    num=0.2866045
                if(l>=3.5 and l<=20.5):
                    num=0.28971976
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.29283503
                if(l>=1.5 and l<3.5):
                    num=0.2959503
                if(l>=3.5 and l<=20.5):
                    num=0.29906556
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.30218083
                if(l>=1.5 and l<3.5):
                    num=0.3052961
                if(l>=3.5 and l<=20.5):
                    num=0.30841136
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.31152663
                if(l>=1.5 and l<3.5):
                    num=0.3146419
                if(l>=3.5 and l<=20.5):
                    num=0.31775716
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.32087243
                if(l>=1.5 and l<3.5):
                    num=0.3239877
                if(l>=3.5 and l<=20.5):
                    num=0.32710296
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.33021823
                if(l>=1.5 and l<3.5):
                    num=0.3333335
                if(l>=3.5 and l<=20.5):
                    num=0.33644876
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.33956403
                if(l>=1.5 and l<3.5):
                    num=0.3426793
                if(l>=3.5 and l<=20.5):
                    num=0.34579456
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.34890983
                if(l>=1.5 and l<3.5):
                    num=0.3520251
                if(l>=3.5 and l<=20.5):
                    num=0.35514036
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.35825562
                if(l>=1.5 and l<3.5):
                    num=0.3613709
                if(l>=3.5 and l<=20.5):
                    num=0.36448616
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.36760142
                if(l>=1.5 and l<3.5):
                    num=0.3707167
                if(l>=3.5 and l<=20.5):
                    num=0.37383196
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.37694722
                if(l>=1.5 and l<3.5):
                    num=0.3800625
                if(l>=3.5 and l<=20.5):
                    num=0.38317776
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.38629302
                if(l>=1.5 and l<3.5):
                    num=0.3894083
                if(l>=3.5 and l<=20.5):
                    num=0.39252356
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.39563882
                if(l>=1.5 and l<3.5):
                    num=0.3987541
                if(l>=3.5 and l<=20.5):
                    num=0.40186936
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.40498462
                if(l>=1.5 and l<3.5):
                    num=0.4080999
                if(l>=3.5 and l<=20.5):
                    num=0.41121516
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.41433042
            if(l>=1.5 and l<3.5):
                num=0.4174457
            if(l>=3.5 and l<=20.5):
                num=0.42056096




    if(open>=3 and open<7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=0.42367622
            if(h>=1.5 and h<3.5):
                num=0.4267915
            if(h>=3.5 and h<=20.5):
                num=0.42990676
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.43302202
                if(l>=1.5 and l<3.5):
                    num=0.4361373
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.43925256
                if(l>=1.5 and l<3.5):
                    num=0.44236782
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.4454831
                if(l>=1.5 and l<3.5):
                    num=0.44859836
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.45171362
                if(l>=1.5 and l<3.5):
                    num=0.4548289
                if(l>=3.5 and l<20.5):
                    num=0.45794415
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.46105942
                if(l>=1.5 and l<3.5):
                    num=0.4641747
                if(l>=3.5 and l<20.5):
                    num=0.46728995
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.47040522
                if(l>=1.5 and l<3.5):
                    num=0.4735205
                if(l>=3.5 and l<20.5):
                    num=0.47663575
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.47975102
                if(l>=1.5 and l<3.5):
                    num=0.4828663
                if(l>=3.5 and l<=20.5):
                    num=0.48598155
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.48909682
                if(l>=1.5 and l<3.5):
                    num=0.4922121
                if(l>=3.5 and l<=20.5):
                    num=0.49532735
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.49844262
                if(l>=1.5 and l<3.5):
                    num=0.5015579
                if(l>=3.5 and l<=20.5):
                    num=0.5046731
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.50778836
                if(l>=1.5 and l<3.5):
                    num=0.5109036
                if(l>=3.5 and l<=20.5):
                    num=0.51401883
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.5171341
                if(l>=1.5 and l<3.5):
                    num=0.5202493
                if(l>=3.5 and l<=20.5):
                    num=0.52336454
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.5264798
                if(l>=1.5 and l<3.5):
                    num=0.529595
                if(l>=3.5 and l<=20.5):
                    num=0.53271025
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.5358255
                if(l>=1.5 and l<3.5):
                    num=0.5389407
                if(l>=3.5 and l<=20.5):
                    num=0.54205596
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.5451712
                if(l>=1.5 and l<3.5):
                    num=0.54828644
                if(l>=3.5 and l<=20.5):
                    num=0.5514017
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.5545169
                if(l>=1.5 and l<3.5):
                    num=0.55763215
                if(l>=3.5 and l<=20.5):
                    num=0.5607474
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.5638626
                if(l>=1.5 and l<3.5):
                    num=0.56697786
                if(l>=3.5 and l<=20.5):
                    num=0.5700931
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.57320833
                if(l>=1.5 and l<3.5):
                    num=0.57632357
                if(l>=3.5 and l<=20.5):
                    num=0.5794388
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.58255404
                if(l>=1.5 and l<3.5):
                    num=0.5856693
                if(l>=3.5 and l<=20.5):
                    num=0.5887845
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.59189975
                if(l>=1.5 and l<3.5):
                    num=0.595015
                if(l>=3.5 and l<=20.5):
                    num=0.5981302
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.60124546
                if(l>=1.5 and l<3.5):
                    num=0.6043607
                if(l>=3.5 and l<=20.5):
                    num=0.60747594
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.6105912
                if(l>=1.5 and l<3.5):
                    num=0.6137064
                if(l>=3.5 and l<=20.5):
                    num=0.61682165
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.6199369
                if(l>=1.5 and l<3.5):
                    num=0.6230521
                if(l>=3.5 and l<=20.5):
                    num=0.62616736
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.6292826
                if(l>=1.5 and l<3.5):
                    num=0.63239783
                if(l>=3.5 and l<=20.5):
                    num=0.63551307
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.6386283
                if(l>=1.5 and l<3.5):
                    num=0.64174354
                if(l>=3.5 and l<=20.5):
                    num=0.6448588
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.647974
                if(l>=1.5 and l<3.5):
                    num=0.65108925
                if(l>=3.5 and l<=20.5):
                    num=0.6542045
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.6573197
                if(l>=1.5 and l<3.5):
                    num=0.66043496
                if(l>=3.5 and l<=20.5):
                    num=0.6635502
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=0.66666543
                if(l>=1.5 and l<3.5):
                    num=0.6697807
                if(l>=3.5 and l<=20.5):
                    num=0.6728959
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.67601115
                if(l>=1.5 and l<3.5):
                    num=0.6791264
                if(l>=3.5 and l<=20.5):
                    num=0.6822416
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.68535686
                if(l>=1.5 and l<3.5):
                    num=0.6884721
                if(l>=3.5 and l<=20.5):
                    num=0.6915873
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.69470257
            if(l>=1.5 and l<3.5):
                num=0.6978178
            if(l>=3.5 and l<=20.5):
                num=0.70093304



    if(open>=7 and open<9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=0.7040483
            if(h>=1.5 and h<3.5):
                num=0.7071635
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.71027875
                if(l>=1.5 and l<3.5):
                    num=0.713394
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.7165092
                if(l>=1.5 and l<3.5):
                    num=0.71962446
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.7227397
                if(l>=1.5 and l<3.5):
                    num=0.72585493
                if(l>=3.5 and l<20.5):
                    num=0.72897017
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.7320854
                if(l>=1.5 and l<3.5):
                    num=0.73520064
                if(l>=3.5 and l<20.5):
                    num=0.7383159
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.7414311
                if(l>=1.5 and l<3.5):
                    num=0.74454635
                if(l>=3.5 and l<=20.5):
                    num=0.7476616
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.7507768
                if(l>=1.5 and l<3.5):
                    num=0.75389206
                if(l>=3.5 and l<=20.5):
                    num=0.7570073
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.76012254
                if(l>=1.5 and l<3.5):
                    num=0.7632378
                if(l>=3.5 and l<=20.5):
                    num=0.766353
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.76946825
                if(l>=1.5 and l<3.5):
                    num=0.7725835
                if(l>=3.5 and l<=20.5):
                    num=0.7756987
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.77881396
                if(l>=1.5 and l<3.5):
                    num=0.7819292
                if(l>=3.5 and l<=20.5):
                    num=0.78504443
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.78815967
                if(l>=1.5 and l<3.5):
                    num=0.7912749
                if(l>=3.5 and l<=20.5):
                    num=0.79439014
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.7975054
                if(l>=1.5 and l<3.5):
                    num=0.8006206
                if(l>=3.5 and l<=20.5):
                    num=0.80373585
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.8068511
                if(l>=1.5 and l<3.5):
                    num=0.8099663
                if(l>=3.5 and l<=20.5):
                    num=0.81308156
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.8161968
                if(l>=1.5 and l<3.5):
                    num=0.81931204
                if(l>=3.5 and l<=20.5):
                    num=0.8224273
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.8255425
                if(l>=1.5 and l<3.5):
                    num=0.82865775
                if(l>=3.5 and l<=20.5):
                    num=0.831773
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.8348882
                if(l>=1.5 and l<3.5):
                    num=0.83800346
                if(l>=3.5 and l<=20.5):
                    num=0.8411187
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.84423393
                if(l>=1.5 and l<3.5):
                    num=0.84734917
                if(l>=3.5 and l<=20.5):
                    num=0.8504644
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.85357964
                if(l>=1.5 and l<3.5):
                    num=0.8566949
                if(l>=3.5 and l<=20.5):
                    num=0.8598101
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.86292535
                if(l>=1.5 and l<3.5):
                    num=0.8660406
                if(l>=3.5 and l<=20.5):
                    num=0.8691558
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=0.87227106
                if(l>=1.5 and l<3.5):
                    num=0.8753863
                if(l>=3.5 and l<=20.5):
                    num=0.87850153
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=0.8816168
                if(l>=1.5 and l<3.5):
                    num=0.884732
                if(l>=3.5 and l<=20.5):
                    num=0.88784724
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.8909625
            if(l>=1.5 and l<3.5):
                num=0.8940777
            if(l>=3.5 and l<=20.5):
                num=0.89719296



    if(open>=9.94 and open<=10.6):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            num=0.9003082
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.9034234
            if(l>=1.5 and l<3.5):
                num=0.90653867
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.9096539
            if(l>=1.5 and l<3.5):
                num=0.91276914
            if(l>=3.5 and l<20.5):
                num=0.9158844
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.9189996
            if(l>=1.5 and l<3.5):
                num=0.92211485
            if(l>=3.5 and l<=20.5):
                num=0.9252301
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.9283453
            if(l>=1.5 and l<3.5):
                num=0.93146056
            if(l>=3.5 and l<=20.5):
                num=0.9345758
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.93769103
            if(l>=1.5 and l<3.5):
                num=0.94080627
            if(l>=3.5 and l<=20.5):
                num=0.9439215
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.94703674
            if(l>=1.5 and l<3.5):
                num=0.950152
            if(l>=3.5 and l<=20.5):
                num=0.9532672
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.95638245
            if(l>=1.5 and l<3.5):
                num=0.9594977
            if(l>=3.5 and l<=20.5):
                num=0.9626129
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.96572816
            if(l>=1.5 and l<3.5):
                num=0.9688434
            if(l>=3.5 and l<=20.5):
                num=0.97195864
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.9750739
            if(l>=1.5 and l<3.5):
                num=0.9781891
            if(l>=3.5 and l<=20.5):
                num=0.98130435
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.9844196
            if(l>=1.5 and l<3.5):
                num=0.9875348
            if(l>=3.5 and l<=20.5):
                num=0.99065006
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=0.9937653
            if(l>=1.5 and l<3.5):
                num=0.99688053
            if(l>=3.5 and l<=20.5):
                num=0.99999577
                
    return num
