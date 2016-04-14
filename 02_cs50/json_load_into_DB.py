import json

def file_open(filename):
	file = open(filename, 'r')
	contents = json.loads(file.read())
	file.close()
	return contents

def create_sql(contents):
	pass	

def write_into_sql_file(contents):
	f = open(".sql", 'w')
	for i in contents:
		for j in i:
			f.write(j)
	f.close()
	
def main():
	filenamelist = ['']
	contents = {}
	sql_templates ="INSERT INTO slack_question (time, user, text) VALUES ('%s','%s','%s');\n"	
	temp_sql_templates = []
	sql_sentences = []

	for filename in filenamelist:
		contents = file_open(filename)
		for i in range(len(contents)):
			if 'user' in contents[i]:
				temp_sql_templates = [sql_templates %(contents[i]['ts'] ,contents[i]['user'] ,contents[i]['text'])] 
				print(temp_sql_templates)
				sql_sentences.append(temp_sql_templates)
			else:
				temp_sql_templates = [sql_templates %(contents[i]['ts'] ,'' ,contents[i]['text'])] 
				print(temp_sql_templates)
				sql_sentences.append(temp_sql_templates)
	write_into_sql_file(sql_sentences)




if __name__=="__main__":
	main()
