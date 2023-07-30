"""show migration

Revision ID: 1db9f52bebac
Revises: a9b797a939d6
Create Date: 2023-07-29 14:04:40.456505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1db9f52bebac'
down_revision = 'a9b797a939d6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('show_id', sa.String(), nullable=False),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('rating', sa.String(), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('genres', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('directors', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('show_id')
    )
    op.create_index(op.f('ix_shows_show_id'), 'shows', ['show_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shows_show_id'), table_name='shows')
    op.drop_table('shows')
    # ### end Alembic commands ###