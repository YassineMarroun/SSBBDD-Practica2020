
create external table deforestacionTabla (
  WorldBankRegion STRING, Country STRING, ISO3 STRING, wdpaID INT, ParkName STRING, Year INT, OutsideDeforestation DOUBLE, InsideDeforestation DOUBLE) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/cloudera/deforestacionSubSahara';