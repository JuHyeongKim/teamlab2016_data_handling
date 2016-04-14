import csv

matrix =[]
# file open
f = open("all_data_cs50_server.csv",'r')
csvReader = csv.reader(f)
for row in csvReader:
    matrix.append(row)

useful_data = [['command','time','user']]
for i in range(1,len(matrix)):
	try:
		temp_user = matrix[i][5].split('/')
		user = temp_user[2]
		temp_variable = [matrix[i][0],matrix[i][1],user]

		useful_data.append(temp_variable)

	except:
	       	print("out of range")
        	break




#write into file
after_file = open("first_filtered_all_cs50_server.csv", "w")
cw = csv.writer(after_file, delimiter=',')
for row in useful_data:
    cw.writerow(row)
