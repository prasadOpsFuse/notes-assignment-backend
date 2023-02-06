from app.main.models.notes_model import NotesModel
from app.db import db
from flask_smorest import abort


def editNote(note_id, data):
    base_query = NotesModel.query.filter(NotesModel.id == note_id)
    if base_query:
        base_query.update(data)
        db.session.commit()
        return base_query.first(),201
    abort(404, message="No Id Match")

def getNote(note_id):
    base_query = NotesModel.query.filter(NotesModel.id == note_id)
    if base_query:
        return base_query.first(),201
    abort(404, message="No Id Match")

def deleteNote(note_id):
    data= {'deleted':True}
    base_query = NotesModel.query.filter(NotesModel.id == note_id)
    if base_query:
        base_query.update(data)
        db.session.commit()
        return { 'status':202,'message':'Note Deleted'  },202
    abort(404, message="No Id Match")
    
