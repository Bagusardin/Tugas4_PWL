"""seddsepatu

Revision ID: 6b4f8b8006c9
Revises: 66eb9b2777f3
Create Date: 2023-12-23 17:30:25.993225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6b4f8b8006c9"
down_revision: Union[str, None] = "66eb9b2777f3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "sepatu",
            sa.Column("name", sa.String(length=255), nullable=False),
            sa.Column("description", sa.Text(), nullable=False),
            sa.Column("price", sa.Integer(), nullable=False),
            sa.Column("image_url", sa.String(length=255), nullable=False),
            sa.Column("stock", sa.Integer(), nullable=False),
        ),
        [
            {
                "name": "Sepatu 1",
                "description": "Ini adalah sepatu 1",
                "price": 100000,
                "image_url": "https://via.placeholder.com/150",
                "stock": 10,
            },
            {
                "name": "Sepatu 2",
                "description": "Ini adalah sepatu 2",
                "price": 200000,
                "image_url": "https://via.placeholder.com/150",
                "stock": 20,
            },
            {
                "name": "Sepatu 3",
                "description": "Ini adalah sepatu 3",
                "price": 300000,
                "image_url": "https://via.placeholder.com/150",
                "stock": 30,
            },
            {
                "name": "Sepatu Sneakers ABC",
                "description": "Sepatu sneakers nyaman dengan desain modern.",
                "price": 350000,
                "image_url": "https://example.com/images/sepatu_abc.jpg",
                "stock": 25,
            },
            {
                "name": "Sepatu Formal XYZ",
                "description": "Sepatu formal elegan untuk acara penting.",
                "price": 500000,
                "image_url": "https://example.com/images/sepatu_xyz.jpg",
                "stock": 15,
            },
            {
                "name": "Sepatu Lari Performance",
                "description": "Sepatu lari dengan teknologi terkini untuk performa maksimal.",
                "price": 600000,
                "image_url": "https://example.com/images/sepatu_lari.jpg",
                "stock": 20,
            },
            {
                "name": "Sepatu Boots Outdoor",
                "description": "Sepatu boots cocok untuk kegiatan di luar ruangan.",
                "price": 750000,
                "image_url": "https://example.com/images/sepatu_boots.jpg",
                "stock": 18,
            },
            {
                "name": "Sepatu Sandal Santai",
                "description": "Sandal santai untuk digunakan sehari-hari.",
                "price": 150000,
                "image_url": "https://example.com/images/sepatu_sandal.jpg",
                "stock": 30,
            },
            {
                "name": "Sepatu Futsal Pro",
                "description": "Sepatu futsal berkualitas tinggi untuk permainan yang lebih baik.",
                "price": 400000,
                "image_url": "https://example.com/images/sepatu_futsal.jpg",
                "stock": 12,
            },
            {
                "name": "Sepatu Slip-on Casual",
                "description": "Sepatu slip-on yang nyaman untuk gaya kasual.",
                "price": 250000,
                "image_url": "https://example.com/images/sepatu_slip-on.jpg",
                "stock": 22,
            },
            {
                "name": "Sepatu Wedges Fashion",
                "description": "Sepatu wedges untuk penampilan fashion yang menarik.",
                "price": 450000,
                "image_url": "https://example.com/images/sepatu_wedges.jpg",
                "stock": 17,
            },
            {
                "name": "Sepatu Ankle Boots Trendy",
                "description": "Ankle boots dengan desain trendy untuk gaya yang berbeda.",
                "price": 550000,
                "image_url": "https://example.com/images/sepatu_ankle_boots.jpg",
                "stock": 14,
            },
            {
                "name": "Sepatu High Heels Elegan",
                "description": "High heels elegan untuk acara formal.",
                "price": 700000,
                "image_url": "https://example.com/images/sepatu_high_heels.jpg",
                "stock": 10,
            },
        ],
    )


def downgrade() -> None:
    op.execute("DELETE FROM sepatu")
