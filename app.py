import pymssql
import argparse



def parse_args():
    parser  =  argparse.ArgumentParser()
    parser.add_argument('name', type=str, help='The table name')
    args = parser.parse_args()
    return args



def db_connection():   
    try:
        conn = pymssql.connect(server='FLOKI', user='', password='', database='testDB')
    except:
        print("Db connection Error") 
    return conn



def select_all(conn, tbl_name: str):
    try:
        # cursor = conn.cursor()
        with conn.cursor() as cursor:        
            cursor.execute('SELECT * FROM testDB.dbo.{}'.format(tbl_name))
            table =[row for row in cursor]
            print(*table, sep='\n')

    except:
        print("Error in the cursor") 

    finally:
        # cursor.close()
        conn.close()
        


def main():
    conn = db_connection()
    arg_values = parse_args()
    select_all(conn, arg_values.name )
    
    



if __name__ == '__main__':
    main()



