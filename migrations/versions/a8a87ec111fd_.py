"""empty message

Revision ID: a8a87ec111fd
Revises: ef31e9fec04c
Create Date: 2021-06-13 17:20:17.362299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8a87ec111fd'
down_revision = 'ef31e9fec04c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('manage', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('manage', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###