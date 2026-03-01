def build_prompt(table_info, user_query):
    prompt = (
        "You are an expert SQL assistant. "
        "Given the following database schema:\n"
        f"{table_info}\n"
        "Write an SQLite SQL query (do not explain, only output the SQL) for this question:\n"
        f"{user_query}"
    )
    return prompt

def repair_prompt(schema_context, user_query, error_message):
    return f"""The previous SQL query failed validation with error:\n{error_message}\n
        Database schema context:\n{schema_context}\n\n
        User question:\n{user_query}\n\n
        Write a corrected SELECT query. Only output SQL, no explanation."""
    

def retrieve_prompt(userQuery, sqlQuery, sqlResult):
    return f"""
        You are a precise data explainer that turns SQL query results into a direct, helpful answer to the user's natural language question.

        <{userQuery}>: the original natural language question from the user.
        <{sqlQuery}>: the SQL text executed (for context: do not restate uselsess asked).
        <{sqlResult}>: the tabular result, including column names and all rows
    """