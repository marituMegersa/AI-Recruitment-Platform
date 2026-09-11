"""Add ORM relationships and foreign key indices

Revision ID: 002_orm_relationships
Revises: None
Create Date: 2026-09-11 08:30:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '002_orm_relationships'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_index('ix_recruitment_offices_company_id', 'recruitment_offices', ['company_id'], unique=False)
    op.create_index('ix_recruiter_practitioners_office_id', 'recruiter_practitioners', ['office_id'], unique=False)

def downgrade():
    op.drop_index('ix_recruiter_practitioners_office_id', table_name='recruiter_practitioners')
    op.drop_index('ix_recruitment_offices_company_id', table_name='recruitment_offices')
