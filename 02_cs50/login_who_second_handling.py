import csv

matrix =[]
# file open
f = open("after_login_who.csv",'r')
csvReader = csv.reader(f)
for row in csvReader:
    matrix.append(row)

# filtering that first column

useful_data = []
for i in range(1,len(matrix)):
	
	test = matrix[i][0].split(' ')

	count = 0
	while 1:
		try:
			if test[count] == '':
				test.remove(test[count])
				count = 0
			count += 1
		except:
			temp_list = [test[0],test[3]+' '+test[4]]
			useful_data.append(temp_list)
			break


#remove_duplicated_data
useful_data_list = []
#for i in range(len(matrix)):
#    try:
#	
#
#    except:
#        print("out of range")
#        break




#write into file
after_file = open("second_filtered_login_who.csv", "w")
cw = csv.writer(after_file, delimiter=',')
for row in useful_data:
    cw.writerow(row)
