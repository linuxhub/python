#!/usr/bin/env python
#encoding:utf8
#author: zeping lai

import sys
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--file", dest="filename",
                  help="rsync logs file", metavar="FILE")

parser.add_option("-d", "--domain", dest="domain",
                  help="domain list", metavar="DOMAIN")


args= parser.parse_args()[0]
if args.filename and args.domain != None:
    filename = args.filename
    domain = args.domain
else:
    print "\nPlease see --help for more details.\n"
    sys.exit(-1)
    
print "FileName: " + str(filename)
print "Doiam: " + str(domain)

