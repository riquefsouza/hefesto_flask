class ModeTestVO:

    __active: bool

    __login: str

    __loginVirtual: str

    def __init__(self):
        self.__active = False
        self.__login = ""
        self.__loginVirtual = ""
    
    def Create(self, active: bool, login: str, loginVirtual: str):    
        self.__active = active
        self.__login = login
        self.__loginVirtual = loginVirtual    

    @property
    def getActive(self) -> bool:    
        return self.__active    

    @__active.setter
    def setActive(self, value: bool):    
        self.__active = value    

    @property
    def getLogin(self) -> str:    
        return self.__login    

    @__login.setter
    def setLogin(self, value: str):    
        self.__login = value

    @property    
    def getLoginVirtual(self) -> str:    
        return self.__loginVirtual    

    @__loginVirtual.setter
    def setLoginVirtual(self, value: str):    
        self.__loginVirtual = value
    
    def __eq__(self, other):
        if (isinstance(other, ModeTestVO)):
            return self.__str__ == other.__str__            
        return False    

    def __str__(self):
        return "ModeTestVO [active=" + self.__active + ", login=" + self.__login + ", loginVirtual=" + self.__loginVirtual + "]"
