from flask_smorest import Blueprint
from flask.views import MethodView
from app.main.utils.notesDTO import NotesSchema

from app.main.services.notes_services import editNote,getNote,deleteNote

notes_blueprint = Blueprint(
    'Notes', 'notes', url_prefix='/api/v1', description="folders opration")


@notes_blueprint.route('/notes/<string:note_id>')
class Notes(MethodView):
    @notes_blueprint.response(201,NotesSchema)
    def get(self,note_id):
        return getNote(note_id)

    @notes_blueprint.arguments(NotesSchema)
    @notes_blueprint.response(201,NotesSchema)
    def put(self,data,note_id):
        return editNote(note_id,data)
    
    def delete(self,note_id):
        return deleteNote(note_id)