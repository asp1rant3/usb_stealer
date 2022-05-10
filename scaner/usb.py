import psutil

def findUSB() -> list:
	# This func scans the drivers               (for disk in psutil.disk_partitions) 
	# and gets every driver memory information. (psutil.disk_usage)
	# If total count more than 64 GB            (if _total <= 64)
	# it's going to be USB drive.               (arr.append( disk.device ))
	arr = list()

	for disk in psutil.disk_partitions():
		try:
			memory   = psutil.disk_usage( disk.device )
			_total   = memory.total/2**30 # int   (GB)
			_percent = memory.percent     # float (%)

			if _total <= 64:
				arr.append( disk.device )
		except PermissionError:
			""" Cdroms throws this error, cause you cannot scan it """
			continue

	return arr