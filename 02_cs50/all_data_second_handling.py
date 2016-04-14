import csv

matrix =[]
# file open
f = open("first_filtered_all_cs50_server.csv",'r')
csvReader = csv.reader(f)
for row in csvReader:
    matrix.append(row)

useful_data = [['command','time','user']]
for i in range(1,len(matrix)):
	try:
		print(i)
		if matrix[i] not in useful_data:
			useful_data.append(matrix[i])
	except:
	       	print("out of range")
        	break
print(useful_data)



#write into file
after_file = open("second_filtered_all_cs50_server.csv", "w")
cw = csv.writer(after_file, delimiter=',')
for row in useful_data:
    cw.writerow(row)
