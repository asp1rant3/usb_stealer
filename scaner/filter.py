WORDS_TO_DEL = ["system", "found", "file00", ".chk", ".dat", "guid", "volume"]

def firstCleaningStep(elem: str) -> list:
	for word in WORDS_TO_DEL:
		if word in elem.lower():
			return False
	return True

def lastCleaningStep(arr: list) -> list:
	return list(filter(firstCleaningStep, arr))
