from flask import session
from app.base.models.AlertMessageVO import AlertMessageVO
from app.admin.VO.AuthenticatedUserVO import AuthenticatedUserVO

class BaseController:

    __alertMessage: AlertMessageVO

    __userLogged: AuthenticatedUserVO

    __menuItem: MenuVO

    def loadMessages(self):
        self.loadMessagesWithAlertMessage(None)

    def loadMessagesWithAlertMessage(self, alertMessage: AlertMessageVO):
        if (alertMessage == None)
            self.__alertMessage = AlertMessageVO()
        else
            self.__alertMessage = alertMessage

        authenticatedUser = self.getAuthenticatedUser()

        if (authenticatedUser!=None):
            authenticatedUser.getUser().setActive(True)
            self.__userLogged = authenticatedUser.getUser()

            listMenus = authenticatedUser.getListAdminMenus()

            self.__menuItem = listMenus
        else:
            self.__userLogged = UserVO()
            self.__userLogged.setActive(False)

            self.__menuItem = []

    def getAuthenticatedUser() -> AuthenticatedUserVO:
        if (session['authenticatedUser']!=None):
            return session['authenticatedUser']
        else:
            return None

    def setUserAuthenticated(self, usu: AuthenticatedUserVO):
        session['authenticatedUser'] = usu        

    def removeUserAuthenticated(self):
        session.pop('authenticatedUser', None)


