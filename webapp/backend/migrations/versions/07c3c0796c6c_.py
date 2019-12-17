"""empty message

Revision ID: 07c3c0796c6c
Revises: ddfb549efed3
Create Date: 2019-12-09 09:52:31.439739

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '07c3c0796c6c'
down_revision = 'ddfb549efed3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('activities', 'isRead',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('activities', 'thumb',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('messages', 'isRead',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('useractivities', 'applytime',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('users', 'wx',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'wx',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
    op.alter_column('useractivities', 'applytime',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('messages', 'isRead',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('activities', 'thumb',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('activities', 'isRead',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###
