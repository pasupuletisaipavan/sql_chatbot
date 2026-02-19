from src.core.config import get_session

def execute_sql(sql: str):
    session = get_session()
    result = session.execute(sql)
    rows = result.fetchall()
    columns = result.keys()
    return columns, rows