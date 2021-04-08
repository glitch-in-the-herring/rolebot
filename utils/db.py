import sqlite3

conn = sqlite3.connect("necromancy.db")
c = conn.cursor()

def commit():
	conn.commit()

def add_role(role_id, category, alias):
	c.execute("INSERT INTO alias (alias, role_id) VALUES (?, ?)",
		[alias, role_id]
	)
	c.execute("INSERT INTO category (category, role_id) VALUES (?, ?)",
		[category, role_id]
	)

def update_role(role_id, cateogry, alias):

def search_role(role_id, alias):

def delete_role(role_id):