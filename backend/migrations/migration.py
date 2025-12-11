# backend/migrations/000_initial.py
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOSTNAME')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
print("Connecting to:", DATABASE_URL)
def upgrade():
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor() as cur:
        # Track migration versions
        cur.execute("""
            CREATE TABLE IF NOT EXISTS schema_version (
                version VARCHAR(255) PRIMARY KEY,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS seed_version (
                version VARCHAR(255) PRIMARY KEY,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Create your items table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id SERIAL PRIMARY KEY,
                location TEXT,
                object TEXT
            );
        """)
    conn.commit()
    conn.close()
    print("Migration applied: 000_initial")


if __name__ == "__main__":
    upgrade()