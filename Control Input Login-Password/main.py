import stored_logins
import login_ctr
import extract_dict
#help(stored_logins)
#help(login_ctr)
#help(extract_dict)

storage = stored_logins.Storage
control = login_ctr.LoginCtr
extract = extract_dict.Extract()

user1 = storage("Radagast", "brown", "123")
user2 = storage("Gandalf", "grey", "456")
user3 = storage("Saruman", "white", "789")

input_try = 3
control_result = ""
while not control_result and input_try > 0:
    login = input("Enter your username: ")
    password = input("Enter your password: ")
    input_control = control(login, password)
    control_result = input_control.search_matches(extract)
    input_try -= 1
if control_result: print("\n\tWelcome to app, " + control_result[0] + "! You can go on...")
else: print("Just 3 tries to connect per day, unfortunately. See ya tomorrow. (:")