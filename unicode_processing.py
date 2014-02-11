#!/usr/bin/python                                                               
       
import json
obj  = json.load(open("scraped_yelp.json"))

for i in obj:
	print obj[1]
	if len(obj[i]["encode_flag"])>0 :
		open("dumped_entries.json","w").write(str(obj[i])+'\n')
        	obj.pop(i)

open("processed_scraped_yelp.json", "w").write(
    json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
)
