import sqlite3
import os.path

conn = sqlite3.connect(os.path.dirname(__file__) +'/../db/members.db')