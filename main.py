import sqlite3

conn = sqlite3.connect('database.db')



while True:
    try:
      user = input("Enter your username: ")
      password = input("Enter your password: ")
      cur = conn.cursor()
      cur.execute(f"SELECT id, username FROM users WHERE username = '{user}' AND password = '{password}'")
      match = cur.fetchone()

      if match is None:
          print("You are a faker.")
      else:
          print(f"Welcome {match[1]}!")
    except:
        print("Internal Error: Something went wrong! Try again.")