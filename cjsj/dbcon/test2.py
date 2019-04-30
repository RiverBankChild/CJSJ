'''
Created on 2019年4月30日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import numpy as np
from pandas import DataFrame
import pandas as pd


df=DataFrame(np.arange(12).reshape((3,4)),index=['one','two','thr'],columns=list('abcd'))
df.drop(columns=['a']);
print(df)