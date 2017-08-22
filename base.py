import requests


state1 = 'OK'
state2 = 'TX'
state3 = 'NE'

#stateabbrev1 = (state1 + ', ' + state2 + ', ' + state3)
#stateabbrev = "".join(stateabbrev1)
#print (stateabbrev)

commodity = 'WHEAT'


API_BASE = 'http://quickstats.nass.usda.gov/api/api_GET?'
API_PAYLOAD = {'key': 'C2352E9E-5773-358B-9216-4CABA0734896',
               'commodity_desc': ('WHEAT', 'CORN' ) ,
               'state_alpha': ( state1 , state2 , state3) ,
               'year': '2017',
               'short_desc': ( 'WHEAT - ACRES HARVESTED' , 'CORN - ACRES HARVESTED' )
              }

apidata = requests.get(API_BASE, params=API_PAYLOAD)
apidata = apidata.json()

for info in apidata['data']:
    print(info['year'],
          info['state_name'],
          info['short_desc'],
          info['Value'])