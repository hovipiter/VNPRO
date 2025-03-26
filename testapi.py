import requests
import json
def get_ticket(): 
    base_url = "http://x.x.x.x/api/v1/ticket" #lấy token để xác thực
    header = {"content-type": "application/json"}
    body = json.dumps({
        "username": "username",
        "password": "password"
    })
    responses = requests.post(base_url, headers = header, data= body, verify= True) #thực hiện gửi yêu cầu tạo ticket và trả về kết quả
    data = responses.json()
    print(json.dumps(data, indent=4))
    ticket = data['response']['serviceTicket'] #Truy cập vào dữ liệu bên trong để lấy ticket.
    print(ticket) 
    return ticket
get_ticket()

def network_device():
    url = "http://x.x.x.x/api/v1/network-device"
    header = {
        "x-auth-token": get_ticket()
    }
    response_device = requests.get(url, headers=header, verify=False)
    print (response_device)
    list_networkdevice = response_device.json()
    print(json.dumps(list_networkdevice, indent = 4))
    return list_networkdevice   

network_device()