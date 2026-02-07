"""Data shapes for internal operations."""

from pydantic import BaseModel
from aiosqlite import Connection
from filesystem import NotesFileSystem

class User(BaseModel):
    id: str
    username: str
    db: Connection
    fs: NotesFileSystem

class NoteBase(BaseModel):
    title: str

class NoteList(BaseModel):
    pass

class NoteCreate(NoteBase):
    pass