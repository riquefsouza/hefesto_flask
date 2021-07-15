from typing import List
import string
from app.base.pagination.BasePageItemBuilder import BasePageItemBuilder

class BasePageItem:

    __pageItemType: int

    __index: int

    __active: bool
    
    def __init__(self, pageItemType: int, index: int, active: bool):
        self.__pageItemType = pageItemType
        self.__index = index
        self.__active = active
        
    @staticmethod
    def builder() -> BasePageItemBuilder:
        return BasePageItemBuilder()