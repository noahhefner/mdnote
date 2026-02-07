import os

from pathlib import Path
import models

class NotesFileSystem():

    def __init__ (self, username: str):

        self.base_storage_path = os.getenv("MDNOTES_PATH")
        if not Path.exists(self.base_storage_path):
            raise RuntimeError(
                f"{self.base_storage_path} is not a valid base storage directory."
            )

        self.user_storage_path = Path.joinpath(self.base_storage_path, username)
        if not Path.exists(self.user_storage_path):
            raise RuntimeError(
                f"{self.user_storage_path} is not a valid user storage directory."
            )

    def create (self, note: models.NoteCreate):
        """Create a new note."""

        title = f"{note.title}.md"
        note_path = Path.joinpath(self.user_storage_path, title)
        
        open(note_path, "x").close()

    def list (self) -> list[models.NoteList]:
        """List all the users notes."""

        notes: list[models.NoteList] = []

        for file in self.user_storage_path.iterdir():
            if file.is_file():
                notes.append(
                    models.NoteList(title=file.name)
                )

        return notes