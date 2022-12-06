import pymongo
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

MongoAtlas = pymongo.MongoClient(config["ATLAS_URI"])

