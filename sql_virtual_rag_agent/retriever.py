import requests
import sqlite3
import os

OLLAMA_URL = "http://localHost:11434/api/generate"

def embed(text):
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )
    return r.json()['embedding']

def retrieve_schema(query):
    emb = embed(query)
    docs = similarity_search(emb)
    return "\n".join(docs)

def execute_sql_query(db_path, sql_query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description] if cursor.description else []
        return columns, rows
    except Exception as e:
        return [], [f"SQL Error: {e}"]
    finally:
        conn.close()
    
def retrieve_schema_sql():
    from langchain_community.utilities import SQLDatabase
    db = SQLDatabase.from_uri(f"sqlite:///{os.getenv('DB_PATH')}")
    return db.get_table_info()  # Return the schema string