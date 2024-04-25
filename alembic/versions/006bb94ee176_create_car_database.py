"""create car database

Revision ID: 006bb94ee176
Revises: 
Create Date: 2024-04-25 11:07:03.582036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '006bb94ee176'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("cars", 
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("vin", sa.Text, nullable=False),
                    sa.Column("model", sa.Text, nullable=False),
                    sa.Column("make", sa.Text, nullable=False),
                    sa.Column("engine", sa.Text, nullable=False),
                    sa.Column("year", sa.Text, nullable=False))
    
    op.create_table("dealership",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("name", sa.Text, nullable=False),
                    sa.Column("address", sa.Text, nullable=False),
                    sa.Column("phonenumber", sa.Text, nullable=False))
    
    op.create_table("inventory",
                    sa.Column("car_id", sa.Integer, sa.ForeignKey("cars.id")),
                    sa.Column("dealer_id", sa.Integer, sa.ForeignKey("dealership.id")),
                    sa.Column("cost", sa.Float, nullable=False),
                    sa.Column("is_sold", sa.Boolean, nullable=False),
                    sa.PrimaryKeyConstraint("car_id", "dealer_id"))

def downgrade() -> None:
    op.drop_table("inventory")
    op.drop_table("dealership")
    op.drop_table("cars")
