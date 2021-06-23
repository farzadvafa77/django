from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response



def get_data_base():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client['test']


if __name__ == "__main__":
    dbname = get_data_base()

collection_name = dbname['test_collection']

Data={moile_name:  ,;password:   ,submit_date:  ,last_login_date: ,email:  ,}
