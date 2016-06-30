# python hash_file_checker.py -i input_file -o output.txt
# -*- coding: utf-8 -*-

import hashlib
import argparse
import sys


def hashfile(input_file):
    """
    Creates an MD5, SHA1 and SHA256 hash of any file.

    This is useful if you have downloaded a file and need to compare the hash
    values with the values published by the publisher, to ensure that it has
    not been tampered with.
    """

    block_size = 2**20
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    try:
        with open(input_file, 'rb') as f:
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
                sha256.update(data)

    except IOError:
        print('Please check that the input file is valid\n')

    md5_digest = md5.hexdigest().upper()
    sha1_digest = sha1.hexdigest().upper()
    sha256_digest = sha256.hexdigest().upper()

    return md5_digest, sha1_digest, sha256_digest


if __name__ == '__main__':

    # Parse arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input_file', help='mandatory input file')
    parser.add_argument('-o', dest='output_file', help='optional output file')
    parser.add_argument('-t', dest='target', help='optional provided hash')

    args = parser.parse_args()

    # Check validity of input file
    if args.input_file is None:
        sys.exit("\nPlease specify the input file with -i [input_file]\n")

    filein = args.input_file
    fileout = args.output_file
    target = args.target

    # Compute hash
    md5_digest, sha1_digest, sha256_digest = hashfile(filein)

    # If hash has been provided, compare it to computed hash
    if target is not None:
        try:
            target = target.upper()

            if (target == sha1_digest):
                print('\nFile:\t%s' % filein)
                print('SHA1 Hash matched:')
                print(sha1_digest)
                print(target)
                print('The file looks authentic.\n')

            elif (target == md5_digest):
                print('\nFile:\t%s' % filein)
                print('MD5 Hash matched:')
                print(md5_digest)
                print(target)
                print('The file looks authentic.\n')

            elif (target == sha256_digest):
                print('\nFile:\t%s' % filein)
                print('SHA256 Hash matched:')
                print(sha256_digest)
                print(target)
                print('The file looks authentic.\n')

            else:
                print('\nFile:\t%s' % filein)
                print('WARNING: Try to redownload the file.\n')

        except IOError:
            print('Please check the hash you provided\n')

    else:
        print("\nFile:\t%s" % filein)
        print('MD5:\t%s' % md5_digest)
        print('SHA1:\t%s' % sha1_digest)
        print('SHA256:\t%s\n' % sha256_digest)
