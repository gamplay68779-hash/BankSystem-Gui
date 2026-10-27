import sqlite3
import bcrypt


class BankDatabase:
    def __init__(self , db_name = "Bank_system.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL
)
""")
        self.cur.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_no TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL,
    balance REAL NOT NULL DEFAULT 0.0,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
""")
        self.cur.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_account TEXT,
    receiver_account TEXT,
    amount REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
        self.conn.commit()
    # hash password
    def _hash_pwd(self, password:str, rounds=12) -> bytes:
        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds))
        return password
    
    # Register
    def register_user(self, password:str, username:str, initial_deposit:float=0.0):
        try:
            salt = 12
            pwd_hash = self._hash_pwd(password, salt)
            self.cur.execute("""
INSERT INTO users (username , password_hash ,salt) VALUES (? , ? ,?)
""" , (username , pwd_hash , salt),)

            user_id = self.cur.lastrowid
            account_no = f"ACC-{user_id:04d}"

            self.cur.execute("""
INSERT INTO accounts (account_no , user_id , balance) VALUES (?,?,?)
""" , (account_no , user_id , initial_deposit),)
            return True , "Success register"
        except sqlite3.IntegrityError:
            print(f"[ERROR] Username '{username}' already exists.")
            return False , "Register invalid"

    # Check password is correctly
    def _check_pwd(self , password:str , hash:bytes) -> bool:
        return bcrypt.checkpw(password.encode() , hash)


    # Login
    def login(self, username : str, password:str):

        self.cur.execute("""
SELECT id , password_hash FROM users WHERE username = ?
""" , (username,))

        user = self.cur.fetchone()

        if not user:
            return None , "Login info invalid..."

        user_id , pwd_hash = user

        if not self._check_pwd(password , pwd_hash):
            return None , "Login info invalid..."

        return user_id

    def get_account_detail(self , user_id):

        self.cur.execute(
            "SELECT account_no , balance FROM accounts WHERE user_id = ?"
         , (user_id,))

        return self.cur.fetchall()

    def close(self):
       self.conn.close()