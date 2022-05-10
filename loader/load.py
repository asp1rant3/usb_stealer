from mega import Mega
from requests.exceptions import ConnectionError

def load(path: str) -> str:
	mega = Mega()
	m = mega.login("ВАШ ЛОГИН НА mega.nz", "ВАШ ПАРОЛЬ НА mega.nz")
	file = m.upload(path)
	link = m.get_upload_link(file)
	del m, mega

	return link