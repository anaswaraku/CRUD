from app.core.database import engine

from app.models import *
from app.models.base import Base

try:
    # this is used before migration to alembic: Base.metadata.create_all(bind=engine)
    print("Table creation success")
except Exception as e:
    print(f"Table creation failed: {e}")
