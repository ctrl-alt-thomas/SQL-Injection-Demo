# SQL Injection Demo
This repo contains a small python script which is vulnerable to SQL injections.

The purpose of this repo is to provide a small environment to test SQL injection for educational purposes.

The database file contains 2 users:
- `alice` with password `l33t`
- `bob` with password `bobby123`

The database contains a single table which was created with:
```sql
CREATE TABLE "users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "username" TEXT UNIQUE NOT NULL,
  "password" TEXT NOT NULL
);
```
