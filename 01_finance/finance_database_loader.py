import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
SOURCE_FILE_DIR = os.path.join(ROOT_DIR, "TRNA.20110719.1.20030101-20031231.COM.csv")

target_file_list = [os.path.join(SOURCE_FILE_DIR,filename) for filename in os.listdir(SOURCE_FILE_DIR)]
target_file_list = [target_file.replace("\\", "/") for target_file in target_file_list]

load_template = "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s IGNORE 1 LINES;"

load_infile_statments = [load_template % (taraget_file, "EQU")
                         if "EQU" in taraget_file else load_template % (taraget_file, "COM")
                         for taraget_file in target_file_list
                         ]

print("\n".join(load_infile_statments))
