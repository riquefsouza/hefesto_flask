from typing import List
from app.admin.VO.MenuVO import MenuVO
from app.admin.VO.PageVO import PageVO

class MenuVO:

    __id: int

    __description: str

    __order: int

    __idPage: int

    __page: PageVO

    __menuParent: MenuVO

    __subMenus: List[MenuVO]

    def __init__(self):    
        self.__subMenus = []
        self.Clean()
    
    def Clean(self):    
        self.__id = -1
        self.__description = ""
        self.__order = -1
        self.__idPage = -1
        self.__page = PageVO()
        self.__menuParent = None
        self.__subMenus = []
    
    @property
    def getId(self) -> int:    
        return self.__id
    
    @__id.setter
    def setId(self, value: int):    
        self.__id = value    

    @property
    def getDescription(self) -> str:    
        return self.__description
    
    @__description.setter
    def setDescription(self, value: str):    
        self.__description = value    

    @property
    def getOrder(self) -> int:
        return self.__order
    
    @__order.setter
    def setOrder(self, value: int):    
        self.__order = value    

    @property
    def getIdPage(self) -> int:    
        return self.__idPage    

    @__idPage.setter
    def setIdPage(self, value: int):    
        self.__idPage = value    

    @property
    def getPage(self) -> PageVO:    
        return self.__page    

    @__page.setter
    def setPage(self, value: PageVO):    
        self.__page = value    

    @property
    def getMenuParent(self) -> MenuVO:    
        return self.__menuParent    

    @__menuParent.setter
    def setMenuParent(self, value: MenuVO):    
        self.__menuParent = value
    
    @property
    def getSubMenus(self) -> List[MenuVO]:
        return self.__subMenus
    
    @__subMenus.setter
    def setSubMenus(self, subMenus: List[MenuVO]):    
        self.__subMenus = subMenus

    def addSubMenus(self, subMenu: MenuVO) -> MenuVO:    
        self.__subMenus.append(subMenu)
        subMenu.setMenuParent(self)
        return subMenu

    def removeSubMenus(self, subMenu: MenuVO) -> MenuVO:
        for i in range(0, len(self.__subMenus)):
            item = self.__subMenus[i]
            if (item.getId() == subMenu.getId()):
                self.__subMenus.pop(i)
                break            
        
        subMenu.setMenuParent(self)
        return subMenu    

    def isSubMenu(self) -> bool:    
        return self.__page == None    

    @property
    def getUrl(self) -> str:    
        return self.__page.getUrl() if self.__page != None else None    

    def __str__(self):    
        return self.__description    