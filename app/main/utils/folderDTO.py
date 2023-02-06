
from marshmallow import Schema, fields

    

class NotesSchema(Schema):
    id = fields.Str()
    body = fields.Str()
    title = fields.Str()
    group_name = fields.Str()
    deleted = fields.Boolean()
    height = fields.Str()
    width = fields.Str()
    title_color = fields.Str()
    body_color = fields.Str()
    background = fields.Str()

class FolderSchema(NotesSchema):
    id = fields.Str()
    created_at = fields.Str(required=False)
    updated_at = fields.Str(required=False)
    folder_name = fields.Str(required=True)

class FolderSchemaGet(FolderSchema):
    notes = fields.List(fields.Nested(NotesSchema()),dump_only=True)