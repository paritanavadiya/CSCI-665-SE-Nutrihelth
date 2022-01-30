"""
Utility to connect to the database.
"""

from pymongo import MongoClient


def default_database():
    client = MongoClient(
        '####')
    db = client['NutriHelth']
    return db
