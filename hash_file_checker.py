#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import argparse


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
        print 'PLease check that the input file is valid'

    return md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='input_file', help='mandatory input file')
    md5_digest, sha1_digest, sha256_digest = hashfile(
        parser.parse_args().input_file)

    print 'MD5:\t' + md5_digest.upper()
    print 'SHA1:\t' + sha1_digest.upper()
    print 'SHA256:\t' + sha256_digest.upper()
