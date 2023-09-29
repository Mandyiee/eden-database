"""empty message

Revision ID: 768f57393836
Revises: 
Create Date: 2023-09-11 12:33:58.877880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '768f57393836'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('html_text', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('lexer', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_image_id'), ['id'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_image_id'))
        batch_op.drop_column('created')
        batch_op.drop_column('lexer')
        batch_op.drop_column('html_text')
        batch_op.drop_column('text')
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###
