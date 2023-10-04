class Input_name_pas:
    """
    Pattern of log-in control: name, password
    ...
    Methods
    -------
    key_key(name, pas):
        Compare user's input of username and password
        with those stored in internal dictionary -
        - if name and password are stored separately
        {Name="x", Password="y"}
    key_val(name, pas):
        Compare user's input of username and password
        with those stored in internal dictionary -
        - if name and password are stored together
        {"Name": "Password"}
    """
# TYPE "NAME, PASSWORD"
    def key_key():
        user = dict(Name="Marek", Password="1234")
        while True:
            n = input("Enter your username: ")
            p = input("Enter your password: ")
            if n == user.get("Name") and user.get("Password") == p:
                print("\n\tWelcome to app! You can go on...\n")
                break
            else:
                print("\t\nUsername or password isn't OK!\n")
# TYPE "NAME: PASSWORD"
    def key_val():
        user = {'Marek': '1234'}
        while True:
            n = input("Enter your username: ")
            p = input("Enter your password: ")
            if user.get(n) == p:
                print("\n\tWelcome to app! You can go on...\n")
                break
            else:
                print("\t\nUsername or password isn't OK!\n")
