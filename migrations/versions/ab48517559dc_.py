"""empty message

Revision ID: ab48517559dc
Revises: 988955190655
Create Date: 2019-11-21 10:33:32.912647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab48517559dc'
down_revision = '988955190655'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reclamacao', sa.Column('titulo', sa.String(length=60), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reclamacao', 'titulo')
    # ### end Alembic commands ###
