# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/school.sqlite')
c = conn.cursor()


def students_from_city(db, city):
    """return a list of students from a specific city"""
    query ="""SELECT s.id, s.first_name, s.last_name
            FROM students s
            WHERE s.birth_city = ?
            """
    db.execute(query, (city, ))
    rows = db.fetchall()
    return rows
