# Runner script for all modules
from datetime import datetime
from load_data import load_sensor_data
from house_info import HouseInfo
from temperature_info import TemperatureData



##############################
# Do not remove these two lines
# They are needed to validate your unittest

data = []
print("Sensor Data App")

##############################

# Module 1 code here:
data = load_sensor_data()
print("Loaded records: {0}".format(len(data)))

# Module 2 code here:
house_info = HouseInfo(data)
test_area = 1

recs = house_info.get_data_by_area('id',test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))

test_date = datetime.strptime('05/09/20', '%m/%d/%y')
recs = house_info.get_data_by_date("id",test_date)
print("\nHouse sensor records for date {} = {}".format(test_date, len(recs)))
    
  

# Module 3 code here:
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area = test_area)
print("\nHouse Temperature sensor records for area {} = {}".format(test_area, len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))

recs = temperature_data.get_data_by_date(rec_date = test_date)
print("\nHouse Temperature sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))

# Module 4 code here:

# Module 5 code here: