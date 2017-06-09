import MySQLdb
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class DBConnector:
    def command(self, command):
        conn = MySQLdb.connect(host=config['DB']["host"],
                               user=config['DB']["user"],
                               passwd=config['DB']["passwd"],
                               db=config['DB']["db"])
        cur = conn.cursor()
        cur.execute(command)
        conn.commit()
        conn.close()
