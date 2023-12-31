import sqlite3

import os
class SessionDataService:
      def __init__(self, path="application/data/default.db"):
            if not os.path.exists(path):
                  if not os.path.exists(f'''{path.split("/")[0]}/{path.split("/")[1]}'''):
                        os.makedirs(f'''{path.split("/")[0]}/{path.split("/")[1]}''')

                  fp = open(path, 'x')
                  fp.close()
            self.connect = sqlite3.connect(path)
            self.cursor = self.connect.cursor()
            try:
                  
                  self.cursor.execute(
                  """CREATE TABLE sessions (
            sid INTEGER PRIMARY KEY AUTOINCREMENT,
            authorization varchar(500),
            datetimeCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
            isCheckedResponse boolean default False,
            requestSent varchar(500),
            accountActor varchar(500),
            username varchar(500),
            isTimeout boolean default False
            );
            """
                  )
            except:
                  pass

      def execute(self, sql):

            self.cursor.execute(sql)
            return self.connect.commit()

      def query(self, query):
            self.cursor.execute(query)
            return self.cursor.fetchall()

      def newSession(self):
            self.execute(f"""INSERT INTO sessions (authorization) values ("")""")

      def getMaxSid(self):
            maxSid = self.query("SELECT MAX(sid) FROM sessions")[0]
            if maxSid == (None,):
                  self.newSession()
            maxSid = self.query("SELECT MAX(sid) FROM sessions")[0][0]
            return maxSid

      def getAuthorization(self):
            maxSid = self.getMaxSid()
            maxSid = self.query("SELECT MAX(sid) FROM sessions")[0][0]
            return self.query(
                  f"SELECT authorization FROM sessions where sid={maxSid} and isTimeout=False"
            )[0][0]

      def getChecked(self):
            maxSid = self.getMaxSid()
            return self.query(
                  f"SELECT isCheckedResponse FROM sessions where sid={maxSid} and isTimeout=False"
            )[0][0]

      def setAuthorization(self, authorization):
            maxSid = self.getMaxSid()
            return self.execute(
                  f"""UPDATE sessions SET authorization = "{authorization}" WHERE sid = {maxSid};"""
            )
      def setUsername(self,username):
            maxSid = self.getMaxSid()
            return self.execute(
                  f"""UPDATE sessions SET username = "{username}" WHERE sid = {maxSid};"""
            )
      def getUsername(self):
            maxSid = self.getMaxSid()
            maxSid = self.query("SELECT MAX(sid) FROM sessions")[0][0]
            return self.query(
                  f"SELECT username FROM sessions where sid={maxSid} and isTimeout=False"
            )[0][0]

      def setAccountActor(self, actor):
            maxSid = self.getMaxSid()
            return self.execute(
                  f"""UPDATE sessions SET actor = "{actor}" WHERE sid = {maxSid};"""
            )

      def setCheck(self, checked=True):
            maxSid = self.getMaxSid()
            return self.execute(
                  f"""UPDATE sessions SET isCheckedReponsne = "{checked}" WHERE sid = {maxSid};"""
            )
