import sqlite3

conn = sqlite3.connect("roles.db")
c = conn.cursor()

def commit():
	conn.commit()

def add_role_alias(role_id, alias):
	c.execute("INSERT INTO alias (alias, role_id) VALUES (?, ?)",
		[alias, role_id]
	)

def add_role_category(role_id, category)
	c.execute("INSERT INTO category (category, role_id) VALUES (?, ?)",
		[category, role_id]
	)

#def update_role(role_id, cateogry, alias):

def search_role(alias):
	return c.execute("SELECT role_id FROM alias WHERE alias=?")

#def delete_role(role_id):