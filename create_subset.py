import random

#Apertura del file .IN o .OUT
with open("python-train.in", 'r') as fin:
        dataset = fin.readlines()

subsets=[]
num_subsets=50
subset_size=30
for i in range(num_subsets):
        subset=random.sample(dataset,subset_size)
        subsets.append(subset)
        with open("python-subset_"+ str(i+1) +".in", 'w') as fin:
            for j in range(len(subset)):
                fin.write(subsets[i][j])   






