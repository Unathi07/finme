"""Create the initial schema revision for future feature migrations.

The starter has no application tables yet. This no-op revision gives the
database a stable Alembic baseline before the first vertical slice adds tables.
"""

revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
