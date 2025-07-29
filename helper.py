# Helper script for Pet Clinic project

import sqlite3
import pandas as pd
import csv  # Used to read CSV data before inserting into SQLite

# Connect to the database
conn = sqlite3.connect("pet_clinic.db")
cursor = conn.cursor()

# Make sure foreign key constraints are enforced
cursor.execute("PRAGMA foreign_keys = ON;")

# Create table: owners
cursor.execute("""
CREATE TABLE IF NOT EXISTS owners (
    id TEXT PRIMARY KEY,
    name TEXT,
    license_status INTEGER,
    license_date_created TEXT
)
""")

# Create table: pets
cursor.execute("""
CREATE TABLE IF NOT EXISTS pets (
    pet_id TEXT PRIMARY KEY,
    pet_name TEXT,
    animal_type TEXT,
    age REAL,
    owners_id TEXT,
    FOREIGN KEY (owners_id) REFERENCES owners(id)
)
""")

# Load and insert owners.csv
with open("owners.csv", "r", encoding="utf-8") as file:
    dr = csv.DictReader(file)
    to_db = [
        (
            row["id"],
            row["name"],
            int(row["license_status"]),
            row["license_date_created"]
        )
        for row in dr
    ]

cursor.executemany(
    "INSERT INTO owners (id, name, license_status, license_date_created) VALUES (?, ?, ?, ?);",
    to_db
)

# Load and insert pets.csv
with open("pets.csv", "r", encoding="utf-8") as file:
    dr = csv.DictReader(file)
    to_db = [
        (
            row["pet_id"],
            row["pet_name"],
            row["animal_type"],
            float(row["age"]),
            row["owners_id"]
        )
        for row in dr
    ]

cursor.executemany(
    "INSERT INTO pets (pet_id, pet_name, animal_type, age, owners_id) VALUES (?, ?, ?, ?, ?);",
    to_db
)

# Commit and close the connection
conn.commit()
conn.close()

# Part 0
# Initial Data Exploration

# Reconnect to the database
conn = sqlite3.connect("pet_clinic.db")
cursor = conn.cursor()

# View the first 5 data from table owners
print("Owners Table Sample:")
owners_df = pd.read_sql_query("SELECT * FROM owners LIMIT 5;", conn)
print(owners_df)

# View the first 5 data from table pets
print("\nPets Table Sample:")
pets_df = pd.read_sql_query("SELECT * FROM pets LIMIT 5;", conn)
print(pets_df)

conn.close()

# Query 1
# Most Common Animal Types
query = """
SELECT animal_type, COUNT(*) AS total
FROM pets
GROUP BY animal_type
ORDER BY total DESC;
"""

with sqlite3.connect("pet_clinic.db") as conn:
    df = pd.read_sql_query(query, conn)

df

# Query 2
# query = """
SELECT animal_type, ROUND(AVG(age), 2) AS average_age
FROM pets
GROUP BY animal_type
ORDER BY average_age DESC;
"""

with sqlite3.connect("pet_clinic.db") as conn:
    df = pd.read_sql_query(query, conn)

df

# Query 2 extension
# Visualization: Distribution of Pet Ages by Animal Type

import seaborn as sns
import matplotlib.pyplot as plt

# Reconnect and load data
conn = sqlite3.connect("pet_clinic.db")
pets_df = pd.read_sql_query("SELECT * FROM pets;", conn)
conn.close()

plt.figure(figsize=(8,5))
sns.boxplot(data=pets_df, x="animal_type", y="age")
plt.title("Age Distribution by Animal Type")
plt.xlabel("Animal Type")
plt.ylabel("Age")
plt.tight_layout()
plt.show()

# Query 3
# Number of Pets per Owner
query = """
SELECT o.name AS owner_name, COUNT(p.pet_id) AS total_pets
FROM owners o
LEFT JOIN pets p ON o.id = p.owners_id
GROUP BY o.name
ORDER BY total_pets DESC;
"""

with sqlite3.connect("pet_clinic.db") as conn:
    df = pd.read_sql_query(query, conn)

df

# Query 4
# License Status Distribution of Pet Owners
query = """
SELECT license_status, COUNT(*) AS total
FROM owners
GROUP BY license_status;
"""

with sqlite3.connect("pet_clinic.db") as conn:
    df = pd.read_sql_query(query, conn)

df.head()

# Query 4 extensions
# Visualization: Owner License Status Breakdown
# Reconnect and get data
conn = sqlite3.connect("pet_clinic.db")

# Query grouped license status counts
license_df = pd.read_sql_query("""
    SELECT license_status, COUNT(*) AS total
    FROM owners
    GROUP BY license_status;
""", conn)

conn.close()

# Map binary status to descriptive labels
license_df["status"] = license_df["license_status"].map({0: "Inactive", 1: "Active"})

# Plot pie chart
plt.figure(figsize=(5,5))
plt.pie(
    license_df["total"],
    labels=license_df["status"],
    autopct="%1.1f%%",
    colors=["#F44336", "#4CAF50"],  # red for Inactive, green for Active
    startangle=90
)
plt.title("License Status of Pet Owners")
plt.tight_layout()
plt.show()

# Query 5
# Finding All Pets Belonging to a Specific Owner (e.g. Willand)
query = """
SELECT pet_id, 
       pet_name,
       animal_type
FROM pets
WHERE owners_id = 'X002';
"""

with sqlite3.connect("pet_clinic.db") as conn:
    df = pd.read_sql_query(query, conn)

df