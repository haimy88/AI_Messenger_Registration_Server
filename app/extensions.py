from flask_cors import CORS
from pymongo import MongoClient
import os

mongo_client = MongoClient(os.getenv("MONGO_URI"))

cors = CORS()
