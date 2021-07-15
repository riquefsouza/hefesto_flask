from flask import request

class BaseController:

    __alertMessage: AlertMessageVO

    __userLogged: AuthenticatedUserVO

    __menuItem: MenuVO

    def loadMessages(self):
        self.loadMessagesWithAlertMessage(request, nil)

    def loadMessagesWithAlertMessage(self,
        AlertMessageVO|null $alertMessage): void
    {
        if ($alertMessage == null)
            self.__alertMessage = new AlertMessageVO();
        else
            self.__alertMessage = $alertMessage;

        $authenticatedUser = self.__getAuthenticatedUser($request);

        if ($authenticatedUser!=null)
        {
            $authenticatedUser->getUser()->setActive(true);
            self.__userLogged = $authenticatedUser->getUser();

            $listMenus = $authenticatedUser->getListAdminMenus();

            self.__menuItem = $listMenus;
        } else
        {
            self.__userLogged = new UserVO();
            self.__userLogged->setActive(false);

            self.__menuItem = array();
        }

    }

    public function getAuthenticatedUser(Request $request): AuthenticatedUserVO|null
    {
        //AuthenticatedUserVO
        if ($request->session()->has('authenticatedUser'))
            return $request->session()->get('authenticatedUser');
        else
            return null;
    }

    public function setUserAuthenticated(Request $request, AuthenticatedUserVO $usu): void
    {
        $request->session()->put('authenticatedUser', $usu);
    }

    public function removeUserAuthenticated(Request $request): void
    {
        $request->session()->forget('authenticatedUser');    


