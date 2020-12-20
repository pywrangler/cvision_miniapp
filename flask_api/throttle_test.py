import urllib.request, json 
import requests
token = ''
with urllib.request.urlopen("http://0.0.0.0:5000/get_new_token") as url:
    data = json.loads(url.read().decode())
    print(data['token'])
    token = data['token']

files = {'file': open("ttest.png",'rb')}   

r=requests.post("http://0.0.0.0:5000/upload_image", headers={'x-access-token':token},files =files)
r=requests.post("http://0.0.0.0:5000/upload_image", headers={'x-access-token':token},files =files)
r=requests.post("http://0.0.0.0:5000/upload_image", headers={'x-access-token':token},files =files)
r=requests.post("http://0.0.0.0:5000/upload_image", headers={'x-access-token':token},files =files)
r=requests.post("http://0.0.0.0:5000/upload_image", headers={'x-access-token':token},files =files)
r=requests.post("http://0.0.0.0:5000/upload_image", headers={'x-access-token':token},files =files)
r=requests.post("http://0.0.0.0:5000/upload_image", headers={'x-access-token':token},files =files)