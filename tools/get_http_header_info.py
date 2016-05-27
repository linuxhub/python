#!/usr/bin/env python
#encoding:utf8
#author: zeping lia

import sys
import pycurl
import re

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

headers = {}

def header_function(header_line):
    # HTTP standard specifies that headers are encoded in iso-8859-1.
    # On Python 2, decoding step can be skipped.
    # On Python 3, decoding step is required.
    header_line = header_line.decode('iso-8859-1')

    # Header lines include the first status line (HTTP/1.x ...).
    # We are going to ignore all lines that don't have a colon in them.
    # This will botch headers that are split on multiple lines...
    if ':' not in header_line:
        return

    # Break the header line into header name and value.
    name, value = header_line.split(':', 1)

    # Remove whitespace that may be present.
    # Header lines include the trailing newline, and there may be whitespace
    # around the colon.
    name = name.strip()
    value = value.strip()

    # Header names are case insensitive.
    # Lowercase name here.
    name = name.lower()

    # Now we can actually record th
    headers[name] = value


if __name__ == "__main__":

    try:
        url = sys.argv[1]
        #url = "http://www.linuxhub.cn"
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL,url)
        c.setopt(c.WRITEFUNCTION, buffer.write)
        # Set our header function.
        c.setopt(c.HEADERFUNCTION, header_function)
        c.perform()
        c.close()

        print ""
        # print headers
        for d, x in headers.items():
            print d + ": " + x
        print ""

    except:
        print "\n请在脚本后面输入url地址!  "
        print "例: %s http://www.linuxhub.org\n" % sys.argv[0]
