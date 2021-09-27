# Raspberry Pi Pico Micropython ESP8266 Library
[![GitHub version](https://img.shields.io/github/release/noyelseth/rpi-pico-micropython-esp8266-lib.svg)](lib-release)
[![GitHub download](https://img.shields.io/github/downloads/noyelseth/rpi-pico-micropython-esp8266-lib/total.svg)](lib-release)
[![GitHub stars](https://img.shields.io/github/stars/noyelseth/rpi-pico-micropython-esp8266-lib.svg)](lib-stars)
[![GitHub issues](https://img.shields.io/github/issues/noyelseth/rpi-pico-micropython-esp8266-lib.svg)](lib-issues)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](lib-licence)

<p align="center">
<img src="https://user-images.githubusercontent.com/29272159/134866689-f3a34753-1583-441e-917b-6d599b8c0fc8.png" width="250"><img src="https://user-images.githubusercontent.com/29272159/134866581-f0d7cf42-9fc0-48bc-a859-7d74b070a3fd.png" width="150"><img src="https://user-images.githubusercontent.com/29272159/134868586-bd05f5e9-eaf2-4ac2-9688-7aca16165bf8.png" width="350">
</p>

## Description
This is a Micropython Library for RaspberryPi-Pico to communicate with ESP8266 using AT command.

## Hardware Connection
<p align="center">
<img src="https://user-images.githubusercontent.com/29272159/134862637-7109bc5b-ac92-4637-8ca6-b4d2fd6d9656.png" width="800">
</p>

## Getting Started with Examples
This is a basic AT Command library for RaspberryPi-Pico, which simplifies the communication process with the ESP8266. 
The best way to understand the library is with the example shown below, This example shows you how to make a GET/POST request using ESP8266 with the help of the RaspberryPi-Pico.

### How to Use Library
```python
from machine import Pin
from esp8266 import ESP8266
import time, sys

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("RPi-Pico MicroPython Ver:", sys.version)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

## Create On-board Led object
led=Pin(25,Pin.OUT)

## Create an ESP8266 Object
esp01 = ESP8266()
esp8266_at_ver = None

print("StartUP",esp01.startUP())
print("Echo-Off",esp01.echoING())
print("\r\n")

'''
Print ESP8266 AT comand version and SDK details
'''
esp8266_at_ver = esp01.getVersion()
if(esp8266_at_ver != None):
    print(esp8266_at_ver)

'''
set the current WiFi in SoftAP+STA
'''
print("WiFi Current Mode:",esp01.setCurrentWiFiMode()
  
print("\r\n\r\n")

'''
Connect with the WiFi
'''
print("Try to connect with the WiFi..")
while (1):
    if "WIFI CONNECTED" in esp01.connectWiFi("ssid","pwd"):
        print("ESP8266 connect with the WiFi..")
        break;
    else:
        print(".")
        time.sleep(2)


print("\r\n\r\n")
print("Now it's time to start HTTP Get/Post Operation.......\r\n")

while(1):    
    led.toggle()
    time.sleep(1)
    
    '''
    Going to do HTTP Get Operation with www.httpbin.org/ip, It return the IP address of the connected device
    '''
    httpCode, httpRes = esp01.doHttpGet("www.httpbin.org","/ip","RaspberryPi-Pico", port=80)
    print("------------- www.httpbin.org/ip Get Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("-----------------------------------------------------------------------------\r\n\r\n")
    
    
    '''
    Going to do HTTP Post Operation with www.httpbin.org/post
    '''
    post_json="{\"name\":\"Noyel\"}"
    httpCode, httpRes = esp01.doHttpPost("www.httpbin.org","/post","RPi-Pico", "application/json",post_json,port=80)
    print("------------- www.httpbin.org/post Post Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("--------------------------------------------------------------------------------\r\n\r\n")
```




## Contributing
You are very welcome to contribute: stability bugfixes, new hardware support, or any other improvements. Please.
[![GitHub stars](https://img.shields.io/github/stars/noyelseth/rpi-pico-micropython-esp8266-lib.svg?style=social&label=Star)](lib-stars)
[![GitHub forks](https://img.shields.io/github/forks/noyelseth/rpi-pico-micropython-esp8266-lib.svg?style=social&label=Fork)](lib-network)


### License
This project is released under The MIT License (MIT) © [Noyel Seth](https://github.com/noyelseth)

 
