from auth import CurrentUser
from fastapi import APIRouter

from pathvalidate import sanitize_filename
import schemas
import models

router = APIRouter()

@router.post(
    "",
    response_model=schemas.NoteCreatedResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_note(
    note: schemas.NoteCreate,
    current_user: CurrentUser
):
    """Create a new note."""

    # strip invalid characters from filename
    sanitized_title = sanitize_filename(note.title)

    new_note = models.NoteCreate(
        title=sanitized_title
    )

    # create file in filesystem
    current_user.fs.create(new_note)

    return new_note

@router.get("", response_model=list[schemas.AllNotesResponse])
async def get_all_notes(current_user: CurrentUser):
    """Get all a users notes."""
    
    return current_user.fs.list()