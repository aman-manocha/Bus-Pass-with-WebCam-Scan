#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##===============================================

class DatabaseUtility: 
        def __init__(self, database, tableName):
                self.db = database
                self.tableName = tableName

               
                self.cnx = mysql.connector.connect(user = 'root',
                                                   password = 'P&s2103071996',
                                                   host = '127.0.0.1',
                                                   db = database)
                self.cursor = self.cnx.cursor()
                self.ConnectToDatabase()
                ##self.cursor.execute('SELECT * FROM ' + self.tableName + ';')
                ##for f in self.cursor.fetchall():
                        ##print(f)
        def ConnectToDatabase(self):
                try:
                        self.cnx.database = self.db
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_BAD_DB_ERROR:
                                self.CreateDatabase()
                                self.cnx.database = self.db
                        else:
                                print(err.msg)


        def GetTable(self):
                return self.RunCommand("SELECT * FROM %s;" % self.tableName)

        def GetColumns(self):
                return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName)

        def RunCommand(self, cmd):
                print ("RUNNING COMMAND: " + cmd)
                try:
                        self.cursor.execute(cmd)
                except mysql.connector.Error as err:
                        print ('ERROR MESSAGE: ' + str(err.msg))
                        print ('WITH ' + cmd)
                try:
                        msg = self.cursor.fetchall()
                except:
                        msg = self.cursor.fetchone()
                return msg

        def AddEntryToTable(self, Name, Address, Mobile ,Password):
		
                cmd = " INSERT INTO " + self.tableName + " (Name, Address, Phone no., Password) )"
                cmd += " VALUES ('%s', '%s' , '%s' , '%s');" % (Name, Address, Mobile, Password)
                self.RunCommand(cmd)
        
        def __del__(self):
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close() 
                
        
        

        
                
	

##===============================================
##===============================================


if __name__ == '__main__':
	db = 'buspass'
	tableName = 'information'

	dbu = DatabaseUtility(db, tableName)

	dbu.AddEntryToTable ('asdf', 'asdf','asdf', 'asdf')
	print (dbu.GetColumns())
	print (dbu.GetTable())
	
