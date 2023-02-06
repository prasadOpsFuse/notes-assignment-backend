from flask_smorest import Blueprint
from flask.views import MethodView
from app.main.utils.folderDTO import FolderSchema,FolderSchemaGet
from app.main.services.folder_service import add_folder_notes,get_all_notes,all_folders
from flask import request


folder_blueprint = Blueprint(
    'Folder', 'folder', url_prefix='/api/v1', description="folders opration")


@folder_blueprint.route('/notes')
class Folders(MethodView):
    @folder_blueprint.arguments(FolderSchema)
    @folder_blueprint.response(201, FolderSchema)
    def post(self, data):
        return add_folder_notes(data)
    
    @folder_blueprint.response(200,FolderSchemaGet(many=True))
    def get(self):
        folder_name = request.args.get('folder_name','')
        return get_all_notes(folder_name)
        
@folder_blueprint.route('/folders')
class FoldersList(MethodView):
    @folder_blueprint.response(200,FolderSchema(many=True))
    def get(self):
        return all_folders()