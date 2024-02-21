import jaydebeapi

class H2Database:
    def __init__(self):
        self.jdbc_driver = "org.h2.Driver"
        self.url = "jdbc:h2:file:./h2Database"
        self.username = "sa"
        self.password = ""
        self.h2_jar_path = "h2.jar"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = jaydebeapi.connect(self.jdbc_driver, self.url, [self.username, self.password], self.h2_jar_path)
            self.cursor = self.connection.cursor()
            print("Connected to H2 database successfully!")
        except Exception as e:
            print("Error connecting to H2 database:", e)

    def close(self):
        if self.connection:
            self.connection.close()
            print("H2DB Connection closed.")

    def query(self, query):
        try:
            self.cursor.execute(query)
            print("Query executed successfully.")
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print("Error executing query:", e)

# Example usage
# if __name__ == "__main__":
#     db = H2Database()
#     db.connect()
    
#     # Execute a query
#     query = "SELECT * FROM EMPLOYEE"
#     rows = db.query(query)
#     if rows:
#         for row in rows:
#             print(row)

#     db.close()
