#!/bin/python
# -*- coding: UTF-8 -*-
import tesseract
import config

class tessApi():
    def __init__(self):
        '''
            初始化tess
        '''
        self.tessApi = tesseract.TessBaseAPI()
        self.tessApi.Init(config.TESSDATA_PREFIX,config.TESSDATA_LANG,tesseract.OEM_DEFAULT)
        self.tessApi.SetVariable("tessedit_char_whitelist", config.TESSDATA_UNICHARSET)
        self.tessApi.SetPageSegMode(tesseract.PSM_SINGLE_LINE)
    

    def get(self):
        return self.tessApi