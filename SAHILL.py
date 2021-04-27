#!/usr/bin/python

# -*- coding: utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = ['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]']

def keluar():

    print '\x1b[1;91mExit'

    os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'

    x = x.replace('!0', '\x1b[0m')

    sys.stdout.write(x + '\n')

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.0012)

logo = """		\033[1;91m               DDD      KKK      GGGGG

\033[1;91m██████░░    ░░  ██      ██  ░   ██████░░░

\033[1;91m█              ██    ░░  ██   ██     ░ █               █░░░

\033[1;91m█              ██    ░░  ████        ░ █                 ░░░   

\033[1;91m█              ██    ░░  ████        ░ █        ███░░░   

\033[
