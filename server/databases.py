import aiosqlite

async def get_auth_db():
    """Get username / password database."""

    async with aiosqlite.connect("/data/auth.db") as db:
        yield db

async def get_user_db(username: str) -> aiosqlite.Connection:
    """Get user notes database."""

    async with aiosqlite.connect(f"/data/users/{username}.db") as db:
        yield db