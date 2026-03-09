import sqlite3

conn = sqlite3.connect("MachineTest.db")
cursor = conn.cursor()

#lakCreate table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Candidates(
    StudentName TEXT,
    CollegeName TEXT,
    Round1Marks FLOAT,
    Round2Marks FLOAT,
    Round3Marks FLOAT,
    TechnicalRoundMarks FLOAT,
    TotalMarks FLOAT,
    Result TEXT,
    Rank NUMBER
)
""")

name = input("Enter Student Name: ")
while len(name) > 30:
    print("Maximum 30 characters allowed!")
    name = input("Enter Student Name again: ")

college = input("Enter College Name: ")
while len(college) > 50:
    print("Maximum 50 characters allowed!")
    college = input("Enter College Name again: ")

r1 = float(input("Enter Round 1 Marks (0-10): "))
while r1 < 0 or r1 > 10:
    print("Marks must be between 0 and 10")
    r1 = float(input("Enter Round 1 Marks again: "))

r2 = float(input("Enter Round 2 Marks (0-10): "))
while r2 < 0 or r2 > 10:
    print("Marks must be between 0 and 10")
    r2 = float(input("Enter Round 2 Marks again: "))

r3 = float(input("Enter Round 3 Marks (0-10): "))
while r3 < 0 or r3 > 10:
    print("Marks must be between 0 and 10")
    r3 = float(input("Enter Round 3 Marks again: "))

tech = float(input("Enter Technical Round Marks (0-20): "))
while tech < 0 or tech > 20:
    print("Marks must be between 0 and 20")
    tech = float(input("Enter Technical Round Marks again: "))

total = r1 + r2 + r3 + tech

if total >= 35:
    result = "Selected"
else:
    result = "Rejected"

cursor.execute("INSERT INTO Candidates VALUES (?,?,?,?,?,?,?,?,?)",
               (name, college, r1, r2, r3, tech, total, result, 0))

conn.commit()


cursor.execute("SELECT rowid, TotalMarks FROM Candidates ORDER BY TotalMarks DESC")
data = cursor.fetchall()

rank = 1
for i in range(len(data)):
    cursor.execute("UPDATE Candidates SET Rank=? WHERE rowid=?", (i+1, data[i][0]))

conn.commit()

print("\n----- Candidate List -----")

cursor.execute("SELECT StudentName, TotalMarks, Result, Rank FROM Candidates ORDER BY Rank")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()