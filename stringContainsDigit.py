""" Check if string contains only digits """
import re

regex = r'^[0-9]+$'
if re.match(regex, ""):
    print("digits only")
else:
    print("not digits only")
