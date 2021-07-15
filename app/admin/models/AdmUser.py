from app import db
from typing import List
from app.admin.VO.UserVO import UserVO

class AdmUser(db.Model):
    __tablename__ = 'adm_user'

    id = db.Column('usu_seq', db.BigInteger, db.Sequence('adm_user_seq'), primary_key=True)
    active = db.Column('usu_active', db.CHAR, nullable=False, default='N')
    email = db.Column('usu_email', db.String(255), unique=True)
    login = db.Column('usu_login', db.String(64), nullable=False, unique=True)
    name = db.Column('usu_name', db.String(64), unique=True)
    password = db.Column('usu_password', db.String(128), nullable=False, unique=True)

    admIdProfiles: List[int]    
    userProfiles: str
    currentPassword: str
    newPassword: str
    confirmNewPassword: str

    def __init__(self):
        self.id = 0
        self.active = "N"
        self.email = None
        self.login = ""
        self.name = ""
        self.password = ""
        self.admIdProfiles = []
        self.userProfiles = ""
        self.currentPassword = ""
        self.newPassword = ""
        self.confirmNewPassword = ""
    
    def __repr__(self):
        return '<AdmUser %r>' % self.name

    def CreateFromUserVO(self, vo: UserVO):
        self.id = vo.getId()
        self.active = vo.getActive()
        self.email = vo.getEmail()
        self.login = vo.getLogin()
        self.name = vo.getName()
        #self.password = vo.getPassword()
        self.admIdProfiles = vo.getAdmIdProfiles()
        self.userProfiles = vo.getUserProfiles()
        self.currentPassword = vo.getCurrentPassword()
        self.newPassword = vo.getNewPassword()
        self.confirmNewPassword = vo.getConfirmNewPassword()

    def toUserVO(self) -> UserVO:
        u = UserVO()

        u.setId(self.id)
        #u.setIp(self.ip)
        u.setEmail(self.email)
        u.setLogin(self.login)
        u.setName(self.name)

        return u
