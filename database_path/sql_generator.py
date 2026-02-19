from src.utils.llm_client import llm_client

def generate_sql(question: str, schema_summary: str) -> str:
    prompt = (
        f"You are an expert SQL generator. Given the schema:\n{schema_summary}\n"
        f"Generate a single SELECT SQL query for the question: '{question}'.\n"
        "Only output the SQL query. No explanations, markdown, or comments."
    )
    return llm_client.generate_text(prompt)