import sqlite3

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

cursor.execute('''
    create table if not exists users (
        id integer primary key, 
        name text not null
    )
''')

cursor.execute('''
    create table if not exists orders (
        id integer primary key, 
        user_id integer,
        amount real,
        foreign key (user_id) references users(id)
    )
''')

cursor.executemany(
    "insert into users (name) values (?)",
    [("Alice",), ("Bob",), ("Charlie",)]
)

cursor.executemany(
    "insert into orders (user_id, amount) values (?, ?)",
    [
        (1, 1500),
        (1, 2000),
        (2, 5000),
        (3, 3000),
    ]
)

conn.commit()

cursor.execute('''
    select users.name, orders.amount
    from users 
    join orders on users.id = orders.user_id
''')

for row in cursor.fetchall():
    print(row)

cursor.execute('''
    select count(*) from orders
''')
print("Total orders:", cursor.fetchone()[0])

cursor.execute('''
    select sum(amount) from orders
''')
print("Total amount:", cursor.fetchone()[0])

cursor.execute('''
    select users.name, sum(orders.amount) as total
    from users
    join orders on users.id = orders.user_id
    group by users.id, users.name
''')

for row in cursor.fetchall():
    print(f"User: {row[0]}, Total amount: {row[1]}")

cursor.execute('''
    select users.name, orders.amount
    from users
    join orders on users.id = orders.user_id
    where orders.amount <= 3000
''')

print("Orders up to 3000:")
for row in cursor.fetchall():
    print(row)