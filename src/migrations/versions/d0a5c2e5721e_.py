"""empty message

Revision ID: d0a5c2e5721e
Revises: a9426e1ca5ad
Create Date: 2023-07-02 14:55:22.094177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0a5c2e5721e'
down_revision = 'a9426e1ca5ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hikes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cover', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hikes', schema=None) as batch_op:
        batch_op.drop_column('cover')

    # ### end Alembic commands ###
