from typing import List
from app.base.report.ReportType import ReportType

class ReportGroupVO:

    __group: str
    
    __types: List[ReportType]

    def __init__(self, group str, types: List[ReportType]):
        self.__group = group
        self.__types = types

    def getGroup(self) -> str:
        return self.__group

    def setGroup(self, value: str):
        self.__group = value

    def getTypes() -> List[ReportType]:
        return self.__types

    def setTypes(self, types: List[ReportType]):
        self.__types = types
