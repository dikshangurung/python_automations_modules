# #!/usr/bin/env python3

# import re
# import csv


# def contains_domain(address, domain):#blossom@abc.edu,abc.edu
#   """Returns True if the email address contains the given,domain,in the domain position, false if not."""
#   domain_pattern = r'[\w\.-]+@'+domain+'$'
#   if re.match(domain_pattern,address):
#     return True
#   return False


# def replace_domain(address, old_domain, new_domain):
#   """Replaces the old domain with the new domain in the received address."""
#   old_domain_pattern = r'' + old_domain + '$'
#   address = re.sub(old_domain_pattern, new_domain, address)
#   return address

# def main():
#   """Processes the list of emails, replacing any instances of the old domain with the new domain."""
#   old_domain, new_domain = 'abc.edu', 'xyz.edu'
#   csv_file_location = './user_emails.csv'
#   report_file = 'updated_user_emails.csv'
#   user_email_list = []
#   old_domain_email_list = []
#   new_domain_email_list = []

#   with open(csv_file_location, 'r') as f:
#     user_data_list = list(csv.reader(f))
#     # print(user_data_list)
#     user_email_list = [data[1].strip() for data in user_data_list[1:]]
#     # print(user_email_list)

#     for email_address in user_email_list:
#       if contains_domain(email_address, old_domain):
#         old_domain_email_list.append(email_address)
#         replaced_email = replace_domain(email_address,old_domain,new_domain)
#         new_domain_email_list.append(replaced_email)
#     # print(new_domain_email_list)
#     email_key = ' ' + 'Email Address'
#     # print(email_key)
#     email_index = user_data_list[0].index(email_key)
#     # print(email_index)

#     for user in user_data_list[1:]:
#       for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
#         if user[email_index] == ' ' + old_domain:#email_index  = 1
#           user[email_index] = ' ' + new_domain
#     # print(user_data_list)
#   f.close()

#   with open(report_file, 'w+') as output_file:
#     writer = csv.writer(output_file)
#     writer.writerows(user_data_list)
#     output_file.close()

# main()

# import subprocess
# command = ["ls"]
# working_directory = "app_dir/myapp/"
# result = subprocess.run(command,cwd=working_directory,capture_output=True,text=True)
# print(result.stdout)
# print(f"The required paths were:\n{result.stdout.strip().replace(' ', '\n')}")

# import subprocess

# command = ["ls","-l"]
# working_directory = "app_dir/myapp/"
# result = subprocess.run(command, cwd=working_directory, capture_output=True, text=True)

# # Check if the command was successful
# if result.returncode == 0:
#     # Check if stdout is empty
#     if result.stdout.strip():
#       print(result.stdout)
#     else:
#       print("Directory is empty.")
# else:
#     print(f"Error executing command: {result.stderr}")



import re
def show_time_of_pid(line):
  pattern = r"(^[\w\d: ]+) computer.name [\w_=]+\[(\d+)\]:"
  # pattern = r"(\w+ \d+ \d+:\d+:\d+).*\[(\d+)\]"
  result = re.search(pattern, line)
  return f"{result[1]} pid:{result[2]}"

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:2944