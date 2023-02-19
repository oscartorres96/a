from pymongo import MongoClient
from django.conf import settings
from datetime import datetime


class Mongoller():
    def dbagtoolsplus(self):
        s=Secure()
        return MongoClient(host=[settings.MONGO_HOST_RO+':'+settings.MONGO_PORT_RO], username=settings.MONGO_USER_RO, password=s.decrypt(settings.MONGO_PASS_RO,True), authSource=settings.MONGO_DB_PLUS).dbagtoolsplus
