
# Dataset_1 header = Time, joint-angles
# Dataset_2 header = Time, Task, State


assem_list = []
time_list = []

with open("assem.txt", "r") as file: 
  for data in file:
    # print(data)
    angles_line = data.split() 
    assem_list.append(angles_line)

with open("time_a.txt", "r") as file: 
  for data in file:
    # print(data)
    time_line = data.split() 
    time_list.append(time_line)
    # pass

for assem in assem_list:
  # print(assem[0])
  is_found = False

  for time in time_list:
    # print(time[0])
    if float(assem[0]) <= float(time[0]):
      # print(assem[0] + " " + time[0])
      assem.insert(1, time[1])
      assem.insert(2, time[2])

      is_found = True
      break

  if is_found == False:
    # print(assem)
    assem_list.remove(assem)

    
# for x in assem_list[4810:4821]:
#   if float(x[0]) <= float(77.039):
#     print("YES!!!!")
#   else:
#     print("NOOOO")
#   print(x)
# # print(assem_list[4816:4821])
# print("success")



with open('results.txt', 'w') as file:
    for assem in assem_list:      
      # assem_list = assem.split() 
      
      result = ""
      for angles in assem:
        result += angles + " "
        
      file.write(str(result) + "\n")
