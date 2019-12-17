"""empty message

Revision ID: 33d328fefac9
Revises: 9c94a79a753f
Create Date: 2019-12-01 09:29:22.131887

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '33d328fefac9'
down_revision = '9c94a79a753f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('useractivities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('activityId', sa.Integer(), nullable=True),
    sa.Column('workdate', sa.DateTime(), nullable=False),
    sa.Column('content', sa.String(length=400), nullable=False),
    sa.Column('applytime', sa.DateTime(), nullable=False),
    sa.Column('type', sa.Enum('applying', 'applied', 'finished'), nullable=True),
    sa.Column('isRead', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['activityId'], ['activities.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('messages', 'isRead',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.drop_constraint('messages_ibfk_3', 'messages', type_='foreignkey')
    op.create_foreign_key(None, 'messages', 'activities', ['activityId'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.create_foreign_key('messages_ibfk_3', 'messages', 'activities', ['activityId'], ['id'])
    op.alter_column('messages', 'isRead',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_table('useractivities')
    # ### end Alembic commands ###