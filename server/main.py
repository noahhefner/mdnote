from fastapi import Depends, FastAPI, HTTPException, Request, status

app = FastAPI(lifespan=lifespan)

app.include_router(notes.router, prefix="/api/notes", tags=["notes"])