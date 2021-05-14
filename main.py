import db_operations 

def mainFunc():

    db = db_operations.DBOperations()

    #open and read the file
    with open ("Raw_data.txt", "r") as myfile:
        data = myfile.read().splitlines()

    main_data = []


    # format the data into a tuple
    for each_line in data:
        each_line = each_line[1:]
        parts = each_line.split('|')
        
        #remove the header because we 
        if parts[0] == "H" :
            pass
        #insert the data into an array called main_data
        else:
            parts[3] = int(parts[3])
            parts[4] = int(parts[4])
            parts[9] = int(parts[9])
            main_data.append(tuple(parts[1:]))

    #insert the rows one by one to respective tables
    for each_data in main_data:
        table_name = "Table_" + each_data[7]
        db.createTable(table_name) #it ignores in case if table already exists
        db.insertData(table_name,str(each_data))
        db.closeConnection()


if __name__ == '__main__':
    mainFunc()