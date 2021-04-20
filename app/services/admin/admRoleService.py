from app import db
from app.models.role import Role


def add(description):
    r = Role(description)
    db.session.add(r)
    db.session.commit()
    return True
