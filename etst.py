import csv
import json

all_data=[[],[],[],[],[],[],[],[],[],[]]
nums_rows=[]
m=0
c=1
with open("mnist_test.csv") as dataset, open("10k_digits.json", "w+") as output:
    data=csv.reader(dataset)
    for data_row in data:   
        #if c<=10:     
            
        all_data[int(data_row[0])-1].append([int(x) for x in data_row])
            # print(len(data_row))        
            # nums_rows += [[int(x[y]) for y in range(28)] for x in [data_row[28*i+1:28*i+29] for i in range(1,28)]]
            # all_data[int(data_row[0])-1].append(nums_rows)            
            # m+=1
            # if m==100: 
            #     print(c*100)
            #     m=0
            #c+=1
    json.dump(all_data, output)
    
    print('done')
            

            
