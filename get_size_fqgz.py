import gzip
import glob


def get_uncompressed_size(file):
	fileobj = open(file, 'r')
	fileobj.seek(-8, 2)
	crc32 = gzip.read32(fileobj)
	isize = gzip.read32(fileobj)  # may exceed 2GB
	fileobj.close()
	return isize

for file in glob.glob("*_1.fq.gz"):
	filesize=get_uncompressed_size(file)
	print file, filesize/1024/1024 ## the unit for filesize is M
