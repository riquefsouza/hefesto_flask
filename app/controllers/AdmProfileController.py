import re
from typing import List
from app import app
from flask import request, render_template, redirect
from app.base.report.BaseViewReportController import BaseViewReportController
from app.controllers.Messages import MESSAGES
from app.admin.services.AdmProfileService import AdmProfileService
from app.admin.services.AdmPageService import AdmPageService
from app.admin.services.AdmUserService import AdmUserService
from app.admin.models.AdmProfile import AdmProfile
from app.admin.models.AdmPage import AdmPage
from app.admin.models.AdmUser import AdmUser
from app.base.BaseDualList import BaseDualList

class AdmProfileController(BaseViewReportController):

    __service: AdmProfileService
    
    __admPageService: AdmPageService

    __dualListAdmPage: BaseDualList

    __listAllAdmPages: List[AdmPage]

    __admUserService: AdmUserService

    __dualListAdmUser: BaseDualList

    __listAllAdmUsers: List[AdmUser]

    def __init__(self, service: AdmProfileService, admPageService: AdmPageService,
        admUserService: AdmUserService):
        self.__service = service

        self.__admPageService = admPageService
        self.__admUserService = admUserService

        self.__listAllAdmPages = []
        self.__listAllAdmUsers = []

    def params(self, model):
        self.loadMessages()

        if (model!=None):
            return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
            'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged(), 
            'listReportType': self.getListReportType(), 'model': model }
        else:
            return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
            'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged(), 
            'listReportType': self.getListReportType() }

    def loadAdmPages(self, bean: AdmProfile, bEdit: bool) -> BaseDualList:
        listAdmPagesSelected = []
        listAdmPages = []
        allpages = self.__admPageService.findAll()
        for item in allpages:
            listAdmPages.append(item)

        listAllAdmPages = []
        for item in listAdmPages:
            listAllAdmPages.append(item)

        if (bEdit):
            listAdmPagesSelected = []

            for page in listAdmPages:
                for profileId in page.getAdmIdProfiles():
                    if (profileId == bean.getId()):
                        listAdmPagesSelected.append(page)
                        break

            for x in range(len(listAdmPages)-1, 0, -1):
                item = listAdmPages[x]

                if item in listAdmPagesSelected:
                    listAdmPages.pop(x)
        else:
            listAdmPagesSelected = []

        self.__dualListAdmPage = BaseDualList(listAdmPages, listAdmPagesSelected)

        return self.__dualListAdmPage

    def loadAdmUsers(self, bean: AdmProfile, bEdit: bool) -> BaseDualList:
        listAdmUsersSelected = []
        listAdmUsers = []
        allusers = self.__admUserService.findAll()
        for item in allusers:
            listAdmUsers.append(item)

        listAllAdmUsers = []
        for item in listAdmUsers:
            listAllAdmUsers.append(item)

        if (bEdit):
            listAdmUsersSelected = []

            for user in listAdmUsers:
                for profileId in user.getAdmIdProfiles():
                    if (profileId == bean.getId()):
                        listAdmUsersSelected.append(user)
                        break

            for x in range(len(listAdmUsers)-1, 0, -1):
                item = listAdmUsers[x]

                if (item in listAdmUsersSelected):
                    listAdmUsers.pop(x)
        else:
            listAdmUsersSelected = []

        self.__dualListAdmUser = BaseDualList(listAdmUsers, listAdmUsersSelected)

        return self.__dualListAdmUser

    def fillLists(self, model: AdmProfile, bEdit: bool):
        self.__dualListAdmPage = self.loadAdmPages(model, bEdit)
        listSourceAdmPages = self.__dualListAdmPage.getSource()
        listTargetAdmPages = self.__dualListAdmPage.getTarget()

        self.__dualListAdmUser = self.loadAdmUsers(model, bEdit)
        listSourceAdmUsers = self.__dualListAdmUser.getSource()
        listTargetAdmUsers = self.__dualListAdmUser.getTarget()

        params = self.params(model)
        params['listSourceAdmPages'] = listSourceAdmPages
        params['listTargetAdmPages'] = listTargetAdmPages

        params['listSourceAdmUsers'] = listSourceAdmUsers
        params['listTargetAdmUsers'] = listTargetAdmUsers

        return params

    def index(self):
        model = self.__service.findAll()
        params = self.params(model)
        return render_template('admProfile/index.html', params)

    def edit(self, id: int):
        if (id == None):
            #return Response::HTTP_NOT_FOUND
            pass

        if (id > 0):
            model = self.__service.findById(id)
            if (model == None):
                #return Response::HTTP_NOT_FOUND
                pass

            params = self.fillLists(model, True)

            return render_template('admProfile/edit.html', params)
        else:
            model = AdmProfile()

            params = self.fillLists(model, False)

            return render_template('admProfile/edit.html', params)

    def save(self, request: AdmProfileFormRequest):
        if (request.model().getId() > 0):
            updated = self.__service.update(
                request.model().getId(), request.all())
            if (not updated):
                #request.session().flash('message', "Not updated!")
                #return Response::HTTP_NOT_FOUND
                pass
        else:
            self.__service.insert(request.all())

        return redirect('listAdmProfile')

    def delete(self, id: int):
        self.__service.delete(id)
        return redirect('listAdmProfile')
