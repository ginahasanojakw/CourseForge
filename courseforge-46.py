# === Stage 46: Add a schema version field and migration helper ===
# Project: CourseForge
SCHEMA_VERSION = 47


def migrate_to_v47(db):
    """Upgrade CourseForge schema from v46 to v47 by adding the schema_version column to all tables."""
    for table in TABLES:
        if not _col_exists(db, table, "schema_version"):
            db.execute(f"ALTER TABLE {table} ADD COLUMN schema_version INTEGER DEFAULT ?;", (SCHEMA_VERSION,))


def upgrade_schema():
    """Run the latest migration helper against the database."""
    migrate_to_v47(DB)
