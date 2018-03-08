#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0103
import os
import time
import kana # https://github.com/haya14busa/twibusa/blob/master/romaji2kana.py

def getAisatsu():
    u"""時刻に応じた挨拶を返す
    """
    
    hour = time.localtime()[3]
    if hour < 12:
        aisatsu = "おはよう"
    elif hour < 19:
        aisatsu = "こんにちは"
    else:
        aisatsu = "こんばんは"

    return aisatsu

def jsay(message):
    u"""open_jtalk を使って日本語のメッセージを読み上げる
    message: 日本語の文字列
    """
    
    cmd = "sh jsay.sh %s" % message
    os.system(cmd)

if __name__ == "__main__":
    message = "たろうさん　こんにちは"
    jsay(message)

    names = ['naoto', 'makoto', 'osamu', 'tarou',
             'junya', 'masaaki', 'hideki',
             'akiko', 'sanae', 'kanako', 'shiori', 'yuka', 'ayaka']
    for name in names:
        message = "%sさん　%s" % (kana.romaji2katakana(name), getAisatsu())
        jsay(message)
