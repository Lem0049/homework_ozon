# -*- coding: utf-8 -*-
import os, pickle

for file in os.listdir('.'):
    if file.endswith(".dat"):
        infile = open(file, 'rb')
        print(pickle.load(infile))
        infile.close()