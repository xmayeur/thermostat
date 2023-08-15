import lvgl as lv
from param import *

# TFT uses BGR
RED = lv.color_hex(0x1914B3)
GREEN = lv.color_hex(0x1d7810)
ORANGE = lv.color_hex(0x425DF5)
ORANGE_DARK = lv.color_hex(0x0C287D)
BLUE = lv.color_hex(0xF7372D)
BLUE_DARK = lv.color_hex(0x94211B)


class SetCtrl:

    def __init__(self, day_temp=default_day, night_temp=default_night):
        self.day_temp = day_temp
        self.night_temp = night_temp
        self.parent_scr = lv.scr_act()

        # create new screen with two sliders & two buttons
        self.scr = lv.obj()

        self.slider_night = lv.slider(self.scr)
        self.slider_night_label = lv.label(self.scr)
        self.slider_night_title = lv.label(self.scr)
        self.config_slider_night()

        self.slider_day = lv.slider(self.scr)
        self.slider_day_label = lv.label(self.scr)
        self.slider_day_title = lv.label(self.scr)
        self.config_slider_day()

        # configure OK & Cancel buttons
        self.btn_ok = lv.btn(self.scr)
        self.btn_ok.add_event_cb(self.ok_cb, lv.EVENT.CLICKED, None)
        self.btn_ok.set_style_bg_color(GREEN, 0)
        self.lbl_ok = lv.label(self.btn_ok)
        self.lbl_ok.set_text(lv.SYMBOL.OK + " OK")
        self.lbl_ok.set_style_text_color(lv.color_hex(0xFFFFFF), 0)
        self.btn_ok.set_width(lv.SIZE.CONTENT)
        self.btn_ok.set_height(lv.SIZE.CONTENT)
        self.btn_ok.set_x(30)
        self.btn_ok.set_y(200)

        self.btn_cancel = lv.btn(self.scr)
        self.btn_cancel.add_event_cb(self.cancel_cb, lv.EVENT.CLICKED, None)
        self.btn_cancel.set_style_bg_color(RED, 0)
        self.lbl_cancel = lv.label(self.btn_cancel)
        self.lbl_cancel.set_text(lv.SYMBOL.CLOSE + " Cancel")
        self.lbl_cancel.set_style_text_color(lv.color_hex(0xFFFFFF), 0)
        self.btn_cancel.set_width(lv.SIZE.CONTENT)
        self.btn_cancel.set_height(lv.SIZE.CONTENT)
        self.btn_cancel.set_x(190)
        self.btn_cancel.set_y(200)

    def show(self):
        lv.scr_load(self.scr)

    def slider_day_event_cb(self, e):
        self.slider_day_label.set_text("{:d}°C".format(self.slider_day.get_value()))
        self.slider_day_label.align_to(self.slider_day, lv.ALIGN.OUT_BOTTOM_MID, 0, 10)

    def slider_night_event_cb(self, e):
        self.slider_night_label.set_text("{:d}°C".format(self.slider_night.get_value()))
        self.slider_night_label.align_to(self.slider_night, lv.ALIGN.OUT_BOTTOM_MID, 0, 10)

    def ok_cb(self, e):
        self.day_temp = self.slider_day.get_value()
        self.night_temp = self.slider_night.get_value()
        if self.parent_scr:
            lv.scr_load(self.parent_scr)

    def cancel_cb(self, e):
        self.slider_day.set_value(self.day_temp, 0)
        self.slider_night.set_value(self.night_temp, 0)
        self.slider_day_label.set_text("{:d}°C".format(self.slider_day.get_value()))
        self.slider_night_label.set_text("{:d}°C".format(self.slider_night.get_value()))
        if self.parent_scr:
            lv.scr_load(self.parent_scr)

    #
    # Show how to style a slider1.
    #
    # Create a transition
    def config_slider_night(self):
        props = [lv.STYLE.BG_COLOR, 0]
        transition_dsc = lv.style_transition_dsc_t()
        transition_dsc.init(props, lv.anim_t.path_linear, 300, 0, None)

        style_main = lv.style_t()
        style_indicator = lv.style_t()
        style_knob = lv.style_t()
        style_pressed_color = lv.style_t()
        style_main.init()
        style_main.set_bg_opa(lv.OPA.COVER)
        style_main.set_bg_color(lv.color_hex3(0xbbb))
        style_main.set_radius(lv.RADIUS.CIRCLE)
        style_main.set_pad_ver(-2)  # Makes the indicator larger

        style_indicator.init()
        style_indicator.set_bg_opa(lv.OPA.COVER)
        style_indicator.set_bg_color(BLUE)
        style_indicator.set_radius(lv.RADIUS.CIRCLE)
        style_indicator.set_transition(transition_dsc)

        style_knob.init()
        style_knob.set_bg_opa(lv.OPA.COVER)
        style_knob.set_bg_color(BLUE)
        style_knob.set_border_color(BLUE_DARK)
        style_knob.set_border_width(2)
        style_knob.set_radius(lv.RADIUS.CIRCLE)
        style_knob.set_pad_all(6)  # Makes the knob larger
        style_knob.set_transition(transition_dsc)

        style_pressed_color.init()
        style_pressed_color.set_bg_color(BLUE_DARK)
        
        self.slider_night.remove_style_all()  # Remove the styles coming from the theme

        self.slider_night.add_style(style_main, lv.PART.MAIN)
        self.slider_night.add_style(style_indicator, lv.PART.INDICATOR)
        self.slider_night.add_style(style_pressed_color, lv.PART.INDICATOR | lv.STATE.PRESSED)
        self.slider_night.add_style(style_knob, lv.PART.KNOB)
        self.slider_night.add_style(style_pressed_color, lv.PART.KNOB | lv.STATE.PRESSED)

        self.slider_night_label.set_text(str(default_night) + "°C")
        self.slider_night_title.set_text(lv.SYMBOL.MOON + NIGHT_TEMP_TITLE)
        self.slider_night.set_value(default_night, 0)

        self.slider_night.set_width(20)
        self.slider_night.set_height(130)
        self.slider_night.set_pos(lv.pct(20), 40)
        self.slider_night.set_range(10, 30)
        self.slider_night_label.align_to(self.slider_night, lv.ALIGN.OUT_BOTTOM_MID, 0, 10)
        self.slider_night_title.align_to(self.slider_night, lv.ALIGN.OUT_TOP_MID, 0, -10)
        self.slider_night.add_event_cb(self.slider_night_event_cb, lv.EVENT.VALUE_CHANGED, None)

    def config_slider_day(self):
        props = [lv.STYLE.BG_COLOR, 0]
        transition_dsc = lv.style_transition_dsc_t()
        transition_dsc.init(props, lv.anim_t.path_linear, 300, 0, None)

        style_main = lv.style_t()

        style_main.init()
        style_main.set_bg_opa(lv.OPA.COVER)
        style_main.set_bg_color(lv.color_hex3(0xbbb))
        style_main.set_radius(lv.RADIUS.CIRCLE)
        style_main.set_pad_ver(-2)  # Makes the indicator larger
        # Create a slider2 and add the style
        style_indicator = lv.style_t()
        style_knob = lv.style_t()
        style_pressed_color = lv.style_t()
        style_indicator.init()
        style_indicator.set_bg_opa(lv.OPA.COVER)
        style_indicator.set_bg_color(ORANGE)
        style_indicator.set_radius(lv.RADIUS.CIRCLE)
        style_indicator.set_transition(transition_dsc)

        style_knob.init()
        style_knob.set_bg_opa(lv.OPA.COVER)
        style_knob.set_bg_color(ORANGE)
        style_knob.set_border_color(ORANGE_DARK)
        style_knob.set_border_width(2)
        style_knob.set_radius(lv.RADIUS.CIRCLE)
        style_knob.set_pad_all(6)  # Makes the knob larger
        style_knob.set_transition(transition_dsc)

        style_pressed_color.init()
        style_pressed_color.set_bg_color(ORANGE_DARK)

        self.slider_day.remove_style_all()  # Remove the styles coming from the theme

        self.slider_day.add_style(style_main, lv.PART.MAIN)
        self.slider_day.add_style(style_indicator, lv.PART.INDICATOR)
        self.slider_day.add_style(style_pressed_color, lv.PART.INDICATOR | lv.STATE.PRESSED)
        self.slider_day.add_style(style_knob, lv.PART.KNOB)
        self.slider_day.add_style(style_pressed_color, lv.PART.KNOB | lv.STATE.PRESSED)

        self.slider_day_label.set_text(str(default_day) + "°C")
        self.slider_day_title.set_text(lv.SYMBOL.SUN +  DAY_TEMP_TITLE)
        self.slider_day.set_value(default_day, 0)

        self.slider_day.set_width(20)
        self.slider_day.set_height(130)
        self.slider_day.set_pos(lv.pct(70), 40)
        self.slider_day.set_range(10, 30)
        self.slider_day_label.align_to(self.slider_day, lv.ALIGN.OUT_BOTTOM_MID, 0, 10)
        self.slider_day_title.align_to(self.slider_day, lv.ALIGN.OUT_TOP_MID, 0, -10)
        self.slider_day.add_event_cb(self.slider_day_event_cb, lv.EVENT.VALUE_CHANGED, None)
