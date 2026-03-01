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

import psycopg2

def execute_sql_query(db_url, sql_query):
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return columns, rows
    except Exception as e:
        return [], [f"SQL Error: {e}"]
    finally:
        cursor.close()
        conn.close()
    
def retrieve_schema_sql():
    from langchain_community.utilities import SQLDatabase
    db = SQLDatabase.from_uri(f"sqlite:///{os.getenv('DB_PATH')}")
    return db.get_table_info()  # Return the schema string