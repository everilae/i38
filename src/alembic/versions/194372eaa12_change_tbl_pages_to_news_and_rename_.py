"""Change tbl pages to news and rename page_ to site_

Revision ID: 194372eaa12
Revises: 63374da944
Create Date: 2014-05-25 23:12:33.913904

"""

# revision identifiers, used by Alembic.
revision = '194372eaa12'
down_revision = '63374da944'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('site_title', sa.UnicodeText(length=200), nullable=True),
    sa.Column('site_url', sa.String(length=2048), nullable=True),
    sa.Column('description', sa.UnicodeText(length=2048), nullable=True),
    sa.Column('vote_up', sa.Integer(), nullable=True),
    sa.Column('vote_down', sa.Integer(), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.Column('rank', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pages')
    op.add_column('comments', sa.Column('news_id', sa.Integer(), nullable=False))
    op.drop_column('comments', 'page_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('page_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('comments', 'news_id')
    op.create_table('pages',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('page_title', mysql.VARCHAR(collation='utf8_unicode_ci', length=200), nullable=True),
    sa.Column('page_url', mysql.VARCHAR(collation='utf8_unicode_ci', length=2048), nullable=True),
    sa.Column('description', mysql.VARCHAR(collation='utf8_unicode_ci', length=2048), nullable=True),
    sa.Column('rank', mysql.DECIMAL(precision=12, scale=2), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('comments', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('vote_down', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('vote_up', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('news')
    ### end Alembic commands ###
