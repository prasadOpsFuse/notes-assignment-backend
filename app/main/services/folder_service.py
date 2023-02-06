from uuid import uuid4
from app.main.models.folders_model import FolderModel
from app.main.services.common import save_data
from app.main.models.notes_model import NotesModel


def add_folder_notes(data):
    folderAvailable = FolderModel.query.filter(
        FolderModel.folder_name == data['folder_name']).first()
    if not folderAvailable:
        folder_id = uuid4().hex
        folder = {
            'id': folder_id,
            'folder_name': data['folder_name']
        }
        folder_item = FolderModel(**folder)
        save_data(folder_item)
        notes_id = uuid4().hex
        notes = {
            'title': data['title'],
            'body': data['body'],
            'id': notes_id,
            'group_name': 'default',
            'folder_id': folder_id,
        }
        note_item = NotesModel(**notes)
        save_data(note_item)
        return NotesModel.query.get(notes_id)
    else:
        notes_id = uuid4().hex
        notes = {
            'title': data['title'],
            'body': data['body'],
            'id': notes_id,
            'folder_id': folderAvailable.id,
            'group_name': 'default' 
        }
        note_item = NotesModel(**notes)
        save_data(note_item)
        return NotesModel.query.get(notes_id)


def get_all_notes(folder_name):
    if folder_name:
        folderAvailable = FolderModel.query.filter(
        FolderModel.folder_name == folder_name).one_or_404()
        return [folderAvailable] 
    return FolderModel.query.all()

def all_folders():
    return FolderModel.query.all()