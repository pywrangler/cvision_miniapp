import urllib.request, json 
import requests
token = ''
with urllib.request.urlopen("http://15.207.17.16:5000/get_new_token") as url:
    data = json.loads(url.read().decode())
    print(data['token'])
    token = data['token']

files = {'file': open("ttest.png",'rb')}   

r=requests.post("http://15.207.17.16:5000/upload_image", headers={'x-access-token':token},files =files)
print ("req result=",r)
r=requests.post("http://15.207.17.16:5000/upload_image", headers={'x-access-token':token},files =files)
print ("req result=",r)
r=requests.post("http://15.207.17.16:5000/upload_image", headers={'x-access-token':token},files =files)
print ("req result=",r)
r=requests.post("http://15.207.17.16:5000/upload_image", headers={'x-access-token':token},files =files)
print ("req result=",r)
r=requests.post("http://15.207.17.16:5000/upload_image", headers={'x-access-token':token},files =files)
print ("req result=",r)
r=requests.post("http://15.207.17.16:5000/upload_image", headers={'x-access-token':token},files =files)
print ("req result=",r)
r=requests.post("http://15.207.17.16:5000/upload_image", headers={'x-access-token':token},files =files)
print ("req result=",r)