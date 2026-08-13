from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Dataset(Base):
    __tablename__ = "datasets"

    dataset_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    file_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="uploaded",
    )