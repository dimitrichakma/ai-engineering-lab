from datetime import date, datetime

from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Application(Base):
    __tablename__ = "applications"
    # TODO: id (primary key), company, role, status, applied_on (nullable), url (nullable),
    #       created_at, updated_at
    # TODO: notes: Mapped[list["Note"]] = relationship(back_populates=..., cascade="all, delete-orphan")
    # TODO (migration 2): salary_bdt: Mapped[int | None]
    # TODO (step 5): __table_args__ = (Index(...),)
    pass


class Note(Base):
    __tablename__ = "notes"
    # TODO: id, application_id (ForeignKey with ondelete="CASCADE"), text, created_at
    # TODO: application relationship
    pass


_ = (date, datetime, ForeignKey, Index, String, mapped_column, relationship)
