"""empty message

Revision ID: 3198ce836c1f
Revises: bc063c94d08e
Create Date: 2020-09-18 16:54:09.175177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3198ce836c1f'
down_revision = 'bc063c94d08e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conn_speed_tests', sa.Column('ping', sa.Float(precision='10,2'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('conn_speed_tests', 'ping')
    # ### end Alembic commands ###
