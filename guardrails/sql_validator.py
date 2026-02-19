FORBIDDEN = ["DROP", "DELETE", "UPDATE", "INSERT", "TRUNCATE", "ALTER"]

def validate_sql(sql: str) -> str:
    sql_upper = sql.strip().upper()
    if not sql_upper.startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")
    for forbidden in FORBIDDEN:
        if forbidden in sql_upper:
            raise ValueError(f"Forbidden SQL keyword detected: {forbidden}")
    if "LIMIT" not in sql_upper:
        sql = sql.rstrip(";") + " LIMIT 1000;"
    return sql