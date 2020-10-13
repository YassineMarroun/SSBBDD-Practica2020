#!/usr/bin/env python
 
import sys
 
for line in sys.stdin:
	data = line.strip().split(",")
	if len(data) == 8:
		WorldBankRegion, Country, ISO3, wdpaID, ParkName, Year, OutsideDeforestation, InsideDeforestation = data
		if ParkName == "Rusizi" and Year == "2011":
			print ("%s %s" % (ParkName, InsideDeforestation))