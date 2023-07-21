data={"user1":"Jack wilson", "password1":"jack123", "user2":"stokes", "password2":"stokes123"}
for i in data.items():
    if i[0].startswith("password"):
        pass
    else:
        print(f"Username exits in database: {i[1]}")