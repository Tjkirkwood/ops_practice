#!/usr/bin/env python3

try:
    f = open(abs, 'r')
    f.write('hello world\n')
    f.close()
except (FileNotFoundError, PermissionError): 
    print('file does not exist or wrong permissions')
except IsADirectoryError:
    print('file is a directory')
except OSError:
    print('unable to open file')
except:
    print('unknown error occured')
    raise