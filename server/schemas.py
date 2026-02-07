"""Data shapes for HTTP requests and responses."""

from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str

class NoteCreate(NoteBase):
    pass

class AllNotesResponse(NoteBase):
    pass

class SingleNoteResponse(NoteBase):
    content: str

class NoteCreatedResponse(NoteBase):
    pass