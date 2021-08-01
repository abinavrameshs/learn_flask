import sqlite3

connection = sqlite3.connect(database='data.db')

cursor = connection.cursor()

table_users = "users"
# drop table
drop_cmd = f"drop table if exists {table_users} "
cursor.execute(drop_cmd)

# create table

create_statement = f"create table if not exists {table_users}  (id int, username text, password text);"

cursor.execute(create_statement)

# insert statement

user_tuple = (1, 'Abinav', 'abcd')
insert_statement = f"insert into {table_users}  values (?,?,?)"

cursor.execute(insert_statement,user_tuple )


## insert multiple

users = [
    (2, 'Nethra', 'bcdf'),
    (3, 'Rohit', 'adaa'),
    (4, 'Hajar', 'ab2312rwercd'),
    (5, 'Rida', 'hdhdsfhgdsjn')
]

cursor.executemany(insert_statement, users)

## select statement from sqllite

select_st = f"select * from {table_users} "

cursor.execute(select_st)


print(cursor.fetchall())

connection.commit()
connection.close()