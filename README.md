#hash-checker

### Instructions
Generate and validate MD5, SHA1 and SHA256 hashes of an `input_file` using  
`python hash_file_checker.py -i input_file -o output_file -t hash`



### Example

#### Compute hash
```
$ python hash_file_checker.py -i test_file.txt

MD5:    6CD3556DEB0DA54BCA060B4C39479839
SHA1:   943A702D06F34599AEE1F8DA8EF9F7296031D699
SHA256: 315F5BDB76D078C43B8AC0064E4A0164612B1FCE77C869345BFC94C75894EDD3
```
#### Check hash validity
```
$ python hash_file_checker.py -i test_input.txt -t 6CD3556DEB0DA54BCA060B4C39479839

File: test_file.txt
MD5 Hash matched:
6CD3556DEB0DA54BCA060B4C39479839
6CD3556DEB0DA54BCA060B4C39479839

The file looks authentic.

```

### License
MIT License

Copyright (c) 2016 xab13r

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
