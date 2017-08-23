import requests

#inputs here#
state1 = 'OK'
state2 = 'TX'
state3 = 'NE'

commodity = 'WHEAT'
subcommodity = 'WHEAT - ACRES HARVESTED'


#foundation of the api here#
API_BASE = 'http://quickstats.nass.usda.gov/api/api_GET?'
API_PAYLOAD = {'key': 'C2352E9E-5773-358B-9216-4CABA0734896',
               'commodity_desc': (commodity) ,
               'state_alpha': ( state1 , state2 , state3) ,
               'year': '2017',
               'short_desc': ( subcommodity ) #could remove
              }

apidata = requests.get(API_BASE, params=API_PAYLOAD)
apidata = apidata.json()


###Output Printing

for info in apidata['data']:
    print(info['year'],
          info['state_name'],
          info['short_desc'],
          info['Value'],
          info ['unit_desc']
          )
