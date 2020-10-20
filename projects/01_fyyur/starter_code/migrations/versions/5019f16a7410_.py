"""empty message

Revision ID: 5019f16a7410
Revises: ade0d5d55522
Create Date: 2020-10-16 20:36:12.281994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5019f16a7410'
down_revision = 'ade0d5d55522'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.drop_constraint('Show_venue_fkey', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    op.drop_column('Show', 'venue')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('venue', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('Show_venue_fkey', 'Show', 'Venue', ['venue'], ['id'])
    op.drop_column('Show', 'venue_id')
    # ### end Alembic commands ###