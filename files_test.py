import pickle, os
pickle.dump('hi', open('awooga', 'w'))
word = pickle.load(open('awooga'))
print word