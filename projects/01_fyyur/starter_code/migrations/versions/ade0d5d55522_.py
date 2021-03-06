"""empty message

Revision ID: ade0d5d55522
Revises: ffc8b14045bc
Create Date: 2020-10-15 01:05:10.735525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ade0d5d55522'
down_revision = 'ffc8b14045bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Venue_past_shows_id_fkey', 'Venue', type_='foreignkey')
    op.drop_constraint('Venue_upcoming_shows_id_fkey', 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'upcoming_shows_id')
    op.drop_column('Venue', 'past_shows_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('past_shows_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Venue_upcoming_shows_id_fkey', 'Venue', 'Show', ['upcoming_shows_id'], ['id'])
    op.create_foreign_key('Venue_past_shows_id_fkey', 'Venue', 'Show', ['past_shows_id'], ['id'])
    # ### end Alembic commands ###
