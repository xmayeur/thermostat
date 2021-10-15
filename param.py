# Environment
mqtt_host = "192.168.1.10"
mqtt_port = 1884


# Language selection
class Lang:
    FR = 0
    EN = 1


l = Lang()
lang = l.FR

# labels
NIGHT_TEMP_TITLE = ["Temperature Nuit", "Night Temperature"][lang]
DAY_TEMP_TITLE = ["Temperature Jour", "Day Temperature"][lang]

days = [
    ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"],
    ["Mon", "Tue", "Wed", 'Thu', "Fri", "Sat", "Sun"]
][lang]


# Constants
default_night = 16
default_day = 19