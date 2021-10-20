import network
from locales import *
from secrets import *
import webrepl
from ili9XXX import ili9341, LANDSCAPE
from xpt2046 import xpt2046
import lvgl as lv
import ntptime
from machine import RTC, reset
from lib.umqtt.simple2 import MQTTClient
import json

config = json.load(open('config.json', 'r'))
mqtt_host = config['mqtt_host']
mqtt_port = config['mqtt_port']


# initialize display & touch screen
displ = ili9341(cs=5, dc=4, rst=22, clk=18, mosi=23, miso=19, colormode=0, factor=32, rot=LANDSCAPE, width=320, height=240)
touch = xpt2046(cs=14, half_duplex=True, mhz=5, max_cmds=16, cal_x0=3800, cal_y0=3710, cal_x1=400,cal_y1=300, transpose=False, samples=3)

# set display style
style = lv.style_t()
style.init()
style.set_radius(5)

style.set_width(lv.SIZE.CONTENT)
style.set_height(lv.SIZE.CONTENT)

style.set_pad_ver(5)
style.set_pad_left(5)
style.set_x(lv.pct(5))
style.set_y(lv.pct(5))

console = lv.obj(lv.scr_act())
console.set_style_bg_color(lv.color_white(), 0)
console.add_style(style, 0)
label = lv.label(console)

HOSTNAME = 'touchESP'
msg = ''


# start network
def do_connect():
    global msg, label
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        msg = 'connecting to network...'
        label.set_text(msg)
        wlan.connect(ssid, wifi_pwd)
        while not wlan.isconnected():
            pass
    msg += '\nIP address : ' + wlan.ifconfig()[0]
    label.set_text(msg)
    wlan.config(dhcp_hostname=HOSTNAME)


do_connect()

# set time from ntpserver
ntptime.settime()
rtc = RTC()

year, mth, d, day, h, m, s, _ = rtc.datetime()
msg += "\n%s  %d/%d/%d - %d:%d:%d UTC" %(days[day], year, mth, d, h, m, s)
label.set_text(msg)

# start webrepl
webrepl.start()

# Initialize MQTT
mqtt_client = MQTTClient("esp", mqtt_host, port=mqtt_port, user=mqtt_user, password=mqtt_pwd)
mqtt_client.connect()
mqtt_client.publish(HOSTNAME.encode()+b'/status', b"Booting...")
msg += '\nMQTT client connected'
label.set_text(msg)
