import lvgl as lv
from locales import *
import json

hours = ["{:02d}".format(x) for x in range(0, 24)]
minutes = ['0', '15', '30', '45']


class SetSchedule:

    def __init__(self):
        # create new screen with two sliders & two buttons
        self.parent_scr = lv.scr_act()
        self.scr = lv.obj()
        self.schedule = {}
        self.updated = False
        self.sel_day = ''
        self.start_hr = ''
        self.start_min = ''
        self.end_hr = ''
        self.end_min = ''
        self.roller1 = lv.roller(self.scr)
        self.roller2 = lv.roller(self.scr)
        self.roller3 = lv.roller(self.scr)
        self.roller4 = lv.roller(self.scr)
        self.roller5 = lv.roller(self.scr)

        self.draw_rollers()
        self.draw_buttons()
        self.read_schedule()

    def read_schedule(self):
        try:
            self.schedule = json.load(open('config.json', 'r'))['week_schedule']
        except:
            self.schedule = None

    def write_schedule(self):
        try:
            _config = json.load(open('config.json', 'r'))
            _config['week_schedule'] = self.schedule
            json.dump(_config, open('config.json', 'w'))
            return True
        except:
            self.schedule = None
            return False

    def event_hdlr_day(self, e):
        code = e.get_code()
        obj = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED:
            self.sel_day = obj.get_selected()
            x = self.schedule[self.sel_day]
            self.roller2.set_selected(int(x[0]['start'][:2]), lv.ANIM.ON)
            self.roller3.set_selected(int(x[0]['start'][2:]), lv.ANIM.ON)
            self.roller4.set_selected(int(x[0]['end'][:2]), lv.ANIM.ON)
            self.roller5.set_selected(int(x[0]['end'][2:]), lv.ANIM.ON)

    def event_hdlr_hr(self, e):
        code = e.get_code()
        obj = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED:
            option = " " * 10
            obj.get_selected_str(option, len(option))
            self.start_hr = option.strip()

    def event_hdlr_min(self, e):
        code = e.get_code()
        obj = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED:
            option = " " * 10
            obj.get_selected_str(option, len(option))
            self.end_min = option.strip()

    def event_hdlr_end_hr(self, e):
        code = e.get_code()
        obj = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED:
            option = " " * 10
            obj.get_selected_str(option, len(option))
            self.end_hr = option.strip()

    def event_hdlr_end_min(self, e):
        code = e.get_code()
        obj = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED:
            option = " " * 10
            obj.get_selected_str(option, len(option))
            self.start_min = option.strip()

    def draw_rollers(self):
        #
        # five infinite roller with the name of the days, hours, minutes
        #

        # TODO SET TITLE ABOVE ROLLERS
        roller1 = self.roller1
        roller1.set_options("\n".join(days), lv.roller.MODE.INFINITE)
        roller1.set_visible_row_count(4)
        roller1.set_pos(10, 30)
        roller1.add_event_cb(self.event_hdlr_day, lv.EVENT.ALL, None)

        roller2 = self.roller2
        roller2.set_options("\n".join(hours), lv.roller.MODE.INFINITE)
        roller2.set_visible_row_count(4)
        roller2.set_pos(120, 30)
        roller2.add_event_cb(self.event_hdlr_hr, lv.EVENT.ALL, None)

        roller3 = self.roller3
        roller3.set_options("\n".join(minutes), lv.roller.MODE.INFINITE)
        roller3.set_visible_row_count(4)
        roller3.set_pos(170, 30)
        roller3.add_event_cb(self.event_hdlr_min, lv.EVENT.ALL, None)

        roller4 = self.roller4
        roller4.set_options("\n".join(hours), lv.roller.MODE.INFINITE)
        roller4.set_visible_row_count(4)
        roller4.set_pos(220, 30)
        roller4.add_event_cb(self.event_hdlr_end_hr, lv.EVENT.ALL, None)

        roller5 = self.roller5
        roller5.set_options("\n".join(minutes), lv.roller.MODE.INFINITE)
        roller5.set_visible_row_count(4)
        roller5.set_pos(270, 30)
        roller5.add_event_cb(self.event_hdlr_end_min, lv.EVENT.ALL, None)

    def draw_buttons(self):
        # configure OK & Cancel buttons
        btn_ok = lv.btn(self.scr)
        btn_ok.add_event_cb(self.ok_cb, lv.EVENT.CLICKED, None)
        btn_ok.set_style_bg_color(GREEN, 0)
        lbl_ok = lv.label(btn_ok)
        lbl_ok.set_text(lv.SYMBOL.OK + " Update")
        lbl_ok.set_style_text_color(lv.color_hex(0xFFFFFF), 0)
        btn_ok.set_width(lv.SIZE.CONTENT)
        btn_ok.set_height(lv.SIZE.CONTENT)
        btn_ok.set_x(30)
        btn_ok.set_y(200)

        btn_cancel = lv.btn(self.scr)
        btn_cancel.add_event_cb(self.cancel_cb, lv.EVENT.CLICKED, None)
        btn_cancel.set_style_bg_color(RED, 0)
        lbl_cancel = lv.label(btn_cancel)
        lbl_cancel.set_text(lv.SYMBOL.CLOSE + " Quit")
        lbl_cancel.set_style_text_color(lv.color_hex(0xFFFFFF), 0)
        btn_cancel.set_width(lv.SIZE.CONTENT)
        btn_cancel.set_height(lv.SIZE.CONTENT)
        btn_cancel.set_x(190)
        btn_cancel.set_y(200)

    def ok_cb(self, e):
        self.schedule[self.sel_day][0] = {
            "start": self.start_hr + self.start_min,
            "end": self.end_hr + self.end_min
        }
        self.updated = True

    def cancel_cb(self, e):
        self.write_schedule()
        if self.parent_scr:
            lv.scr_load(self.parent_scr)

    def show(self):
        lv.scr_load(self.scr)