"""sync user model

Revision ID: 7571ccea693b
Revises:
Create Date: 2026-08-13 03:12:02.686246

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7571ccea693b"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Add created_at with a temporary server default so
    # existing rows receive a valid timestamp.
    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    # Remove the temporary database-level default.
    op.alter_column(
        "users",
        "created_at",
        server_default=None,
    )

    # Increase role column from VARCHAR(20) to VARCHAR(30).
    op.alter_column(
        "users",
        "role",
        existing_type=sa.VARCHAR(length=20),
        type_=sa.String(length=30),
        existing_nullable=False,
    )

    # user_id is already a primary key, so this extra index is unnecessary.
    op.drop_index(
        op.f("ix_users_user_id"),
        table_name="users",
    )


def downgrade() -> None:
    """Downgrade schema."""

    # Restore the extra user_id index.
    op.create_index(
        op.f("ix_users_user_id"),
        "users",
        ["user_id"],
        unique=False,
    )

    # Change role back to VARCHAR(20).
    op.alter_column(
        "users",
        "role",
        existing_type=sa.String(length=30),
        type_=sa.VARCHAR(length=20),
        existing_nullable=False,
    )

    # Remove created_at.
    op.drop_column(
        "users",
        "created_at",
    )