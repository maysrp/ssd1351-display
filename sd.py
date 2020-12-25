import base64
import os,sdcard,time
from machine import SPI,Pin
from ssd1351 import Display


spi = SPI(2, baudrate=14500000, sck=Pin(33), mosi=Pin(32))
display = Display(spi, dc=Pin(26), cs=Pin(25), rst=Pin(27),width=128,height=128)

sdi = SPI(1, baudrate=30000000, sck=Pin(14), mosi=Pin(15), miso=Pin(2))
sd = sdcard.SDCard(sdi, Pin(13))
sdfile=os.VfsFat(sd)
os.mount(sdfile,'/sd')
# os.chdir('sd')

v=time.ticks_ms()
c=open("/sd/v305.b",'r')
q=c.readlines()
print(time.ticks_ms()-v)


v=time.ticks_ms()
c=open("ssd1351.py",'r')
q=c.readlines()
print(time.ticks_ms()-v)



for i in q:
    c=time.ticks_ms()
    swap=base64.b64decode(i)
    display.draw_image_ram(swap, 0, 30, 128, 96)
    print(time.ticks_ms()-c)
    time.sleep(0.4)



//////
with open("/sd/v80.b",'r') as f:
    c=time.ticks_ms()
    for i in f:
        swap=base64.b64decode(i)
        s=open("w.raw",'wb')
        s.write(swap)
        s.close()
        print('123')
        display.draw_image('w.raw', 0, 30, 128, 96)
    print(time.ticks_ms()-c)



j=0
with open("/sd/v80.b",'r') as f:
    c=time.ticks_ms()
    for i in f:
        j+=1
        pass
    print(time.ticks_ms()-c)
print(j)

for i in range(800):
    c=time.ticks_ms()
    cf=open('/sd/'+str(i)+".raw",'rb')
    q=cf.read()
    cf.close()
    print(time.ticks_ms()-c)

    
import network
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True) # activate the interface
wlan.connect('1806', 'zgs12345') # connect to an AP



v=time.ticks_ms()
c=urequests.get("http://45.32.60.23/a")
print(time.ticks_ms()-v)


v=time.ticks_ms()
c=urequests.get("http://45.32.60.23/a.jpg")
print(time.ticks_ms()-v)


v=time.ticks_ms()
c=urequests.get("http://45.32.60.23/v305.b")
print(time.ticks_ms()-v)


使用互联网 http存储图片

base64 1fps=>多个fps 压制到一个文件

urequest 下载
c.text
[0:32768] 1fp
[32768:65536] 2fp

依次截取文件


base64 b64decode

然后给display 显示