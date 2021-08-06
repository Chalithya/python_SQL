import pymssql
import argparse



def parse_args():
    parser  =  argparse.ArgumentParser()
    parser.add_argument('name', type=str, help='The table name')
    args = parser.parse_args()
    return args



def db_connection():   
    conn = pymssql.connect(server='FLOKI', user='', password='', database='testDB')
    return conn



def select_all(conn, tbl_name: str):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM testDB.dbo.{}'.format(tbl_name))
    for row in cursor:
        print(row)




def main():
    conn = db_connection()
    arg_values = parse_args()
    select_all(conn, arg_values.name )
    



if __name__ == '__main__':
    main()