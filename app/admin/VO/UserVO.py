from datetime import datetime
from typing import List
from app.admin.models.AdmUser import AdmUser

class UserVO:

    __id: int

    __ip: str

    __date: datetime

    __email: str
    
    __login: str

    __name: str

    __password: str

    __active: bool

    __admIdProfiles: List[int]
    
    __userProfiles: str

    __currentPassword: str

    __newPassword: str

    __confirmNewPassword: str

    def __init__(self):
        self.Clean()

    def Create(self, login: str, password: str):
        self.__login = login
        self.__password = password

    def CreateWithEmail(self, id: int, email: str, login: str, name: str, active: bool):
        self.__id = id
        self.__email = email
        self.__login = login
        self.__name = name
        self.__active = active

    def CreateWithAdmUser(self, admUser: AdmUser):
        self.__setId(admUser.id)
        self.__setActive(admUser.active)
        self.__setEmail(admUser.email)
        self.__setLogin(admUser.login)
        self.__setName(admUser.name)
        self.__setPassword(admUser.password)
        self.__setAdmIdProfiles(admUser.admIdProfiles)
        self.__setUserProfiles(admUser.userProfiles)
        self.__setCurrentPassword(admUser.currentPassword)
        self.__setNewPassword(admUser.newPassword)
        self.__setConfirmNewPassword(admUser.confirmNewPassword)

    def Clean(self):
        self.__ip = ""
        self.__date = datetime.now()
        self.__email = ""
        self.__login = ""
        self.__name = ""
        self.__password = ""
        self.__active = False
        self.__admIdProfiles = []
        self.__userProfiles = ""
        self.__currentPassword = ""
        self.__newPassword = ""
        self.__confirmNewPassword = ""

    def getId(self) -> int:
        return self.__id

    def setId(self, value: int):
        self.__id = value

    def getIp(self) -> str:
        return self.__ip

    def setIp(self, value: str):
        self.__ip = value

    def getDate(self) -> datetime:
        return self.__date

    def setDate(self, value: datetime):
        self.__date = value

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, value: str):
        self.__email = value

    def getLogin(self) -> str:
        return self.__login

    def setLogin(self, value: str):
        self.__login = value

    def getName(self) -> str:
        return self.__name

    def setName(self, value: str):
        self.__name = value

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, value: str):
        self.__password = value

    def getActive(self) -> bool:
        return self.__active

    def setActive(self, value: bool):
        self.__active = value

    def getAdmIdProfiles(self) -> List[int]:
        return self.__admIdProfiles

    def setAdmIdProfiles(self, admIdProfiles: List[int]):
        self.__admIdProfiles = admIdProfiles

    def getUserProfiles(self) -> str:
        return self.__userProfiles

    def setUserProfiles(self, userProfiles: str):
        self.__userProfiles = userProfiles

    def getCurrentPassword(self) -> str:
        return self.__currentPassword

    def setCurrentPassword(self, currentPassword: str):
        self.__currentPassword = currentPassword

    def getNewPassword(self) -> str:
        return self.__newPassword

    def setNewPassword(self, newPassword: str):
        self.__newPassword = newPassword

    def getConfirmNewPassword(self) -> str:
        return self.__confirmNewPassword

    def setConfirmNewPassword(self, confirmNewPassword: str):
        self.__confirmNewPassword = confirmNewPassword
