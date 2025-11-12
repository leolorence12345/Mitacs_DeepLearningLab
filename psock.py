#import re

#def function1(x):
#    with open("list.txt", "w") as f:
#        for s in x:
#            f.write(str(s) +"\n")
#    
## def split_by_two_delimiters(string, delimiter1, delimiter2,delimiter3):
##     pattern = re.compile(f"{re.escape(delimiter1)}|{re.escape(delimiter2)}|{re.escape(delimiter3)}")
##     result = re.split(pattern, string)
##     return result

# list_pos = []
position = ""
with open("list.txt", "r") as f:
 for line in f:
   position  = position+line
print(position)
positions = position.split("Position_")[1:]
# print(positions)

result = []

for position in positions:
   # Extract the values from the substring
   values = position.split(" ")
   cordinates = values[1].split("(")[1].split(",")
   # print(values)
   # print(cordinates)
   x = float(cordinates[0])
   y = float(cordinates[1])
   z = float(cordinates[2])
   # print(values[3].split(')')[0])
#    break
   
#    break
#    result.append((x,y,z))
   # break
 
# print(result)
   
   # list_pos.append(split_by_two_delimiters(str(line.strip()),",","(",")"))

   


# def remove_empty_strings_and_group(lst):
#     cleaned_list = [item for sublist in lst for item in sublist if item]
#     tuples_list = [(float(cleaned_list[i]), float(cleaned_list[i+1]), float(cleaned_list[i+2]), float(cleaned_list[i+3])) for i in range(0, len(cleaned_list), 4)]
#     return tuples_list

# print(len(remove_empty_strings_and_group(list_pos)))

# def testing_f(arg):
#     print("hello_world")

