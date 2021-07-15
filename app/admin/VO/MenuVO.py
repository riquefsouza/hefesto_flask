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
    
    def getId(self) -> int:    
        return self.__id
    
    def setId(self, value: int):    
        self.__id = value    

    def getDescription(self) -> str:    
        return self.__description
    
    def setDescription(self, value: str):    
        self.__description = value    

    def getOrder(self) -> int:
        return self.__order
    
    def setOrder(self, value: int):    
        self.__order = value    

    def getIdPage(self) -> int:    
        return self.__idPage    

    def setIdPage(self, value: int):    
        self.__idPage = value    

    def getPage(self) -> PageVO:    
        return self.__page    

    def setPage(self, value: PageVO):    
        self.__page = value    

    def getMenuParent(self) -> MenuVO:    
        return self.__menuParent    

    def setMenuParent(self, value: MenuVO):    
        self.__menuParent = value
    
    def getSubMenus(self) -> List[MenuVO]:
        return self.__subMenus
    
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

    def getUrl(self) -> str:    
        return self.__page.getUrl() if self.__page != None else None    

    def __str__(self):    
        return self.__description    