from typing import List
import string
from app.controllers.Messages import MESSAGES

class AlertMessageVO:

    PrimaryMessage: str
    SecondaryMessage: str
    SuccessMessage: str
    DangerMessage: str
    WarningMessage: str
    InfoMessage: str
    LightMessage: str
    DarkMessage: str

    def __init__(self):
        self.PrimaryMessage = ""
        self.SecondaryMessage = ""
        self.SuccessMessage = ""
        self.DangerMessage = ""
        self.WarningMessage = ""
        self.InfoMessage = ""
        self.LightMessage = ""
        self.DarkMessage = ""
    
    @staticmethod
    def Primary(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.PrimaryMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Secondary(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.SecondaryMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Success(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.SuccessMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Danger(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.DangerMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Warning(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.WarningMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Info(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.InfoMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Light(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.LightMessage = MESSAGES[key]
        return vo

    @staticmethod
    def Dark(key: str):
        vo: AlertMessageVO = AlertMessageVO()
        vo.DarkMessage = MESSAGES[key]
        return vo
