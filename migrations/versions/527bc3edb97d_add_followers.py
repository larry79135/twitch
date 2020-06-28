"""add followers

Revision ID: 527bc3edb97d
Revises: 181196cb92fa
Create Date: 2020-06-22 17:54:59.868039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '527bc3edb97d'
down_revision = '181196cb92fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
