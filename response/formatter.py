def format_response(answer: str, sql_used: str, rows: list):
    return {
        "answer": answer,
        "sql_used": sql_used,
        "rows": rows
    }