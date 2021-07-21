from typing import List
from app import app
from flask import request, render_template, redirect
from app.base.report.BaseViewReportController import BaseViewReportController
from app.controllers.Messages import MESSAGES
from app.admin.services.AdmParameterCategoryService import AdmParameterCategoryService
from app.admin.models.AdmParameterCategory import AdmParameterCategory

class AdmParameterCategoryController(BaseViewReportController):

    __service: AdmParameterCategoryService

    def __init__(self, service: AdmParameterCategoryService):
        self.service = service

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

    def index(self):
        model = AdmParameterCategory::paginate(10)
        params = self.params(model)
        return render_template('admParameterCategory/index.html', params)

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
            return render_template('admParameterCategory/edit.html', params)
        else:
            model = AdmParameterCategory()
            params = self.params(model)
            return render_template('admParameterCategory/edit.html', params)

    def save(self, request: AdmParameterCategoryFormRequest):
        if (request.model().getId() > 0):
            updated = self.__service.update(
                request.model().getId(), request.all())
            if (not updated):
                #$request.session().flash('message', "Not updated!")
                #return Response::HTTP_NOT_FOUND
                pass
        else:
            self.__service.insert(request.all())

        return redirect('listAdmParameterCategory')

    def delete(self, id: int):
        self.__service.delete(id)
        return redirect('listAdmParameterCategory')
