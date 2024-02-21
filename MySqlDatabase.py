import mysql.connector

class MySqlDatabase:
    def __init__(self):
        self.host = "localhost"
        self.port = "3306"
        self.user = "root"
        self.password = "root"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print("Connected to MYSQL database successfully!")
        except mysql.Error as e:
            print("Error connecting to database:", e)

    def close(self):
        if self.connection:
            self.connection.close()
            print("MYSQL Connection closed.")

    def query(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print("Error executing query:", e)

# Example usage
# if __name__ == "__main__":
#     host = "localhost"
#     port = "3306"
#     user = "root"
#     password = "root"

#     db = MySqlDatabase(host, port, user, password)
#     db.connect()
    
#     # Query the data
#     select_query = "SELECT * FROM test.employee"
#     db.query(select_query)

#     db.close()
