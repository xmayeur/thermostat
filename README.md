# CONNECTED THERMOSTAT
Project based on [AZ Delivery Touch](https://www.az-delivery.de/en/products/az-touch-wandgehauseset-mit-2-8-zoll-touchscreen-fur-esp8266-und-esp32) ili9371 + xpt2046 display &amp; ESP32 board

![](AZ%20_delivery%20Touch.png)

## Dependencies

### Firmware

The firmware is built using [lvgl & microptyhon](https://github.com/lvgl/lv_micropython)
* Follow the instructions to clone the repositories & compile the initial firmware
* Before compiling, copy with recursive option this local lv_micropython over the cloned lv_micropython the
    * This will enable the embedding of the Monteserrat font with a few font sizes
    * It also embeds additional Font Awesome symbols used by this project
* If you don't want to compile yourself the firmware, execute the [flashFW](./firmware/flashFW.sh) command

### Libraries

* mqtt.simple2
* DHT22

### screen shots

![](./.images/set_schedule.png)

![](.images/set_temp.png)
