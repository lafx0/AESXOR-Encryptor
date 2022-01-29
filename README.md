# AESXOR-Encryptor
Python3 script to AES/XOR encrypt strings and files.

![Banner Image](/images/banner.jpg)

AESXOR-Encryptor is a Python3 based tool able to encrypt strings and files when performing payload and function call obfuscation. It is inspired to Sektor7's MDE course content and scripts originally written in Python2. 
I ported the code to Python3 and added some enhancements that I considered useful. 


## Requirements

The script depends on the `PyCryptodome` package. 
https://pycryptodome.readthedocs.io/en/latest/index.html


To install it:

```
pip3 install pycryptodome
```

## Usage
### String encryption

The script performs encryption on strings and files. 
When no argument is passed, the user can encrypt custom strings selecting between AES and XOR encryption. 

```
python3 aesxorencryptor.py
```

Info: The XOR key can be created by the user, while the AES key is being generated randomly and refreshed after every session. 



### File encryption

In order to encrypt files, the scripts accepts a `.bin` file as an argument and outputs the encrypted file as `testing.ico` in the current directory. 

```
python3 aesxorencryptor.py calc.bin
```


## Acknowledgements

[Sektor7 Institute] (https://institute.sektor7.net/)