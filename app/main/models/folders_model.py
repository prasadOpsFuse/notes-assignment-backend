from app.db import db
import datetime

class FolderModel(db.Model):
    __tablename__ = 'folders'
    now = datetime.datetime.now(datetime.timezone.utc)
    id = db.Column(db.String, primary_key=True )
    folder_name = db.Column(db.String)
    created_at = db.Column(db.Date, default=now)
    updated_at = db.Column(db.Date, onupdate=now)
    notes = db.relationship('NotesModel', back_populates="folder")