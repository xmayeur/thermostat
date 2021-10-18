import lvgl as lv


# Language selection
class Lang:
    FR = 0
    EN = 1


lang = Lang().FR

# labels
NIGHT_TEMP_TITLE = ["Temperature Nuit", "Night Temperature"][lang]
DAY_TEMP_TITLE = ["Temperature Jour", "Day Temperature"][lang]

days = [
        ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"],
        ["Mon", "Tue", "Wed", 'Thu', "Fri", "Sat", "Sun"]
    ][lang]

# TFT uses BGR
RED = lv.color_hex(0x1914B3)
GREEN = lv.color_hex(0x1d7810)
ORANGE = lv.color_hex(0x425DF5)
ORANGE_DARK = lv.color_hex(0x0C287D)
BLUE = lv.color_hex(0xF7372D)
BLUE_DARK = lv.color_hex(0x94211B)
