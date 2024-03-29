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


    def insertCookieFirefox (self, cookie):
        cookiesVal = (cookie['domain'],cookie.key, cookie.value, 
                cookie["domain"],cookie['path'], cookie['expires'], 
                cookie['secure'], cookie['httponly'])

        with self.conn:
            cur = self.conn.cursor()
            try: 
                cur.execute("INSERT INTO moz_cookies ('baseDomain', 'name', \
                        'value', 'host', 'path', 'expiry', 'isSecure', \
                        'isHttpOnly') \
                        VALUES (?,?,?,?,?,?,?,?)", cookiesVal)
                self.conn.commit()
            except sql.Error, e:
                print "Error %s:" % e.args[0]
                sys.exit(1)
            

    def closeConnection(self):
        self.conn.close()

            
    def setDb(self, _dbPath):
        self.dbPath = _dbPath

