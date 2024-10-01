import matplotlib.pyplot as plt
import mysql.connector as mc

# CSCI3329 OOP in python homework 2 with Dr. Kim
# Database class to manage the database connection and operations
class Database:
    def __init__(self):
        self.db = mc.connect(host="35.223.149.83", user="root", passwd="password123", database="carmax")

    def get_cursor(self):
        return self.db.cursor()

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()



print("hi")
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.plot(x, y, marker='o', markerfacecolor='blue', linestyle='-', linewidth=2, color='blue')
plt.title('Basic Line Graph of x squared')
plt.xlabel('x value')
plt.ylabel('x squared')
plt.show()

