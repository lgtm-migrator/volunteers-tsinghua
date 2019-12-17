"""empty message

Revision ID: f8be0ebde913
Revises: 141096417732
Create Date: 2019-11-28 23:03:25.807959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8be0ebde913'
down_revision = '141096417732'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('introcodes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('code', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('teamname', sa.String(length=64), nullable=True),
    sa.Column('establishedtime', sa.DateTime(), nullable=True),
    sa.Column('avatar', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('openId', sa.String(length=64), nullable=False),
    sa.Column('userName', sa.String(length=16), nullable=False),
    sa.Column('wx', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('avatar', sa.String(length=128), nullable=True),
    sa.Column('schoolID', sa.String(length=30), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('department', sa.Text(), nullable=True),
    sa.Column('profile', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('AID', sa.Integer(), nullable=True),
    sa.Column('teamId', sa.Integer(), nullable=True),
    sa.Column('thumb', sa.String(length=128), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=False),
    sa.Column('endtime', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(length=50), nullable=False),
    sa.Column('title', sa.String(length=70), nullable=False),
    sa.Column('content', sa.String(length=400), nullable=False),
    sa.Column('totalRecruits', sa.Integer(), nullable=True),
    sa.Column('appliedRecruits', sa.Integer(), nullable=True),
    sa.Column('manageperson', sa.String(length=70), nullable=False),
    sa.Column('managephone', sa.String(length=70), nullable=False),
    sa.Column('manageemail', sa.String(length=70), nullable=False),
    sa.Column('qrcode', sa.String(length=128), nullable=True),
    sa.Column('type', sa.Enum('creating', 'created', 'finished'), nullable=True),
    sa.ForeignKeyConstraint(['teamId'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('teamId', sa.Integer(), nullable=True),
    sa.Column('activityId', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('qrCode', sa.String(length=64), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('isRead', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['activityId'], ['activities.id'], ),
    sa.ForeignKeyConstraint(['teamId'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('useractivities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('activityId', sa.Integer(), nullable=True),
    sa.Column('workdate', sa.DateTime(), nullable=False),
    sa.Column('content', sa.String(length=400), nullable=False),
    sa.Column('applytime', sa.DateTime(), nullable=False),
    sa.Column('type', sa.Enum('applying', 'applyed', 'finished'), nullable=True),
    sa.ForeignKeyConstraint(['activityId'], ['activities.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('useractivities')
    op.drop_table('messages')
    op.drop_table('activities')
    op.drop_table('users')
    op.drop_table('teams')
    op.drop_table('introcodes')
    # ### end Alembic commands ###
