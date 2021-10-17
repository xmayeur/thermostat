

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

