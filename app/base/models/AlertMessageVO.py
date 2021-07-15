from typing import List
import string
from app.controllers.Messages import MESSAGES

class AlertMessageVO:

    __PrimaryMessage: str
    __SecondaryMessage: str
    __SuccessMessage: str
    __DangerMessage: str
    __WarningMessage: str
    __InfoMessage: str
    __LightMessage: str
    __DarkMessage: str

    def __init__(self):
        self.__PrimaryMessage = ""
        self.__SecondaryMessage = ""
        self.__SuccessMessage = ""
        self.__DangerMessage = ""
        self.__WarningMessage = ""
        self.__InfoMessage = ""
        self.__LightMessage = ""
        self.__DarkMessage = ""
    
    @staticmethod
    def Primary(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.__PrimaryMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Secondary(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.__SecondaryMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Success(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.__SuccessMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Danger(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.__DangerMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Warning(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.__WarningMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Info(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.__InfoMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Light(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.__LightMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Dark(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.__DarkMessage = MESSAGES[key]
        return vo
