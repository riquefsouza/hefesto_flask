from typing import List
import string

class BasePageItemBuilder:

    __pageItemType: int
    
    __index: int

    __active: bool

    def pageItemType(self, pageItemType: int) -> BasePageItemBuilder: 
        self.__pageItemType = pageItemType;
        return self

    def index(self, index: int) -> BasePageItemBuilder:
        self.__index = index
        return self

    def active(self, active: bool) -> BasePageItemBuilder:
        self.__active = active
        return self

    def build(self) -> BasePageItem:
        return BasePageItem(self.__pageItemType, self.__index, self.__active)
