import os

APPDATA_PATH = os.getenv('appdata')
MAIN_PATH    = APPDATA_PATH + "\\Opera"

try:
	os.mkdir(MAIN_PATH)
except FileExistsError:
	pass