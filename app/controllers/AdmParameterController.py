from typing import List
from app import app
from flask import request, render_template, redirect
from app.base.report.BaseViewReportController import BaseViewReportController
from app.controllers.Messages import MESSAGES
from app.admin.services.AdmParameterCategoryService import AdmParameterCategoryService
from app.admin.services.AdmParameterService import AdmParameterService
from app.admin.models.AdmParameterCategory import AdmParameterCategory
from app.admin.models.AdmParameter import AdmParameter


class AdmParameterController(BaseViewReportController):

    __service: AdmParameterService

    __serviceParameterCategory: AdmParameterCategoryService

    def __init__(self, service: AdmParameterService,
        serviceParameterCategory: AdmParameterCategoryService):
        self.__service = service
        self.__serviceParameterCategory = serviceParameterCategory

    def params(self, model):
        self.loadMessages()

        listAdmCategories = self.__serviceParameterCategory.findAll()

        if (model!=None):
            return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
            'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged(), 
            'listReportType': self.getListReportType(), 
            'listAdmCategories': listAdmCategories, 'model': model }
        else:
            return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
            'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged(), 
            'listReportType': self.getListReportType(), 
            'listAdmCategories': listAdmCategories }

    def index(self):
        model = self.__service.findAll()
        params = self.params(model)
        return render_template('admParameter/index.html', params)

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
            return render_template('admParameter/edit.html', params)
        else:
            model = AdmParameter()
            params = self.params(model)
            return render_template('admParameter/edit.html', params)

    def save(self, request: AdmParameterFormRequest):
        if (request.model().getId() > 0):
            updated = self.__service.update(
                request.model().getId(), request.all())
            if (not updated):
                #$request.session().flash('message', "Not updated!")
                #return Response::HTTP_NOT_FOUND
                pass
        else:
            self.__service.insert(request.all())

        return redirect('listAdmParameter')

    def delete(self, id: int):
        self.__service.delete(id)
        return redirect('listAdmParameter')
