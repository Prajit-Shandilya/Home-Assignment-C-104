import csv

with open("SORC_H_W.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
    print(file_data)

file_data.pop(0)
print(file_data)    
new_data=[]
for i in range(len(file_data)):
    h_num=file_data[i][1]
    new_data.append(float(h_num))

n=len(new_data)
total=0
for j in new_data:
    total +=j
    

mean=total/n
print(f"Mean(average)is: {mean}") 
