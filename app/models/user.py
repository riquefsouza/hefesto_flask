from app import db

class User(db.Model):
    __tablename__ = "adm_user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.String(2))
    #role_id = db.Column(db.Integer, db.ForeignKey('adm_role.id'))
    #role = db.relationship('Role', foreign_keys=role_id)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.active = 'S'
    
    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)  