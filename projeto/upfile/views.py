from django.shortcuts import render
from pymongo import MongoClient

def index(request):
    return render(request, 'upfile/index.html')

client = MongoClient(
    'mongodb+srv://iadmin:iadmin@iacluster.dvudjrb.mongodb.net/?retryWrites=true&w=majority')

#Define Db Name
dbname = client['upfile']

#Define Collection
collection1 = dbname['arquivos']
collection2 = dbname['users']