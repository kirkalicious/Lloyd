
class BigramDictionary:

  def __init__(self,fn):
    self.first = {}
    self.second = {}
    
    f = open(fn, "r")
    for line in f:
      rec = line.split()

      # Surely there's a better pattern here
      if not self.first.has_key(rec[0]):
        self.first[rec[0]] = [] 
      if not self.second.has_key(rec[1]):
        self.second[rec[1]] = []

      self.first[rec[0]].append(rec) 
      self.second[rec[1]].append(rec)




