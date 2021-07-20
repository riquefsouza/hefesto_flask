from typing import List
from app import app
from flask import request, render_template, redirect
from app.base.report.BaseViewReportController import BaseViewReportController
from app.base.BaseDualList import BaseDualList
from app.controllers.Messages import MESSAGES
from app.admin.services.AdmProfileService import AdmProfileService
from app.admin.services.AdmPageService import AdmPageService
from app.admin.models.AdmPage import AdmPage
from app.admin.models.AdmProfile import AdmProfile


class AdmPageController(BaseViewReportController):

    __service: AdmPageService

    __admProfileService: AdmProfileService

    __dualListAdmProfile: BaseDualList

    __listAllAdmProfiles: List[AdmProfile]

    def __init__(self, service: AdmPageService, admProfileService: AdmProfileService):
        self.__service = service
        self.__admProfileService = admProfileService
        self.__listAllAdmProfiles = []

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

    def loadAdmProfiles(self, bean: AdmPage, bEdit: bool) -> BaseDualList:
        listAdmProfilesSelected = []
        listAdmProfiles = []
        allprofiles = self.__admProfileService.findAll()
        for item in allprofiles:
            listAdmProfiles.append(item)

        listAllAdmProfiles = []
        for item in listAdmProfiles:
            listAllAdmProfiles.append(item)

        if (bEdit):
            listAdmProfilesSelected = []

            for profile in listAdmProfiles:
                for page in profile.getAdmPages():
                    if (page.getId() == bean.getId()):
                        listAdmProfilesSelected.append(profile)
                        break

            for x in range(len(listAdmProfiles)-1, 0, -1):
                item = listAdmProfiles[x]

                if item in listAdmProfilesSelected:
                    listAdmProfiles.pop(x)
        else:
            listAdmProfilesSelected = []

        self.__dualListAdmProfile = BaseDualList(listAdmProfiles, listAdmProfilesSelected)

        return self.__dualListAdmProfile

    def index(self):
        model = self.__service.findAll()
        params = self.params(model)
        return render_template('admPage/index.html', params)

    def edit(self, id: int):
        if (id == None):
            #return Response::HTTP_NOT_FOUND;
            pass

        if (id > 0):
            model = self.__service.findById(id)
            if (model == None):
                #return Response::HTTP_NOT_FOUND
                pass

            self.__dualListAdmProfile = self.loadAdmProfiles(model, True)
            listSourceAdmProfiles = self.__dualListAdmProfile.getSource()
            listTargetAdmProfiles = self.__dualListAdmProfile.getTarget()

            params = self.params(model)
            params['listSourceAdmProfiles'] = listSourceAdmProfiles
            params['listTargetAdmProfiles'] = listTargetAdmProfiles
            return render_template('admPage/edit.html', params)
        else:
            model = AdmPage()

            self.__dualListAdmProfile = self.loadAdmProfiles(model, False)
            listSourceAdmProfiles = self.__dualListAdmProfile.getSource()
            listTargetAdmProfiles = self.__dualListAdmProfile.getTarget()

            params = self.params(model)
            params['listSourceAdmProfiles'] = listSourceAdmProfiles
            params['listTargetAdmProfiles'] = listTargetAdmProfiles
            return render_template('admPage/edit.html', params)

    def save(self, request: AdmPageFormRequest):
        if (request.model().getId() > 0):
            updated = self.__service.update(
                request.model().getId(), request.all())

            if (not updated):
                #$request->session()->flash('message', "Not updated!");
                #return Response::HTTP_NOT_FOUND;
                pass
        else:
            self.__service.insert(request.all())

        return redirect('listAdmPage')

    def delete(self, id: int):
        self.__service.delete(id)
        return redirect('listAdmPage')
