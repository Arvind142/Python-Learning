import mysql.connector
from mysql.connector import Error
import utils.Properties

def connect():
    """ Connect to MySQL database """
    conn = None
    map =utils.Properties.readProperty('creds.properties')
    try:
        conn = mysql.connector.connect(host=map.get('Host'),
                                       database=map.get('Database'),
                                       user=map.get('User'),
                                       password=map.get('Password'))
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()