import json


def save_config(username, password, name):
    user_dict = {
        "name": name,
        "username": username,
        "password": password
    }
    string = json.dumps(user_dict)
    with open("user_config.txt", "w") as f:
        f.write(string)


def read_config():
    with open("user_config.txt", "r") as f:
        html = f.read()
    if html == "":
        return {"name": "", "username": "", "password": ""}
    return json.loads(html)
