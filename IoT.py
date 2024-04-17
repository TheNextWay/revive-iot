import string

import wiringpi
import random
import requests
from .gui import show_frame
from .gui import frame_maintain
def init():
wiringpi.wiringPiSetup()
wiringpi.pinMode(2, 1)
wiringpi.digitalWrite(2, 1)

def turnoffcoveyor():
    wiringpi.digitalWrite(6, 1)

def turnonconveyor():
    wiringpi.digitalWrite(6, 0)

def maketoken(point : int, tokenstr):
    response = requests.post('serverip:3000/qrrawan/'+ tokenstr + '/' + point)
    if (response.status_code == 200) :
        return tokenstr
    if (response.status_code == 500) :
        show_frame(frame_maintain)
    if (response.status_code == 406) :
        return maketoken(point, tokenstr)

def checktoken(token, point) :
    response = requests.post('serverip:3000/check/' + token)
    if(response.status_code == 200) :
        nama = response.content
        return nama
    if(response.status_code == 204) :
        return 'belum di claim'
    if(response.status_code == 404) :
        maketoken(point,token)
        return 'belum di claim'
