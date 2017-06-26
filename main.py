#!/usr/bin/python
# -*- coding: utf-8 -*-
from array import*
import nltk
from urllib import urlopen
import webbrowser
import datetime
from dateutil.parser import parse
from datetime import timedelta
import os


d=datetime.datetime.now()
print(d.strftime('%Y-%d-%mT%H:%M:%S'))
var=raw_input("Please enter your birthday: mm-dd-yy\n")

d1=datetime.datetime.strptime(var,"%m-%d-%y")
print "Since you born %d seconds passed" % ((d-d1).total_seconds()) 
print "Do you want to learn more?"

var1=raw_input("Y/N.....")

def to_integer(dt_time):
    return 100*dt_time.month + dt_time.day

if 81 <= to_integer(d1) <= 120:
      f= open("ascii/oglak.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is oglak"
      print "Do you want to learn more?"
      var2=raw_input("Y/N.....")
      os.system("link https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10")
elif 181 <= to_integer(d1) <= 220:
      f= open("ascii/kova.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is kova"
      print "Do you want to learn more?"
      var3=raw_input("Y/N.....")
      os.system("http www.beycan.net/626/kova-burcu-kadininin-ve-erkeginin-ozellikleri.html") 
elif 281 <= to_integer(d1) <= 320:
      f= open("ascii/balık.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is balık"
      print "Do you want to learn more?"
      var4=raw_input("Y/N.....")
      os.system("lynx www.beycan.net/627/balik-burcu-kadininin-ve-erkeginin-ozellikleri.html")
      
elif 381 <= to_integer(d1) <= 420:
      f= open("ascii/koc.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is koç"
      print "Do you want to learn more?"
      var5=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/616/koc-burcu-kadininin-ve-erkeginin-ozellikleri.html")
elif 481 <= to_integer(d1) <= 520:
      f= open("ascii/boga.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is boğa"
      print "Do you want to learn more?"
      var6=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/617/boga-burcu-kadininin-ve-erkeginin-ozellikleri.html")
elif 581 <= to_integer(d1) <= 620:
      f= open("ascii/ikizler.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is ikizler"
      print "Do you want to learn more?"
      var7=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/618/ikizler-burcu-kadininin-ve-erkeginin-ozellikleri.html")
elif 681 <= to_integer(d1) <= 720:
      f= open("ascii/yengec.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is yengeç"
      print "Do you want to learn more?"
      var8=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/619/yengec-burcu-kadininin-ve-erkeginin-ozellikleri.html")
elif 781 <= to_integer(d1) <= 820:
      f= open("ascii/aslan.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is aslan"
      print "Do you want to learn more?"
      var8=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/620/aslan-burcu-kadininin-ve-erkeginin-ozellikleri.html")
elif 881 <= to_integer(d1) <= 920:
      f= open("ascii/basak.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is başak"
      print "Do you want to learn more?"
      var9=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/621/basak-burcu-kadininin-ve-erkeginin-ozellikleri.html")
elif 981 <= to_integer(d1) <= 1020:
      f= open("ascii/terazi.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope terazi"
      print "Do you want to learn more?"
      var10=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/622/terazi-burcu-kadininin-ve-erkeginin-ozellikleri.html")
elif 1081 <= to_integer(d1) <= 1120:
      f= open("ascii/akrep.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is akrep"
      print "Do you want to learn more?"
      var11=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/623/akrep-burcu-kadininin-ve-erkeginin-ozellikleri.html")
elif 1181 <= to_integer(d1) <= 1220:
      f= open("ascii/yay.txt", "r")
      file_contents= f.read() 
      print (file_contents)
      f.close()
      print "Your horoscope is yay"
      print "Do you want to learn more?"
      var12=raw_input("Y/N.....")
      os.system("lynx http://www.beycan.net/624/yay-burcu-kadininin-ve-erkeginin-ozellikleri.html")
