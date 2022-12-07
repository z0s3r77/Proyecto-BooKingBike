import pymongo
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

#Modulo que guarda variables importantes

MongoAtlas = pymongo.MongoClient(config["ATLAS_URI"])
MongoKey = config["Key"]

