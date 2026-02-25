import os
from typing import List, Optional, Dict
import json
from fastapi import APIRouter, HTTPException, Query, Response, status
import sqlite3


class UserStore:
    def __init__(self, dbpath):
        self.dbpath = dbpath
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.dbpath) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def __iter__(self):
        return iter(self._users)

    def save(self, userdata: dict):
        try:
            with sqlite3.connect(self.dbpath) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.execute("""
                    INSERT INTO users (name, email, password)
                    VALUES (?, ?, ?)
                """, (userdata["name"], userdata["email"], userdata["password"]))
                conn.commit()
                new_id = cursor.lastrowid
            return self.find_by_id(new_id)
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: users.email" in str(e):
                return "duplicate_email"
        raise e

    def load(self, where_clause: str = "", params: tuple = ()):
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            query = "SELECT id, name, email, password FROM users"
            if where_clause:
                query += f" {where_clause}"
            cursor = conn.execute(query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def find_by_id(self, user_id: int):
        results = self.load("WHERE id = ?", (user_id,))
        return results[0] if results else None

    def update_user(self, user_id: int, updated_data: dict):
        if not updated_data:
            return self.find_by_id(user_id)
        set_clause = ", ".join([f"{key} = ?" for key in updated_data.keys()])
        values = list(updated_data.values())
        values.append(user_id)
        try:
            with sqlite3.connect(self.dbpath) as conn:
                query = f"UPDATE users SET {set_clause} WHERE id = ?"
                cursor = conn.execute(query, values)
                conn.commit()
                if cursor.rowcount == 0:
                    return None
            return self.find_by_id(user_id)
        except sqlite3.IntegrityError:
            return "duplicate_email"

    def delete_user(self, user_id):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0