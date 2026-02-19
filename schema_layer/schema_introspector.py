from sqlalchemy import inspect
from src.core.config import get_engine

def get_schema_summary():
    engine = get_engine()
    inspector = inspect(engine)
    summary = []
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        col_info = [f"{col['name']} ({col['type']})" for col in columns]
        summary.append(f"Table: {table_name}\nColumns: {', '.join(col_info)}")
    return "\n\n".join(summary)