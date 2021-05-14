import sqlite3

class DBOperations():
    def __init__(self):
        self.conn = sqlite3.connect('test.db')

    def createTable(self,table_name):
        try :
            self.conn.execute('''CREATE TABLE IF NOT EXISTS ''' + table_name + 
                        ''' (
                            Customer_Name VARCHAR(255) PRIMARY KEY NOT NULL,
                            Customer_Id VARCHAR(18) NOT NULL,
                            Open_Date DATE(8) NOT NULL,
                            Last_Consulted_Date DATE(8),
                            Vaccination_Id Type CHAR(5),
                            Dr_Name CHAR(255),
                            State CHAR(5),
                            Country CHAR(5),
                            Post_Code INTEGER(5),
                            DOB DATE(8),
                            Is_Active CHAR(1)
                        );''')
        except:
            print ('Some error occured')

    def insertData(self,table_name,data):
        try:
            self.conn.execute('''INSERT INTO ''' + table_name + '''(Customer_Name, 
            Customer_Id, Open_Date, Last_Consulted_Date, Vaccination_Id, 
            Dr_Name,State, Country,DOB, Is_Active) Values''' + data +''';''')
            self.conn.commit()
        except:
            print("Some error occurred in inserting data")

            
    def closeConnection(self):
        self.conn.close()
   
