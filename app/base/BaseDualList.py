from typing import List

class BaseDualList:

    __source = List

    __target = List

    def __init__(self, source: List, target: List):
        self.__source = source
        self.__target = target

    def __eq__(self, other):
        if (isinstance(other, BaseDualList)):
            return self.__source == other.__source and self.__target == other.__target
        return False 
    
    @property
    def getSource(self) -> List:
        return self.__source

    @__source.setter
    def setSource(self, source: List):
        self.__source = source

    @property
    def getTarget(self) -> List:
        return self.__target

    @__target.setter
    def setTarget(self, target: List):
        self.__target = target

