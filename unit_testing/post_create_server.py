import requests
import json


def post_create_server():
    print("You are attempting to post information for servers")

    host = input("Hostname: ")
    port = input("Port Number: ")
    api_key = input("API Key: ")

    baseurl = "http://{}:{}/projectstorm/create_servers".format(host, port)
    header = {"Content-Type": "application/json"}

    data = {}
    data["api_key"] = api_key
    data["server_type"] = "rust"
    data["seed"] = "22"
    data["worldsize"] = "1000"
    data["maxplayers"] = "250"
    data["server_name"] = "Rusty Storm"
    json_outgoing = json.dumps(data)

    try:
        response = requests.post(baseurl, headers=header, data=json_outgoing, verify=False)
        print(response)
        print(response.text)

    except Exception as e:
        print("FAILED: " + str(e))


post_create_server()