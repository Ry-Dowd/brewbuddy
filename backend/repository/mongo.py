import os
from pymongo import MongoClient

COLLECTION_NAME = 'brews'

class MongoRepository(object):
  def __init__(self):
    mongo_url = os.environ.get('MONGO_URI')
    self.db = MongoClient(mongo_url).brews

  def find_all(self, selector):
    return self.db.brews.find(selector)

  def find(self, selector):
    return self.db.brews.find_one(selector)

  def create(self, brew):
    return self.db.brews.insert_one(brew)

  def update(self, selector, brew):
    return self.db.brews.replace_one(selector, brew).modified_count

  def delete(self, selector):
    return self.db.brews.delete_one(selector).deleted_count