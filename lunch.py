#!/usr/bin/env python
''' Simple script that access the yelp API and finds the 400 `best' restaurants within a bounding lat/long box.
    The queried responses are saved to a file for parsing.

    API keys stored in keys or just write yours in at the preemble
'''
from yelpapi import YelpAPI
import pickle
import keys

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
token = keys.token
token_secret = keys.token_secret

yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)

"""
    Example search by location text and term. Take a look at http://www.yelp.com/developers/documentation/v2/search_api for
    the various options available.
"""
# response = yelp_api.search_query(term='restaurants', location='idaho falls, ID', sort=1, offset=20)
# print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))
# for business in response['businesses']:
#     print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s' % (business['name'], business['id'], business['rating'],
#                                                                            business['review_count'], ', '.join(business['location']['display_address'])))
#
#

response = []

for offset in range(0,400,20):
    tmp = yelp_api.search_query(term='restaurants', bounds='43.446888,-112.097128|43.542030,-111.931131', sort=0, offset=offset,radius_filter=8000)
    response.append(tmp)
    print(tmp)

pickle.dump(response, open('restaurants.p','wb'))