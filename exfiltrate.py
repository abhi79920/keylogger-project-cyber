import base64

def send_to_server(data):
    with open("logs/exfiltrated_data.txt", "a") as f:
        f.write(base64.b64encode(data).decode() + "\n")
