import time


def epoch_to_exif_format(time_in_epoch):
    exif_string = time.strftime("%Y:%m:%d %H:%M:%S", time.gmtime(int(time_in_epoch)))

    return exif_string.encode('ascii')


def exif_format_to_epoch(time_in_exif_format):
    # Since exif does not have timezone information, let's just assume that it's local time
    ascii_string = time_in_exif_format.decode('ascii')

    # Duct taping...
    if ": " in ascii_string:
        ascii_string = ascii_string.replace(": ", ":0")

    if '\x00' in ascii_string:
        ascii_string_parts = ascii_string.split('\x00')
        ascii_string = ascii_string_parts[1] + ":" + ascii_string_parts[0]

    hour_segment = ascii_string.split(' ')[1].split(':')[0]
    if hour_segment == "24":
        ascii_string = ascii_string.replace(" 24", " 00")

    exif_time = time.strptime(ascii_string, "%Y:%m:%d %H:%M:%S")

    return int(time.mktime(exif_time))
