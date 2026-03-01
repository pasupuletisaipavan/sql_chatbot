import requests
import json

def generate(user_query, table_info):
    url = "http://localhost:11434/api/chat"
    print("Generating SQL query...")
    prompt = (
        "You are an expert SQL assistant. "
        "Given the following database schema:\n"
        f"{table_info}\n"
        "Write an SQLite SQL query (do not explain, only output the SQL) for this question:\n"
        f"{user_query}"
    )
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": "You are an expert SQL assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": True
    }
    response = requests.post(url, json=payload, stream=True)
    sql_query = ""
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line.decode("utf-8"))
            sql_query += chunk.get("message", {}).get("content", "")
    sql_query = sql_query.strip().strip("```sql").strip("```").strip()
    return sql_query