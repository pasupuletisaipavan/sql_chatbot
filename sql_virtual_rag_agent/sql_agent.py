from retriever import execute_sql_query, retrieve_schema_sql
from prompts import build_prompt, repair_prompt
from model import generate
from validator import validate
import os
import requests
import json

def verify_sql_with_llm(schema, question, sql_query):
    print("Verifying whether the generated sql is correct or not...")
    url = "http://localhost:11434/api/chat"
    verify_prompt = (
        "You are an expert SQL assistant.\n"
        f"Given the following database schema:\n{schema}\n"
        f"Question: {question}\n"
        f"SQL: {sql_query}\n"
        "Is the SQL query correct for the question and schema? Respond with 'YES' or 'NO' only."
    )
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": "You are an expert SQL assistant."},
            {"role": "user", "content": verify_prompt}
        ],
        "stream": False
    }
    response = requests.post(url, json=payload)
    try:
        response.raise_for_status()
        data = response.json()
        return data.get("message", {}).get("content", data.get("response", ""))
    except Exception as e:
        print("Raw response text:", response.text)
        raise e
    
class SQLAgent:
    def run(self, question):
        schema = retrieve_schema_sql()
        sql = generate(question, schema)
        print("Generated SQL:", sql)
        attempts = 0
        while attempts < 3:
            valid, err = validate(sql)
            if valid:
                # verification = verify_sql_with_llm(schema, question, sql)
                # print("Verification prompt:", verification)
                # if "YES" in verification.upper():
                db_path = os.getenv("DB_URL")
                columns, rows = execute_sql_query(db_path, sql)
                return {
                    "sql_query": sql,
                    "sql_results": (columns, rows)
                }
                # else:
                #     print("LLM flagged SQL as incorrect")
                #     repair_sql = generate(
                #         repair_prompt(schema, sql, err), schema
                #     )
                #     sql = repair_sql
            else:
                repair_sql = generate(
                    repair_prompt(schema, sql, err), schema
                )
                sql = repair_sql
            attempts += 1
        raise Exception("Failed to generate valid SQL")