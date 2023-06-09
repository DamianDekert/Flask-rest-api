"""empty message

Revision ID: 526025f1b720
Revises: ade70f6e9c51
Create Date: 2023-06-08 17:47:23.682230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '526025f1b720'
down_revision = 'ade70f6e9c51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
