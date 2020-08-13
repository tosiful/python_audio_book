# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:55:19 2020

@author: Tosif

Easy & Smart Spoken English (updated).pdf

"""

import pyttsx3

import PyPDF2


book=open('Spamming ebook.pdf','rb')

pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages

friend=pyttsx3.init()
for num in range(5,pages):
    
    
    page=pdfreader.getPage(num)
    
    text=page.extractText()
    
    friend.say(text)
    friend.runAndWait()