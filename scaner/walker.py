import os

def walkingByDirs(dir: str) -> list:
	arr = list()

	for root, dirs, files in os.walk(dir):
		for file in files:
			arr.append(os.path.join(root,file))

	return arr