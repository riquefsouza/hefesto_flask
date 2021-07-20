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

    @property
    def getId(self) -> int:
        return self.__id

    @__id.setter
    def setId(self, value: int):
        self.__id = value

    @property
    def getIp(self) -> str:
        return self.__ip

    @__ip.setter
    def setIp(self, value: str):
        self.__ip = value

    @property
    def getDate(self) -> datetime:
        return self.__date

    @__date.setter
    def setDate(self, value: datetime):
        self.__date = value

    @property
    def getEmail(self) -> str:
        return self.__email

    @__email.setter
    def setEmail(self, value: str):
        self.__email = value

    @property
    def getLogin(self) -> str:
        return self.__login

    @__login.setter
    def setLogin(self, value: str):
        self.__login = value

    @property
    def getName(self) -> str:
        return self.__name

    @__name.setter
    def setName(self, value: str):
        self.__name = value

    @property
    def getPassword(self) -> str:
        return self.__password

    @__password.setter
    def setPassword(self, value: str):
        self.__password = value

    @property
    def getActive(self) -> bool:
        return self.__active

    @__active.setter
    def setActive(self, value: bool):
        self.__active = value

    @property
    def getAdmIdProfiles(self) -> List[int]:
        return self.__admIdProfiles

    @__admIdProfiles.setter
    def setAdmIdProfiles(self, admIdProfiles: List[int]):
        self.__admIdProfiles = admIdProfiles

    @property
    def getUserProfiles(self) -> str:
        return self.__userProfiles

    @__userProfiles.setter
    def setUserProfiles(self, userProfiles: str):
        self.__userProfiles = userProfiles

    @property
    def getCurrentPassword(self) -> str:
        return self.__currentPassword

    @__currentPassword.setter
    def setCurrentPassword(self, currentPassword: str):
        self.__currentPassword = currentPassword

    @property
    def getNewPassword(self) -> str:
        return self.__newPassword

    @__newPassword.setter
    def setNewPassword(self, newPassword: str):
        self.__newPassword = newPassword

    @property
    def getConfirmNewPassword(self) -> str:
        return self.__confirmNewPassword

    @__confirmNewPassword.setter
    def setConfirmNewPassword(self, confirmNewPassword: str):
        self.__confirmNewPassword = confirmNewPassword
