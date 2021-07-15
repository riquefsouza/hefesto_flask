from typing import List
from app.admin.VO.ProfileVO import ProfileVO

class PageVO:

    __id: int

    __description: str

    __url: str

    __profiles: List[ProfileVO]

    def __init__(self):
        self.__profiles = []
        self.Clean()

    def Clean(self):
        self.__id = -1
        self.__description = ""
        self.__url = ""
        self.__profiles = []    

    def __str__(self):  
        return self.__url

    def getId(self) -> int:    
        return self.__id
    
    def setId(self, value: int):    
        self.__id = value    

    def getDescription(self) -> str:    
        return self.__description    

    def setDescription(self, value: str):    
        self.__description = value    

    def getUrl(self) -> str:    
        return self.__url    

    def setUrl(self, value: str):    
        self.__url = value
    
    def getProfiles(self) -> List[ProfileVO]: 
        return self.__profiles    

    def setProfiles(self, profiles: List[ProfileVO]):    
        self.__profiles = profiles
