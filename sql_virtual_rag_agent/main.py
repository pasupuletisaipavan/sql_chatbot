from sql_agent import SQLAgent
import dotenv

dotenv.load_dotenv()
agent = SQLAgent()

query = "List all the students and their marks whose marks are above than the average"
result = agent.run(query)

sql_query = result["sql_query"]
print(f"\nSQL Query Generated is: \n{sql_query}")

columns,rows = result["sql_results"]
print(f"\nResults:")
print(columns)
for row in rows:
    print(row)