
#Apertura del file .IN o .OUT
with open("python-train.in", 'r') as file:
        content = file.readlines()

#Continua il codice...

with open("dataset_python.in",'w') as f:
        f.write(combined_lines)

#Ulteriore modo

with open("python-train.out", 'r') as file:
        content = file.readlines()

list_of_codes=list()

for i in content:
    list_of_codes.append(i)

#Continua il codice...

with open("dataset_python.out",'w') as f:
      for c in list_of_codes:
        f.write(c)




