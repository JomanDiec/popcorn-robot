import numpy as np

new_data = []
new_time = []

with open('assem.txt', 'r') as file: 
  for line in file:
    data = line.split()
    new_data.append(data)
   
with open('time_a.txt', 'r') as file: 
  for line in file:
    time_data = line.split()
    new_time.append(time_data)

# for time in new_data:
#   print(time)
    
merge_data = []

for time in reversed(new_time):
  for data in reversed(new_data):
    if len(new_time) == 1:
      merge = data + time
      merge_data.insert(0,merge)
      new_data.pop(len(new_data)-1)
    elif float(time[0]) >= float(data[0]) > float(new_time[len(new_time)-2][0]):
      merge = data + time
      merge_data.insert(0,merge)
      new_data.pop(len(new_data)-1)
    elif float(data[0]) > 77.039:          # can be improve by compairing to the last time on time_a == to data (looped)
      new_data.pop(len(new_data)-1)
    elif len(new_time) > 0:
      new_time.pop(len(new_time)-1)
      break

f = open("merge_data.txt", "a")

for data in merge_data:
  f.write(str(data) + '\n')

f.close()


# print(str(len(merge_data)) + ' items in list')
# print(new_data[0] + new_time[0])
  