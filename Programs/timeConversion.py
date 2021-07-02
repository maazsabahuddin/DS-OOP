def timeConversion(s):

    list = s.split(':')
    tf_hour_format = ''
    if "PM" in list[2]:
        if list[0] == "12":
            tf_hour_format = str(list[0]) + ':' + str(list[1]) + ':' + str(list[2].replace('PM', ''))
        else:
            tf_hour_format = str(int(list[0]) + 12) + ':' + str(list[1]) + ':' + str(list[2].replace('PM', ''))
    elif "AM" in list[2]:
        if list[0] == "12":
            list[0] = "00"
        tf_hour_format = str(list[0]) + ':' + str(list[1]) + ':' + str(list[2].replace('AM', ''))

    return tf_hour_format


# print(timeConversion("07:05:35PM"))
# print(timeConversion("12:40:22AM"))
print(timeConversion("12:40:22PM"))
