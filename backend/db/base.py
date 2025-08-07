"""
Base module for SQLAlchemy models.
Alembic needs to know about all models here to support automatic migration generation.
"""

from backend.db.base_class import Base  # the DeclarativeBase
from backend.models.user import User    # all models here
# from app.models.other_model import OtherModel
