import csv
# reading cs file
with open("csv_file.txt") as file:
	csv_f = csv.reader(file)
	print(csv_f)
	for row in csv_f:
		print(row)
		# name,phone,role = row
		# print(f"Name:{name} \n phone: {phone} \n role: {role}")


# writing csv file

# hosts = [["Dikshan Gurung",192-322-443,"Backend Engineer"],["RAj Gurung",192-322-443,"Backend Engineer"],["Ramesh Gurung",192-322-443,"Backend Engineer"]]
# with open("new_csv.txt","w") as file:
#     writer = csv.writer(file)
#     writer.writerows(hosts)
    
# Dictionary

# users = [{"name":"Dikshan Gurung","username": "dxngrg","department":"software"},{"name":"Ram Gurung","username": "dxngrg","department":"software"},{"name":"Hari Gurung","username": "dxngrg","department":"software"}]
# keys = ["name","username","department"]
# with open("by_department.csv","w") as file:
#     writer = csv.DictWriter(file,fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(users)
# 	# writer.writerows(users)
  
# with open("by_department.csv") as file:
#     reader = csv.DictReader(file)
#     # print(reader)
#     for row in reader:
#         print(row)  
