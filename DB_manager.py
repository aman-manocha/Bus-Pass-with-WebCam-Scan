#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##===============================================

class DatabaseUtility: 
        def __init__(self, database, tableName):
                #self.db = database
                self.tableName = tableName

               
                self.cnx = mysql.connector.connect(user = 'root',
                                                   password = 'P&s2103071996',
                                                   host = '127.0.0.1',
                                                   db = database)
                self.cursor = self.cnx.cursor()

                #self.ConnectToDatabase()
                #self.CreateTable()
                self.cursor.execute('SELECT * FROM ' + self.tableName + ';')
                for f in self.cursor.fetchall():
                        print(f)

        
                
	

##===============================================
##===============================================


if __name__ == '__main__':
	db = 'buspass'
	tableName = 'information'

	dbu = DatabaseUtility(db, tableName)

	# dbu.AddEntryToTable ('asdf', 'asdf')
	# print (dbu.GetColumns())
	# print (dbu.GetTable())
	
