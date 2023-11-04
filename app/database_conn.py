import psycopg2
from psycopg2.extras import RealDictCursor


def connect():
    try:
        conn = psycopg2.connect(host='localhost',database='hospital_management_system',
                                user='postgres',password='haggaiikez123',cursor_factory=RealDictCursor)
        cur=conn.cursor()
        print('connected to the database successfully!!!!')
        return cur,conn

    except Exception as error:
        print ('connection to database failed')
        print('error',error) 

        return error


