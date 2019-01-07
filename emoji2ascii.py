SCRIPT_NAME    = "emoji2ascii"
SCRIPT_AUTHOR  = "eyJhb <eyjhbb@gmail.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPLv3"
SCRIPT_DESC    = "Replaces emoji characters with ascii text"

import_ok = True

try:
   import weechat as w
except:
   print "Script must be run under weechat. http://www.weechat.org"
   import_ok = False

import re
import emoji

def convert_emoji_to_aliases(data, modifier, modifier_data, string):
    string = unicode(string, "utf-8")
    return emoji.demojize(string)

if __name__ == "__main__" and import_ok:
    if w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
                  SCRIPT_DESC, "", "utf-8"):

        w.hook_modifier("irc_in_away", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_cnotice", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_cprivmsg", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_kick", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_knock", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_notice", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_part", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_privmsg", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_quit", "convert_emoji_to_aliases", "")
        w.hook_modifier("irc_in_wallops", "convert_emoji_to_aliases", "")
