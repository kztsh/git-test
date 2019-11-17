#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:54:20 2019

@author: arimoto
"""
import numpy as np
import pandas as pd

test_hoge1=2
test_hoge2 = 3

df = pd.read_csv("sample_utf8.csv")
print(df)
df.to_csv("test_out.csv")

def test_func(test_hoge1, test_hoge2):
    var = test_hoge1 + test_hoge2
    print("var: ", var)

a=1

test_func(test_hoge1, test_hoge2)

print("hoge1")

print("hoge2")
print("1{}{}".format(test_hoge1, test_hoge2))