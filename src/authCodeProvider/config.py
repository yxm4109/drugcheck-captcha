#!/bin/python
# -*- coding: UTF-8 -*-
"""
Settings for project.
"""

import os
import random


'''工程目录'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


TESSDATA_PREFIX="C:\Tesseract-OCR"
TESSDATA_LANG="eng"
TESSDATA_UNICHARSET="0123456789abcdefghijklmnopqrstuvwxyz@."


DEBUG = True
