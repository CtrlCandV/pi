# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
#将舵机度数转换为信号占空比
def tonum(num):
    fm=10.0/180.0
    num=num*fm+2.5
    num=int(num*10)/10.0
    return num

GPIO.setmode(GPIO.BCM) #设置gpio引脚编号模式，有两种编号模式可供选择，自己随意设置就好
GPIO.setup(13, GPIO.OUT)
p13 = GPIO.PWM(13, 50)
p13.start(tonum(0))
i=0
num=5
while True:
    i=i+num
    if i>180:
        i=180
        num=-num
    if i<0:
        i=0
        num=-num
    p13.ChangeDutyCycle(tonum(i))
    time.sleep(0.05)