import usys as sys
import lvgl as lv
import display_driver
from imagetools import get_png_info, open_png


def cb(evt):
    print('OK')


# Register PNG image decoder
decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

# Create an image from the png file
try:
    with open('../../assets/img_cogwheel_argb.png', 'rb') as f:
        png_data = f.read()
except:
    print("Could not find img_cogwheel_argb.png")
    sys.exit()

img_cogwheel_argb = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data
})

img1 = lv.img(lv.scr_act())
img1.set_src(img_cogwheel_argb)
img1.align(lv.ALIGN.CENTER, 0, -20)
img1.set_size(200, 200)

btn = lv.btn(lv.scr_act())
btn.add_event_cb(cb, lv.EVENT.CLICKED, None)
btn.set_style_bg_color(lv.palette_main(lv.PALETTE.GREEN), 0)
lbl = lv.label(btn)
lbl.set_text(lv.SYMBOL.OK + " OK")
lbl.set_style_text_color(lv.color_hex(0xFFFFFF), 0)
btn.align_to(img1, lv.ALIGN.OUT_BOTTOM_RIGHT, -20, 40)

btn2 = lv.btn(lv.scr_act())
btn2.add_event_cb(cb, lv.EVENT.CLICKED, None)
btn2.set_style_bg_color(lv.palette_main(lv.PALETTE.RED), 0)
lbl2 = lv.label(btn2)
lbl2.set_text(lv.SYMBOL.CLOSE + " Cancel")
lbl.set_style_text_color(lv.color_hex(0xFFFFFF), 0)
btn2.align_to(img1, lv.ALIGN.OUT_BOTTOM_RIGHT, 100, 40)

