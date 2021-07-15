from typing import List
import string

class MenuItemDTO:

    __label: str
    __routerLink: str
    __url: str
    __to: str
    __items: List[MenuItemDTO] = []

    def __init__(self):
        self.__items = []
        self.Clean()

    def Create(self, label: str, url: str):
        self.__label = label
        self.__url = url
        self.__routerLink = url
        self.__to = url
    }

    def CreateWithItems(self, label: str, url: str, items: List[MenuItemDTO])
        self.__label = label
        self.__url = url
        self.__routerLink = url
        self.__to = url
        self.__items = items

    def Clean(self):
        self.__label = ""
        self.__routerLink = ""
        self.__url = ""
        self.__to = ""
        self.__items = []

    def getLabel(self):
        return self.__label

    def setLabel(self, value: str):
        self.__label = value

    def getRouterLink(self):
        return self.__routerLink

    def setRouterLink(self, value: str):
        self.__routerLink = value

    def getUrl(self): 
        return self.__url

    def setUrl(self, value: str):
        self.__url = value

    def getTo(self):
        return self.__to

    def setTo(self, value: str):
        self.__to = value

    def getItems(self):
        return self.__items

    def setItems(self, items: List[MenuItemDTO]):
        self.__items = items