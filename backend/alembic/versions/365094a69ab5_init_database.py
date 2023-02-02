"""Init database

Revision ID: 365094a69ab5
Revises: 
Create Date: 2023-02-02 11:27:15.494523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '365094a69ab5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        create table campus (
            id uuid NOT NULL PRIMARY KEY,
            name VARCHAR (50) NOT NULL,
            rank INTEGER NOT NULL
        )
    """)
    op.execute("""
        create table users (
            id uuid NOT NULL PRIMARY KEY,
            uname VARCHAR (50),
            dname VARCHAR (50),
            email VARCHAR (50),
            github VARCHAR (50),
            rank INTEGER NOT NULL,
            campus_id uuid REFERENCES campus ON DELETE SET NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)


def downgrade() -> None:
    op.execute("drop table users")
    op.execute("drop table campus")
