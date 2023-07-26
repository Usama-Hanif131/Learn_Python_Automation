def code(**data):
    for k,v in data.items():
        print(f"{k}: {v}")
database={"server":"192.168.12.15", "OS":"Linux", "version":"debian 11"}
code(**database)

