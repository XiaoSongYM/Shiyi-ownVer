

class service():
    serviceName: str = "default service"
    serviceURL: str = "default service URL"
    # 1 Get
    # 2 POST
    serviceType: int = -1
    serviceDescription: str = f"{serviceName} when {serviceType}ed: "

    def __init__(self, name:str, url:str, type:int) -> None:
        self.serviceName = name
        self.serviceURL = url
        self.serviceType = type
        pass

    def check(self):
        # 设置发送 http 请求
        pass

class errorList():
    errList: list = [service]
    empty = True
    def add(self, errservice:service):
        self.errList.append(errservice)
        self.empty = False

    def fine(self):
        return self.empty

    def print(self):
        if self.empty:
            print("API Service is healthy!")
        else:
            for i in self.errList:
                print("Error occured!")