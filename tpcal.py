from time import sleep

def tpcal(lv, touch):
    old = lv.scr_act()
    s = lv.obj()
    lv.scr_load(s)
    btn = lv.btn(s)
    xt = 315
    yt = 235
    btn.set_pos(xt, yt)
    btn.set_size(5,5)
    x0 = touch.cal_x0
    x1 = touch.cal_x1
    y0 = touch.cal_y0
    y1 = touch.cal_y1
    lbl = lv.label(s)
    lbl.center()
    lbl.set_text(str(touch.cal_x0) + '-' + str(touch.cal_y0))
    t  = lv.btn(s)
    t.set_size(5,5)
    while True:
        try:
            (x, y) = touch.get_coords()
            t.set_x(x)
            t.set_y(y)
            touch.cal_x0 -= 5*(xt - x0)
            touch.cal_y0 -= 5*(yt - y0)
            lbl.set_text(str(x) + '-' + str(y) + '\n'+str(touch.cal_x0), str(touch.cal_y0))
        except:
            pass
        sleep(0.1)


# lv.scr_load(old)


