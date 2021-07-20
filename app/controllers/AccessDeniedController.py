from app import app
from flask import request, render_template
from app.base.BaseController import BaseController
from app.controllers.Messages import MESSAGES

class AccessDeniedController(BaseController):
    
    def params(self):
        messages = MESSAGES

        self.loadMessages(request)

        return {'messages': MESSAGES, 'alertMessage': self.getAlertMessage(), 
        'menuItem': self.getMenuItem(), 'userLogged': self.getUserLogged() }

    @app.route('/accessDenied')
    def index(self):
        params = self.params()        
        return render_template('accessDenied/index.html', params)
