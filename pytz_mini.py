from tzfile import build_tzinfo

def timezone(zone):
	fp = open(zone, 'rb')
	tzinfo = build_tzinfo(zone, fp)
	fp.close()
	return tzinfo
