"""createtablesepatu

Revision ID: 66eb9b2777f3
Revises: 
Create Date: 2023-12-23 17:28:27.477346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "66eb9b2777f3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "sepatu",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("image_url", sa.String(length=255), nullable=False),
        sa.Column("stock", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("sepatu")
