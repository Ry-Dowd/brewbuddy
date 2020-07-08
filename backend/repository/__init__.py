class Repository(object):
  def __init__(self, adapter=None):
    self.client=adapter()

  def find_all(self, selector):
    return self.client.find_all(selector)

  def find(self, selector):
    return self.client.find(selector)

  def create(self, brew):
    return self.client.create(brew)

  def update(self, selector, brew):
    return self.client.update(selector, brew)
  
  def delete(self, selector):
    return self.client.delete(selector)