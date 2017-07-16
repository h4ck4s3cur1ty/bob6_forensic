import sys
import pythonwhois
import json
import datetime
import yaml

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

filename = sys.argv[0]

if len(sys.argv) is 1:
  exit('Usage : ' + filename + ' filename ')

domain_list = sys.argv[1]

f = open(domain_list, 'r')
line = f.readlines()

for name in line:
	jsonString = pythonwhois.get_whois(name)

	a = json.dumps(jsonString, default=datetime_handler)
	d = yaml.load(a)

	with open(name.replace("\n","") + ".json", 'w') as outfile: 
   		json.dump(d, outfile)