import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
import psycopg
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}"

@asynccontextmanager
async def get_connection():
    """
    Returns a new async database connection instance, and handles commit/rollback.
    """
    conn = await psycopg.AsyncConnection.connect(DATABASE_URL)
    try:
        async with conn.transaction(): 
            async with conn.cursor() as cursor:
                yield cursor  
    except Exception as e:
        raise e
    finally:
        await conn.close()  