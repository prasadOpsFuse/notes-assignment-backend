from app.db import db
import datetime

class NotesModel(db.Model):
    __tablename__ = 'notes'
    now = datetime.datetime.now(datetime.timezone.utc)
    id = db.Column(db.String, primary_key=True )
    title = db.Column(db.String)
    body = db.Column(db.String)
    created_at = db.Column(db.String, default=now)
    updated_at = db.Column(db.String, onupdate=now)
    group_name = db.Column(db.String)
    deleted = db.Column(db.Boolean, default=False)
    height = db.Column(db.String)
    width = db.Column(db.String)
    title_color = db.Column(db.String)
    body_color = db.Column(db.String)
    background = db.Column(db.String)
    folder_id = db.Column(db.String, db.ForeignKey('folders.id'))
    folder = db.relationship('FolderModel', back_populates="notes")
    