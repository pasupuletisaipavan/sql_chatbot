from schema_layer.schema_introspector import get_schema_summary
from database_path.sql_generator import generate_sql
from guardrails.sql_validator import validate_sql
from database_path.db_executor import execute_sql
from database_path.result_processor import process_rows

def orchestrate_query(question: str):
    schema = get_schema_summary()
    sql = generate_sql(question, schema)
    valid_sql = validate_sql(sql)
    columns, rows = execute_sql(valid_sql)
    processed_rows = process_rows(columns, rows)
    return {
        "answer": "Query executed successfully.",
        "sql_used": valid_sql,
        "rows": processed_rows
    }