from typing import List
from app import app
from flask import request, render_template, redirect
from app.base.report.BaseViewReportController import BaseViewReportController
from app.controllers.Messages import MESSAGES
from app.admin.services.AdmMenuService import AdmMenuService
from app.admin.services.AdmPageService import AdmPageService
from app.admin.models.AdmPage import AdmPage
from app.admin.models.AdmMenu import AdmMenu

class AdmMenuController(BaseViewReportController):

    __service: AdmMenuService

    __servicePage: AdmPageService

    __listAdmPage: List[AdmPage]

    __listAdmMenuParent: List[AdmMenu]

    def __init__(self, service: AdmMenuService, servicePage: AdmPageService):
        self.__service = service
        self.__servicePage = servicePage

        self.__listAdmPage = []
        self.__listAdmMenuParent = []

    def params(self, model):
        self.loadMessages(request)

        if (model!=None):
            return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
            'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged(), 
            'listReportType': self.getListReportType(), 'model': model }
        else:
            return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
            'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged(), 
            'listReportType': self.getListReportType() }

    def fillLists(self, params):
        self.listAdmPage = self.__servicePage.findAll()
        params['listAdmPages'] = self.__listAdmPage

        self.__listAdmMenuParent = []

        listAdmMenus = self.__service.findAll()
        for menu in listAdmMenus:
            if ((menu.getAdmSubMenus() != None) and (menu.getAdmPage() == None)):
                menu.append(self.__listAdmMenuParent)

        params['listAdmMenuParents'] = self.__listAdmMenuParent

        return params

    def filterLists(self, bean: AdmMenu):
        page = AdmPage()
        for item in self.__listAdmPage:
            if (item.getId() == bean.getIdPage()):
                page = item
                break

        if (page!=None):
            bean.setIdPage(page.getId())

        menuParent = AdmMenu()
        for item in self.__listAdmMenuParent:
            if (item.getId() == bean.getIdMenuParent()):
                menuParent = item
                break

        if (menuParent != None):
            bean.setIdMenuParent(menuParent.getId())

    def index(self):
        model = self.getAuthenticatedUser().getListAdminMenus()
        params = self.params(model)
        return render_template('admMenu/index.html', params)

    def edit(self, id: int):
        if (id == None):
            #return Response::HTTP_NOT_FOUND
            pass

        if (id > 0):
            model = self.__service.findById(id)
            if (model == None):
                #return Response::HTTP_NOT_FOUND
                pass

            params = self.params(model)
            params = self.fillLists(params)
            self.filterLists(model)

            return render_template('admMenu/edit.html', params)
        else:
            model = AdmMenu()
            params = self.params(model)
            params = self.fillLists(params)

            return render_template('admMenu/edit.html', params)

    def save(self, request: AdmMenuFormRequest):
        if (request.model().getId() > 0):
            updated = self.service->update(
                $request->model()->getId(), $request->all());
            if (!updated)
                #$request->session()->flash('message', "Not updated!");
                #return Response::HTTP_NOT_FOUND;
                pass
            self.filterLists(request->model())
        else:
            model = self.__service.insert(request->all())
            self.filterLists($model)

        return redirect('listAdmMenu')

    def delete(self, id: int):
        self.__service.delete(id)
        return redirect('listAdmMenu')
