from typing import List
from app.admin.VO.UserVO import UserVO
from app.admin.VO.PageVO import PageVO

class ProfileVO:

    __id: int
    
    __administrator: bool

    __description: str

    __general: bool

    __intersection: bool

    __pages: List[PageVO]

    __users: List[UserVO]

    __excludedUsers: List[UserVO]

    def __init__(self):
        self.__pages = []
        self.__users = []
        self.__excludedUsers = []
        self.Clean()
    

    def Clean(self):    
        self.__id = -1
        self.__administrator = False
        self.__description = ""
        self.__general = False
        self.__intersection = False
        self.__pages = []
        self.__users = []
        self.__excludedUsers = []

    def __str__(self):
        return self.__description    

    def getId(self) -> int:
        return self.__id
    
    def setId(self, value: int):    
        self.__id = value    

    def getAdministrator(self) -> bool:    
        return self.__administrator    

    def setAdministrator(self, value: bool):    
        self.__administrator = value    

    def getDescription(self) -> str:    
        return self.__description    

    def setDescription(self, value: str):    
        self.__description = value    

    def getGeneral(self) -> bool:    
        return self.__general
    
    def setGeneral(self, value: bool):    
        self.__general = value
    
    def getIntersection(self) -> bool:
        return self.__intersection
    
    def setIntersection(self, value: bool):    
        self.__intersection = value    

    def getPages(self) -> List[PageVO]:
        return self.__pages    

    def setPages(self, pages: List[PageVO]):    
        self.__pages =pages

    def getUsers(self) -> List[UserVO]:
        return self.__users
    
    def setUsers(self, users: List[UserVO]):
        self.__users = users

    def getExcludedUsers(self) -> List[UserVO]:
        return self.__excludedUsers
    
    def setExcludedUsers(self, excludedUsers: List[UserVO]):    
        self.__excludedUsers = excludedUsers
