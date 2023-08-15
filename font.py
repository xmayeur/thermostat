import lvgl as lv

s = lv.obj()
lbl = lv.label(s)
fnt = lv.font_load('fa-solid.bin')
lbl.set_style_text_font(fnt, 0)
