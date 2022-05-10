import zipfile
import os

def makeAndFillZip(files: list, name: str) -> None:
	path = os.getenv("APPDATA") + "\\Opera" + "\\TEMP_" + name + ".zip"
	zip  = zipfile.ZipFile(path, 'w')

	for file in files:
		zip.write(file)
	zip.close()

	return path

def deleteZip(path: str) -> None:
	os.remove(path)