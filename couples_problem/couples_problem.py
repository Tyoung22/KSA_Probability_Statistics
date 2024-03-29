import random 
import statistics

N = 4 # num of couples
Sample_N = 1000 # enum of experiment

class Person():
    def __init__(self,gender,idx) -> None:
        self.gender = gender # man or woman
        self.idx = idx #idx of person
        

cnt_list = []
for _ in range(Sample_N):
    Man_list = [Person('man',i) for i in range(N)]
    Woman_list = [Person('woman',i) for i in range(N)]
    cnt=0
    table = [Man_list.pop(0)]
    table.append(Woman_list.pop(random.randrange(len(Woman_list))))
    while Man_list:
        table.append(Man_list.pop(random.randrange(len(Man_list))))
        table.append(Woman_list.pop(random.randrange(len(Woman_list))))
        
    for i in range(0,len(table),2):
        if table[i+1].idx==table[i].idx or table[i-1].idx ==table[i].idx:
            cnt +=1
    cnt_list.append(cnt)
        
print(f"Mean: {statistics.mean(cnt_list)}")
print(f"Variance: {statistics.variance(cnt_list)}")
        