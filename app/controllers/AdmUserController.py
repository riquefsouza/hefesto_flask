from typing import List
from app import app
from flask import request, render_template, redirect
from app.base.report.BaseViewReportController import BaseViewReportController
from app.controllers.Messages import MESSAGES
from app.admin.services.AdmUserService import AdmUserService
from app.admin.models.AdmUser import AdmUser


class AdmUserController(BaseViewReportController):

    __service: AdmUserService

    def __init__(self, service: AdmUserService):
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
        model = self.service.findAll()
        params = self.params(model)
        return render_template('admUser/index.html', params)

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
            return render_template('admUser/edit.html', params)
        else:
            model = AdmUser()
            params = self.params(model)
            return render_template('admUser/edit.html', params)

    def save(self, request: AdmUserFormRequest):
        if (request.model().getId() > 0):
            updated = self.__service.update(
                request.model().getId(), request.all())
            if (not updated):
                #request.session().flash('message', "Not updated!")
                #return Response::HTTP_NOT_FOUND
                pass
        else:
            self.__service.insert(request.all())

        return redirect('listAdmUser')

    def delete(self, id: int):
        self.__service.delete(id)
        return redirect('listAdmUser')
