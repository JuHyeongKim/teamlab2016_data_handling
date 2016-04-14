import csv

matrix =[]
# file open
f = open("login_who.csv",'r')
csvReader = csv.reader(f)
for row in csvReader:
    matrix.append(row)


#remove_duplicated_data
useful_data_list = []
i = 0
for i in range(len(matrix)):
    try:
        if matrix[i][0] != 'USERNAME        LINE        HOSTNAME                                  TIME':
            if matrix[i] not in useful_data_list:
                print("!")
                useful_data_list.append(matrix[i])
        i += 1
    except:
        print("out of range")
        break


#useful_data_list = list((set(useful_data_list)))

for i in range(20):
    print(useful_data_list[i])
#write into file
after_file = open("after_login_who.csv", "w")
cw = csv.writer(after_file, delimiter=',')
for row in useful_data_list:
    cw.writerow(row)