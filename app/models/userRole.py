from app import db

class UserRole(db.Model):
    __tablename__ = "adm_user_role"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('adm_user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('adm_role.id'))
    user = db.relationship('User', foreign_keys=user_id)
    role = db.relationship('Role', foreign_keys=role_id)

    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id
