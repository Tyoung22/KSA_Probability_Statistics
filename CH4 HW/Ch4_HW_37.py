from collections import Counter
import random
import numpy as np

sample_size = 100000

def count_couple(L):
    L = Counter(L);cnt=0
    for i in range(1,101):
        if L[i]==2:cnt+=1
    return cnt

cnt_list = []
for _ in range(sample_size):
    couples = [i for i in range(1,101)]*2
    #print(count_couple(couples))
    random_indices = set(random.sample(range(200), 50))
    couples = [item for idx, item in enumerate(couples) if idx not in random_indices]
    cnt_list.append(count_couple(couples))

ans = np.mean(np.array(cnt_list))
my_ans =  75*149/199
print(f"compute:{ans}")
print(f"My ans: {my_ans}")
print(f"error: {abs(ans-my_ans)}")




        
    
