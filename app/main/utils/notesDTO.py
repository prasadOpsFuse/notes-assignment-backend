from marshmallow import Schema, fields

class NotesSchema(Schema):
    body = fields.Str()
    title = fields.Str()
    group_name = fields.Str()
    created_at = fields.Str(required=False)
    updated_at = fields.Str(required=False)
    folder_id = fields.Str()
    deleted = fields.Boolean()
    height = fields.Str()
    width = fields.Str()
    title_color = fields.Str()
    body_color = fields.Str()
    background = fields.Str()