current_users = ['jom', 'tim', 'Admin', 'sinno', 'jin']
new_users = ['sam', 'tom', 'admin', 'sinno', 'gou']
temp_users = [user.lower() for user in current_users]
for user in new_users:
    if user in temp_users:
        print(f"{user}, you need a new username!")
    else:
        print(f"{user}, can be used!")
