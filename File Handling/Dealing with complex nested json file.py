import json

def print_nested_dict(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value,dict):
            print(key)
            print_nested_dict(value)
        else:
            print(f"   {key}: {value}")

with open("E:\\Knowledge_Hub\\Devops\\Python_Automation\\Notes\\Practice\\data.json", "r") as jf:
    my_dict=json.load(jf)
jf.close()
for server,server_info in my_dict.items():
    print(server)
    if isinstance(server_info,dict):
        print_nested_dict(server_info)
    else:
        print(f"   {server}: {server_info}")