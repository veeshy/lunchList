#!/usr/bin/env python
''' Parses yelp API response for things.
'''
import pickle
from random import shuffle

response = pickle.load( open( "restaurants.p", "rb" ) )
f = open('yelpList.txt','w')

for iii in response:
    names = iii['businesses']
    shuffle(names)
    for business in names:
        f.write('%s\n' % (business['name']))


# Prints out some buisness info, example from yelp api python interface
# f.write('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))
# print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s\n' % (business['name'], business['id'], business['rating'],
#                                                                     business['review_count'], ', '.join(business['location']['display_address'])))

f.close()