import random

with open("violent_python.in", 'r') as fin:
    dataset_in = fin.readlines()

with open("violent_python.out", 'r') as fout:
    dataset_out = fout.readlines()

subset_size = 10
num_subsets = 1
for subset_index in range(num_subsets):
    unique_numbers = random.sample(range(len(dataset_in)), subset_size)
    subset_in = [dataset_in[i] for i in unique_numbers]
    subset_out = [dataset_out[i] for i in unique_numbers]
    
    with open(f"python-subset_{subset_index + 1}.in", 'w') as f_in:
        f_in.writelines(subset_in)
    with open(f"python-subset_{subset_index + 1}.out", 'w') as f_out:
        f_out.writelines(subset_out)
