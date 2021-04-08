CREATE TABLE alias (
	alias TEXT,
	role_id INTEGER NOT NULL,
	PRIMARY KEY(alias)
);

CREATE TABLE category (
	role_id INTEGER NOT NULL,
	category TEXT,
	PRIMARY KEY(role_id)
);