from utils.consulclient import ConsulClient
import requests
#请求rest api 实例
class HttpClient():
    #指定consul 服务的主机，端口，以及所要请求的应用民
    def __init__(self,consulhost,consulport,appname):
        self.consulhost=consulhost
        self.consulport=consulport
        self.appname=appname
        self.consulclient=ConsulClient(host=self.consulhost,port=self.consulport)
    def request(self):
        host,port=self.consulclient.getService(self.appname)
        scrapyMessage=requests.get('http://'+host+':'+str(port)+'/'+'api/services').text
        print(scrapyMessage)

if __name__=='__main__':
    client=HttpClient('192.168.16.161','8500','p3')
    client.request()