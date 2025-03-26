"""Added password field to UserProfile

Revision ID: 7396a109590a
Revises: c55e70350e6d
Create Date: 2025-03-26 14:02:54.666990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7396a109590a'
down_revision = 'c55e70350e6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=False))
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('password')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
