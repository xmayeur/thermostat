"""
Test with https://sim.lvgl.io/v8.1/micropython/ports/javascript/index.html
Examples: https://docs.lvgl.io/master/examples.html

"""
import lvgl as lv

class DayTemp:

    def __init__(self):

        self.day_temp = 20
        self.scr = lv.obj()

        # add a meter
        self.meter = lv.meter(self.scr)
        self.meter.set_size(170, 170)
        self.meter.center()

        # add a scale
        self.scale = self.meter.add_scale()
        self.meter.set_scale_range(self.scale, 10, 30, 270, 135)
        self.meter.set_scale_ticks(self.scale, 21, 1, 10, lv.palette_main(lv.PALETTE.GREY))
        self.meter.set_scale_major_ticks(self.scale, 5, 3, 15, lv.color_black(), 10)
        self.meter.set_y(20)

        # Add an arc
        self.arc = lv.arc(self.scr)
        self.arc.set_end_angle(200)
        self.arc.set_size(180, 180)
        self.arc.set_range(10, 30)
        self.arc.set_value(self.day_temp)
        self.arc.center()
        self.arc.set_y(20)
        self.arc.add_event_cb(self.evt_hldr, lv.EVENT.VALUE_CHANGED, None)

        # Set label style
        style = lv.style_t()
        style.init()
        style.set_width(lv.SIZE.CONTENT)
        style.set_height(lv.SIZE.CONTENT)
        style.set_text_font(lv.font_montserrat_16)
        style.set_bg_color(lv.color_white())

        # Add selected temperature label
        self.label = lv.label(self.scr)
        self.label.add_style(style, 0)
        self.label.set_text(str(self.day_temp)+'°C')
        self.label.set_style_text_font(lv.font_montserrat_16, 0)
        self.label.center()
        self.label.set_y(40)
        lv.scr_load(self.scr)

        # Add title
        # TODO

        # Add OK & Cancel button
        # TODO

    # Call back when changing the temperature
    def evt_hldr(self, evt):
        _arc = evt.get_target()
        self.day_temp = _arc.get_value()
        self.label.set_text(str(self.day_temp)+'°C')

