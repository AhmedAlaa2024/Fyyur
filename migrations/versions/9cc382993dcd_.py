"""empty message

Revision ID: 9cc382993dcd
Revises: 8793b168c3b3
Create Date: 2020-10-24 22:25:31.556300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cc382993dcd'
down_revision = '8793b168c3b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('seekin_description', sa.String(), nullable=True))
    op.add_column('artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('venue', sa.Column('seekin_description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'seekin_description')
    op.drop_column('artist', 'seeking_venue')
    op.drop_column('artist', 'seekin_description')
    # ### end Alembic commands ###
