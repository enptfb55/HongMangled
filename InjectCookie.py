#!/usr/bin/python

import sqlite3 as sql
import sys 
import Cookie

class InjectCookie:

    def __init__(self, dbPath):
        self.dbPath = dbPath

    def connectToDb(self):
        try:
            self.conn = sql.connect(self.dbPath)

            cur = self.conn.cursor()
            cur.execute('SELECT SQLITE_VERSION()')

            data = cur.fetchone()

            print "SQLITE version: %s" % data
        except sql.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)


    def inserCookie(cookie = Cookie.SimpleCookie()):
        cookieVal = (cookie.creation_utc, cookie.host_key, cookie.name,
                cookie.value, cookie.path, cookie.expires_utc, cookies.secure,
                cookie.httponly, cookie.last_access_utc, cookie.has_expires,
                cookie.persistant)

        with self.conn:
            cur.execute("INSERT INTO cookies VALUES (?,?,?,?,?,?,?,?,?)")
            
