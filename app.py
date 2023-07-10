import connexion
import sqlite3

class StackCalc:
    def __init__(self):
        self.connector = sqlite3.connect('stack.db', check_same_thread=False)
        self.cursor = self.connector.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS stackids (id TEXT PRIMARY KEY)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS stackvalues (id TEXT, value INTEGER, FOREIGN KEY(id) REFERENCES stackids(id))')               
    
    

    def push(self, id, n):
        try:
            self.cursor.execute('INSERT OR IGNORE INTO stackids (id) VALUES (?)', (id,))
            self.cursor.execute('INSERT INTO stackvalues (id, value) VALUES (?, ?)', (id, n))
            self.connector.commit()
            return n, 200
        except sqlite3.Error as e:
            errormsg = str(e)
            print(f'database error: {errormsg}')
            return 'Failed to push onto stack', 500

    def pop(self, id):
        self.cursor.execute('''SELECT value FROM stackvalues WHERE id=? ORDER BY rowid DESC LIMIT 1''', (id,))
        result = self.cursor.fetchone()
        if result is not None:
            value = result[0]
            self.cursor.execute('''DELETE FROM stackvalues WHERE id=? AND value=?''', (id, value))
            self.connector.commit()
            return value, 200
        else:
            return 'Not enough values on stack', 400
        
    def add(self, id):
        self.cursor.execute('SELECT value FROM stackvalues WHERE id=? ORDER BY rowid DESC LIMIT 2', (id,))
        fetch = self.cursor.fetchall()
        if len(fetch) >= 2:
            last = fetch[0][0]
            next_value = fetch[1][0]
            result = last + next_value
            self.cursor.execute('INSERT INTO stackvalues (id, value) VALUES (?, ?)', (id, result))
            self.connector.commit()
            return result, 200
        else:
            return 'Not enough values on stack', 400

    def subtract(self, id):
        self.cursor.execute('SELECT value FROM stackvalues WHERE id=? ORDER BY rowid DESC LIMIT 2', (id,))
        fetch = self.cursor.fetchall()
        if len(fetch) >= 2:
            last = fetch[0][0]
            next_value = fetch[1][0]
            result = last - next_value
            self.cursor.execute('INSERT INTO stackvalues (id, value) VALUES (?, ?)', (id, result))
            self.connector.commit()
            return result, 200
        else:
            return 'Not enough values on stack', 400

    def multiply(self, id):
        self.cursor.execute('SELECT value FROM stackvalues WHERE id=? ORDER BY rowid DESC LIMIT 2', (id,))
        fetch = self.cursor.fetchall()
        if len(fetch) >= 2:
            last = fetch[0][0]
            next_value = fetch[1][0]
            result = last * next_value
            self.cursor.execute('INSERT INTO stackvalues (id, value) VALUES (?, ?)', (id, result))
            self.connector.commit()
            return result, 200
        else:
            return 'Not enough values on stack', 400
    
    def divide(self, id):
        self.cursor.execute('SELECT value FROM stackvalues WHERE id=? ORDER BY rowid DESC LIMIT 2', (id,))
        fetch = self.cursor.fetchall()
        if len(fetch) >= 2:
            last = fetch[0][0]
            next_value = fetch[1][0]
            result = last / next_value
            self.cursor.execute('INSERT INTO stackvalues (id, value) VALUES (?, ?)', (id, result))
            self.connector.commit()
            return result, 200
        else:
            return 'Not enough values on stack', 400     
        
    def peek(self, id):
        self.cursor.execute('SELECT value FROM stackvalues WHERE id=? ORDER BY rowid DESC LIMIT 1', (id,))
        fetch = self.cursor.fetchone()
        return fetch[0]
    
app = connexion.FlaskApp(__name__)
app.add_api("swagger.yml")

StackCalc = StackCalc()

if __name__ == "__main__":
    app.run(port=8000, debug=True)
