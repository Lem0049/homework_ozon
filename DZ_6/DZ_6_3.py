# -*- coding: utf-8 -*-
import os


for file in os.listdir('.'):
    if file.endswith(".dat"):
        print(open(file).read())
