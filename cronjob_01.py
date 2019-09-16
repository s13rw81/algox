import sqlite3
from datetime import datetime
class cronjob():

    def __init__(self):
        self.conn = sqlite3.connect('cron_db.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS cron_table_01(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, message TEXT)")

    def insert_data(self):
        for _ in range(10):
            d = datetime.utcnow().ctime()
            m = 'Hello World!'
            self.c.execute("INSERT INTO cron_table_01 (date, message) VALUES (?, ?);", (d, m))
        self.conn.commit()
            
    # def showtime(self):
    #     self.c.execute('SELECT * FROM cron_table_01')
    #     result = self.c.fetchall()
    #     for row in result:
    #         print('ID: {}\tDATE: {}\tMessage: {}'.format(row[0], row[1], row[2]))



    def shutdown(self):
        self.c.close()
        self.conn.close()


if __name__ == '__main__':
    job = cronjob()
    job.insert_data()
    # job.showtime()
    job.shutdown()