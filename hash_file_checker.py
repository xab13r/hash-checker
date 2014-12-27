# python hash_file_checker.py -i input_file -o output.txt

import sys
import hashlib
import argparse

def hashfile(filein):
	"""
	Creates an md5 and sha1 hash of any file.
	
	Useful if you have downloaded some file from a mirror and need to check if 
	the downloaded file is the same as the file from the original source 
	by comparing the hash values.

	Assumes that the legitimate publisher of the file has made the hashes 
	publically available on his website (which we implicitly trust).
	"""

	block_size = 2**20
	md5 = hashlib.md5()
	sha1 = hashlib.sha1()

	try:
		with open(filein, 'rb') as f:
			while True:
				data = f.read(block_size)
				if not data:
					break
				md5.update(data)
				sha1.update(data)
  
	except IOError:
		print 'PLease check that the input file is valid'

	md5_digest = md5.hexdigest().upper()
	sha1_digest = sha1.hexdigest().upper()

	return md5_digest, sha1_digest

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest = 'filein', help = 'mandatory input file')
    parser.add_argument('-o', dest = 'fileout', help = 'optional output file')

    args = parser.parse_args()
    if args.filein == None:
    	sys.exit("Please specify the full input file name with -i [input_file]")

    filein = args.filein
    fileout = args.fileout

    print "Hashing in progress"

    md5_digest, sha1_digest = hashfile(filein)

    print 'MD5:\t' + md5_digest
    print 'SHA1:\t' + sha1_digest

    if args.fileout != None:
    	try:
    		with open(fileout, 'w') as outfile:
        		outfile.write('MD5:\t' + md5_digest + '\n')
        		outfile.write('SHA1:\t' + sha1_digest)
        	print 'Hash values written to ' + fileout
        except IOError:
        	print 'Please check that the output file is valid'
