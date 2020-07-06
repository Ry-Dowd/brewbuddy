from repository import Repository
from repository.mongo import MongoRepository
from .schema import BrewSchema

class Service(object):
  def __init__(self, user_id, repo_client=Repository(adapter = MongoRepository)):
    self.repo_client = repo_client
    self.user_id = user_id

    if not user_id:
      raise Exception("User id not provided")

  def find_all_brews(self):
    brews = self.repo_client.find_all({'public': True})
    return [self.dump(brew) for brew in brews]

  def find_own_brews(self):
    brews = self.repo_client.find_all({'author_id':self.user_id})
    return [self.dump(brew) for brew in brews]

  def find_brew(self, brew_id):
    brew = self.repo_client.find({brew_id})
    if brew.author_id == self.user_id:
      return self.dump(brew)
    elif brew.public:
      return self.dump(brew)
    else:
      raise Exception("You don't have access to that recipe")

  def create_brew_for(self, brew):
    self.repo_client.create(brew)
    return self.dump(brew.data)

  def update_brew_with(self, brew_id, brew):
    records_affected = self.repo_client.update({'author_id':self.user_id, 'brew_id':brew_id}, brew)
    return records_affected > 0

  def delete_brew_for(self, brew_id):
    records_affected = self.repo_client.delete({'author_id':self.user_id, 'brew_id':brew_id})
    return records_affected > 0

  def dump(self, data):
    return BrewSchema(exclude=['author_id']).dump(data).data

  
  