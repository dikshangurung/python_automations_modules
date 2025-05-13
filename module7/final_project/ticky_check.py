#!/usr/bin/env python3
import re
import operator
error = {}
per_user = {}
error_keys = {"Error", "Count"}
per_user_keys = {"Username", "INFO", "ERROR"}
with open("syslog.log", "r") as file:
    for line in file:
        error_match = re.search(r"ticky: ERROR ([\w ]*) ", line)
        if error_match:
            user_error_match = re.search(r" \(([\w.]*)\)", line)
            error_message = error_match[1]
            username = user_error_match[1]
            
            if error_message in error:
                if 'Count' in error[error_message]:
                    error[error_message]["Count"] += 1
                else:
                    error[error_message]["Count"] = 1
            else:
                error[error_message] = {'Error': error_message, 'Count': 1}
            
            if username in per_user:
                if 'Error' in per_user[username]:
                    per_user[username]['Error'] += 1
                else:
                    per_user[username]['Error'] = 1
            else:
                per_user[username] = {'Username': username, 'Error': 1, 'Info': 0}
        else:
            info_match = re.search(r"ticky: INFO ([\w ]*) ", line)
            if info_match:
                user_info_match = re.search(r" \(([\w.]*)\)", line)
                info_message = info_match[1]
                username = user_info_match[1]
                
                if username in per_user:
                    if 'Info' in per_user[username]:
                        per_user[username]['Info'] += 1
                    else:
                        per_user[username]['Info'] = 1
                else:
                    per_user[username] = {'Username': username, 'Info': 1, 'Error': 0}

# Convert per_user dictionary to a list of dictionaries
per_user_list = [{'Username': user,'INFO': info['Info'],'ERROR': info['Error']} for user, info in per_user.items()]
error_list = [{'Error': error['Error'],'Count': error['Count']} for error in error.values()]
print(error_list)

#Write the error messages to a CSV file
with open("error_message.csv", "w") as error_file:
    error_file.write("Error,Count\n")
    for error in error_list:
        error_file.write(f"{error['Error']},{error['Count']}\n")
        
#Write the user statistics to a CSV file
with open("user_statistics.csv", "w") as user_file:
    user_file.write("Username,INFO,ERROR\n")
    for user in per_user_list:
        user_file.write(f"{user['Username']},{user['INFO']},{user['ERROR']}\n")
# print(per_user)
# print(per_user_list)
# print(error)