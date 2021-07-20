from typing import List
from app.admin.VO.MenuVO import MenuVO
from app.admin.VO.UserVO import UserVO
from app.admin.VO.PageVO import PageVO
from app.admin.VO.ProfileVO import ProfileVO
from app.admin.VO.PermissionVO import PermissionVO

class AuthenticatedUserVO:

    __userName: str

    __displayName: str

    __email: str

    __listPermission: List[PermissionVO]

    __listMenus: List[MenuVO]

    __listAdminMenus: List[MenuVO]

    __user: UserVO

    __modeTest: bool

    __modeTestLogin: str

    __modeTestLoginVirtual: str

    def __init__(self):   
        self.__listPermission = []
        self.__listMenus = []
        self.__listAdminMenus = []
        self.__user = UserVO()

        self.Clean()

        self.__modeTest = False
        self.__modeTestLogin = ""
        self.__modeTestLoginVirtual = ""
    
    def Create(self, userName: str):    
        self.__userName = userName    

    def Clean(self):    
        self.__userName = ""
        self.__displayName = ""
        self.__email = ""
        self.__listPermission = []
        self.__listMenus = []
        self.__listAdminMenus = []
        self.__user.Clean()
        self.__modeTestLogin = ""
        self.__modeTestLoginVirtual = ""
    
    def __eq__(self, other):
        if (isinstance(other, AuthenticatedUserVO)):
            return self.__str__ == other.__str__            
        return False 
    
    def __str__(self):
        return self.__displayName
    
    def getProfileById(self, idProfile: int) -> ProfileVO:    
        admProfile = None
        for permissaoVO in self.__listPermission:
            if (permissaoVO.getProfile().getId() == idProfile):            
                admProfile = permissaoVO.getProfile()
                break
        return admProfile    

    def isProfileById(self, idProfile: int) -> bool:    
        return (self.getProfile(idProfile) != None)    

    def getProfile(self, profile: str) -> ProfileVO:
        admProfile = None
        for permissaoVO in self.__listPermission:
            if (permissaoVO.getProfile().getDescription() == profile):
                admProfile = permissaoVO.getProfile()
                break                    
        return admProfile    

    def isProfile(self, profile: str) -> bool:    
        return (self.getProfile(profile) != None)
    
    def getProfileGeneral(self) -> ProfileVO:    
        admProfile = None
        for permissaoVO in self.__listPermission:
            if (permissaoVO.getProfile().getGeneral()):            
                admProfile = permissaoVO.getProfile()
                break                    
        return admProfile    

    def getProfileAdministrator(self) -> ProfileVO:    
        admProfile = None
        for permissaoVO in self.__listPermission:
            if (permissaoVO.getProfile().getAdministrator()):            
                admProfile = permissaoVO.getProfile()
                break                    
        return admProfile
    
    def isGeneral(self) -> bool:    
        profile = self.getProfileGeneral()
        if (profile != None):        
            return profile.getGeneral()        
        return False
    
    def isAdministrator(self) -> bool:    
        profile = self.getProfileAdministrator()
        if (profile != None):
            return profile.getAdministrator()        
        return False
    
    def getPageByMenu(self, idMenu: int) -> PageVO:    
        admPage = None
        if (self.__listMenus != None and len(self.__listMenus) > 0):
            for admMenu in self.__listMenus:
                admPage = admMenu.getPage()
                break

        if (self.__listAdminMenus != None and len(self.__listAdminMenus) > 0):        
            for admMenu in self.__listAdminMenus:
                admPage = admMenu.getPage()
                break
            
        return admPage
    

    def hasPermission(self, url: str, tela: str) -> bool:
        if (url == None):        
            return False
        
        pos = url.index("private")
        url = url[pos + 8 : len(url)] if pos > -1 else url

        if (url == tela):
            return True
        
        for permissao in self.__listPermission:
            for admPage in permissao.getPages():            
                if (admPage.getUrl() == url):                
                    return True
        
        return False
    
    def getMenu(self, sidMenu: str) -> MenuVO:    
        menu = None
        idMenu = int(sidMenu)

        for item in self.__listMenus:
            for submenu in item.getSubMenus():
                if (submenu.getId() == idMenu):
                    menu = submenu
                    break                
            
            if (menu != None):            
                break

        if (menu == None):        
            for item in self.__listAdminMenus:            
                for submenu in item.getSubMenus():
                    if (submenu.getId() == idMenu):
                        menu = submenu
                        break                    
                
                if (menu != None):                
                    break                
        return menu    

    @property
    def getUserName(self) -> str:
        return self.__userName
    
    @__userName.setter
    def setUserName(self, userName: str):    
        self.__userName = userName    

    @property
    def getDisplayName(self) -> str:    
        return self.__displayName

    @__displayName.setter
    def setDisplayName(self, displayName: str):    
        self.__displayName = displayName    

    @property
    def getEmail(self) -> str:    
        return self.__email    

    @__email.setter
    def setEmail(self, email: str):    
        self.__email = email
    
    @property
    def getListPermission(self) -> List[PermissionVO]:
        return self.__listPermission
    
    @__listPermission.setter
    def setListPermission(self, listPermission: List[PermissionVO]):    
        self.__listPermission = listPermission    

    @property
    def getListMenus(self) -> List[MenuVO]:
        return self.__listMenus
    
    @__listMenus.setter
    def setListMenus(self, listMenus: List[MenuVO]):
        self.__listMenus = listMenus

    @property
    def getListAdminMenus(self) -> List[MenuVO]:
        return self.__listAdminMenus

    @__listAdminMenus.setter
    def setListAdminMenus(self, listAdminMenus: List[MenuVO]):    
        self.__listAdminMenus = listAdminMenus    

    @property
    def getUser(self) -> UserVO:    
        return self.__user

    @__user.setter
    def setUser(self, user: UserVO):    
        self.__user = user    

    @property
    def getModeTest(self) -> bool:    
        return self.__modeTest
    
    @__modeTest.setter
    def setModeTest(self, modeTest: bool):    
        self.__modeTest = modeTest    

    @property
    def getModeTestLogin(self) -> str:    
        return self.__modeTestLogin

    @__modeTestLogin.setter
    def setModeTestLogin(self, modeTestLogin: str):    
        self.__modeTestLogin = modeTestLogin    

    @property
    def getModeTestLoginVirtual(self) -> str:    
        return self.__modeTestLoginVirtual

    @__modeTestLoginVirtual.setter
    def setModeTestLoginVirtual(self, modeTestLoginVirtual: str):    
        self.__modeTestLoginVirtual = modeTestLoginVirtual