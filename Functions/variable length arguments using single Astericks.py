def code(*data):
    print(f"server: {data[0]}\nos: {data[1]}\nversion: {data[2]}")

database=("192.168.12.15", "Linux", "debian 11")
code(*database)
