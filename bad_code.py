# Hardcoded credentials (security flaw)
username = "admin"
password = "password123"

# Insecure input handling (command injection vulnerability)
user_input = input("Enter a command: ")
print("Executing:", user_input)
exec(user_input)

# Insecure SQL query (SQL injection vulnerability)
user_id = input("Enter user ID: ")
query = "SELECT * FROM users WHERE id = '" + user_id + "';"
print("Query:", query)