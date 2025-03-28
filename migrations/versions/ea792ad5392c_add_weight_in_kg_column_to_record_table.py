"""Add weight_in_kg column to record table

Revision ID: ea792ad5392c
Revises: 
Create Date: 2025-03-28 12:35:27.723799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea792ad5392c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weight_in_kg', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('unit', sa.String(length=10), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.drop_column('unit')
        batch_op.drop_column('weight_in_kg')

    # ### end Alembic commands ###
