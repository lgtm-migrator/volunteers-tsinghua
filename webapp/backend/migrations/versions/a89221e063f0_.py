"""empty message

Revision ID: a89221e063f0
Revises: 436cc1da8232
Create Date: 2019-11-24 02:44:39.732656

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a89221e063f0'
down_revision = '436cc1da8232'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('activities', 'content',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=400),
               existing_nullable=False)
    op.alter_column('activities', 'description',
               existing_type=mysql.VARCHAR(length=200),
               type_=sa.String(length=400),
               existing_nullable=False)
    op.alter_column('messages', 'isRead',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'isRead',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('activities', 'description',
               existing_type=sa.String(length=400),
               type_=mysql.VARCHAR(length=200),
               existing_nullable=False)
    op.alter_column('activities', 'content',
               existing_type=sa.String(length=400),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=False)
    # ### end Alembic commands ###
