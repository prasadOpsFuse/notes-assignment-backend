from app.db import db


def save_data(data):
    db.session.add(data)
    db.session.commit()


def delete_data(data):
    db.session.delete(data)
    db.session.commit()