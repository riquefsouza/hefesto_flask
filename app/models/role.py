from app import db

class Role(db.Model):
    __tablename__ = "adm_role"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True)

    def __init__(self, description):
        self.description = description
    
    def __repr__(self):
        return '<Role %r>' % self.description
