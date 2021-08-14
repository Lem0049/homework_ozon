# -*- coding: utf-8 -*-
import os
import pickle
'''This program find all .dat files in folder and print content'''
for file in os.listdir('.'):
    if file.endswith(".dat"):
        infile = open(file, 'rb')
        print(pickle.load(infile))
        infile.close()
