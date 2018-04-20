#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0103
import os
import time
import subprocess

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



def jtalk(t):
    u"""open_jtalk を使って日本語のメッセージを読み上げる
    message: 日本語の文字列
    """

    # http://karaage.hatenadiary.jp/entry/2016/07/22/073000
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice']
#    htsvoice=['-m','mei_normal.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)
    

if __name__ == "__main__":
    message = "たろうさん　こんにちは"
    jtalk(message)
    time.sleep(1)

    message = "お疲れ様。"
    jtalk(message)
    
    time.sleep(1)


    names = ['naoto', 'makoto', 'osamu', 'tarou',
             'junya', 'masaaki', 'hideki',
             'akiko', 'sanae', 'kanako', 'shiori', 'yuka', 'ayaka']
             
    message = ""
    for name in names:
        message += "%sさん　%s　" % (kana.romaji2katakana(name), getAisatsu())

    jtalk(message)
        
