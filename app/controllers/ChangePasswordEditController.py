from typing import List
from app import app
from flask import request, render_template, redirect
from app.base.BaseController import BaseController
from app.controllers.Messages import MESSAGES
from app.admin.services.AdmUserService import AdmUserService
from app.admin.services.ChangePasswordService import ChangePasswordService
from app.admin.models.AdmUser import AdmUser
from app.admin.VO.UserVO import UserVO
from app.base.models.AlertMessageVO import AlertMessageVO


class ChangePasswordEditController(BaseController):

    __service: AdmUserService

    __changePasswordService: ChangePasswordService

    __userLogged: UserVO

    __alertMessage: AlertMessageVO

    def __init__(self, service: AdmUserService,
        changePasswordService: ChangePasswordService):
        self.__service = service
        self.__changePasswordService = changePasswordService

    def params(self, model):
        self.loadMessages()

        userLogged = self.getAuthenticatedUser().getUser()

        if (model!=None):
            return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
            'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged(), 
            'model': model }
        else:
            return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
            'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged() }

    def prepareToSave(self, user: UserVO) -> bool:
        if (user.getNewPassword() == None and user.getConfirmNewPassword() == None and user.getCurrentPassword() == None) \
                or (user.getNewPassword() == "" and user.getConfirmNewPassword() == "" and user.getCurrentPassword() == ""):
            self.__alertMessage = AlertMessageVO.Warning("changePasswordView.validation")
        elif (user.getNewPassword() == None and user.getConfirmNewPassword() == None) \
              or (user.getNewPassword() == "" and user.getConfirmNewPassword() == ""):
            self.__alertMessage = AlertMessageVO::Warning("changePasswordView.validation")
        else:
            if (user.getNewPassword() == user.getConfirmNewPassword()):
                return True
            else:
                self.__alertMessage = AlertMessageVO.Warning("changePasswordView.notEqual")
        return False

    def validatePassword(self, user: UserVO) -> bool:
        if not self.changePasswordService.validatePassword(user.getLogin(), user.getCurrentPassword()):
            self.__alertMessage = AlertMessageVO.Warning("changePasswordView.validatePassword")
            return False

        if not self.changePasswordService.validatePassword(user.getLogin(), user.getNewPassword()):
            self.__alertMessage = AlertMessageVO.Warning("changePasswordView.validatePassword")
            return False

        return True

    def index(self):
        params = self.params(None)
        return render_template('changePasswordEdit/index.html', params)

    def save(self, request: AdmUserFormRequest):
        user = UserVO()
        user.CreateWithAdmUser(request.model())

        if not self.prepareToSave(user):
            params = self.params(request.model())
            return render_template('changePasswordEdit/index.html', params)

        if not self.validatePassword(user):
            params = self.params(request.model())
            return render_template('changePasswordEdit/index.html', params)

        if (request.model().getId() > 0):
            admUser = request.model()

            admUser.setPassword(user.getConfirmNewPassword())
            self.__service.register(admUser)

            updated = self.__service.update(admUser.getId(), admUser)
            if not updated:
                #request.session().flash('message', "Not updated!")
                #return Response::HTTP_NOT_FOUND
                pass

            self.__alertMessage = AlertMessageVO.Info("changePasswordView.passwordChanged")

        params = self.params(admUser)
        return render_template('changePasswordEdit/index.html', params)
