"""empty message

Revision ID: a2718421b221
Revises: 
Create Date: 2020-12-19 13:39:14.534989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2718421b221'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('manager', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=8), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('ticker', sa.String(length=4), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('team', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['team'], ['team.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report')
    op.drop_table('team')
    # ### end Alembic commands ###