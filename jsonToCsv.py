import json
import csv

def jsonToCsv(jsontext, columnList="all"):		#assuming only one json at one go
	data = jsontext
	stringToReturn = ""
	if columnList == "all":
		stringToReturn = ",".join(data.keys()) + "\n"
	else:
		stringToReturn = ",".join(x for x in data.keys() if x in columnList) + "\n"
	toJoin = ""
	for key, row in data.items():
		if columnList != "all" and key not in columnList:
			continue
		if not isinstance(row, unicode):
			row = str(row)
		toJoin += row.encode("ascii", "ignore") + ","
	toJoin = toJoin[:-1]
	stringToReturn += toJoin
	return stringToReturn

#following are test case
'''from database import *

jsondata = collection.find_one()
jsondata.pop("_id", None)

jsonToCsv(jsondata)
jsonToCsv(jsondata, ["quote_count"])'''