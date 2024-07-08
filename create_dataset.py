
#Open the file .IN o .OUT
with open("python-train.in", 'r') as file:
        content = file.readlines()

#Continue the code...

with open("dataset_python.in",'w') as f:
        f.write(combined_lines)

#Another mode

with open("python-train.out", 'r') as file:
        content = file.readlines()

list_of_codes=list()

for i in content:
    list_of_codes.append(i)

#Continue the code...

with open("dataset_python.out",'w') as f:
      for c in list_of_codes:
        f.write(c)

#For the creation of the prompt, it is recommended to separate each "sample", i.e. each intent and each snippet, with a comma (just as is done in Python with the list for example)
#Consequently, there are two solutions: print list_of_codes/list_of_descriptions or, when saving to the .IN or .OUT file, add a comma at the end of each line




