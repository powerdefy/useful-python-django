import itertools
import re
import sys
import unicodedata

all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {"Cc", "Cf"}
control_chars = "".join(c for c in all_chars if unicodedata.category(c) in categories)

control_char_re = re.compile("[%s]" % re.escape(control_chars))


def clean_string(s):
    return control_char_re.sub("", s)
