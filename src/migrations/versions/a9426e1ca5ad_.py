"""empty message

Revision ID: a9426e1ca5ad
Revises: fb1efe19f5f4
Create Date: 2023-06-29 23:11:42.076821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9426e1ca5ad'
down_revision = 'fb1efe19f5f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hikes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('depart_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hikes', schema=None) as batch_op:
        batch_op.drop_column('depart_date')

    # ### end Alembic commands ###