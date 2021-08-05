import pymssql

################## Main Function ##############################
def main():

    # print('This is '+ __name__)
    
    conn = pymssql.connect(server='FLOKI', user='', password='', database='testDB')

 

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM testDB.dbo.Take')

    for row in cursor:
        print(row)



if __name__ == '__main__':
    main()