
import sqlite3

conn = sqlite3.connect("crm.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        employee_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL DEFAULT 'Новая'
            CHECK(status IN ('Новая', 'В работе', 'Завершена', 'Отменена')),
        FOREIGN KEY (client_id) REFERENCES clients(id)
            ON DELETE CASCADE,
        FOREIGN KEY (employee_id) REFERENCES employees(id)
    )
""")

conn.commit()


def add_client():
    name = input("Имя клиента: ")
    phone = input("Телефон: ")
    email = input("Email: ")

    cursor.execute(
        "INSERT INTO clients (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email)
    )
    conn.commit()
    print("Клиент добавлен!")


def add_employee():
    name = input("Имя сотрудника: ")
    position = input("Должность: ")

    cursor.execute(
        "INSERT INTO employees (name, position) VALUES (?, ?)",
        (name, position)
    )
    conn.commit()
    print("Сотрудник добавлен!")


def show_clients():
    cursor.execute("SELECT * FROM clients ORDER BY id")
    clients = cursor.fetchall()

    if not clients:
        print("Клиентов нет.")
        return

    for client in clients:
        print(client)


def show_employees():
    cursor.execute("SELECT * FROM employees ORDER BY id")
    employees = cursor.fetchall()

    if not employees:
        print("Сотрудников нет.")
        return

    for employee in employees:
        print(employee)


def create_deal():
    show_clients()
    client_id = input("ID клиента: ")

    show_employees()
    employee_id = input("ID сотрудника: ")

    try:
        amount = float(input("Сумма сделки: "))
        if amount < 0:
            print("Сумма не может быть отрицательной.")
            return
    except ValueError:
        print("Введите корректную сумму.")
        return

    cursor.execute(
        "SELECT id FROM clients WHERE id = ?", (client_id,)
    )
    if cursor.fetchone() is None:
        print("Клиент не найден.")
        return

    cursor.execute(
        "SELECT id FROM employees WHERE id = ?", (employee_id,)
    )
    if cursor.fetchone() is None:
        print("Сотрудник не найден.")
        return

    cursor.execute("""
        INSERT INTO deals (client_id, employee_id, amount, status)
        VALUES (?, ?, ?, 'Новая')
    """, (client_id, employee_id, amount))

    conn.commit()
    print("Сделка создана!")


def show_deals():
    cursor.execute("""
        SELECT deals.id, clients.name, employees.name,
               deals.amount, deals.status
        FROM deals
        JOIN clients ON deals.client_id = clients.id
        JOIN employees ON deals.employee_id = employees.id
        ORDER BY deals.id
    """)

    deals = cursor.fetchall()

    if not deals:
        print("Сделок нет.")
        return

    for deal in deals:
        print(
            f"ID: {deal[0]} | Клиент: {deal[1]} | "
            f"Сотрудник: {deal[2]} | Сумма: {deal[3]} | "
            f"Статус: {deal[4]}"
        )


def search_client():
    search = input("Введите имя или телефон клиента: ")

    cursor.execute("""
        SELECT * FROM clients
        WHERE name LIKE ? OR phone LIKE ?
        ORDER BY name
    """, (f"%{search}%", f"%{search}%"))

    clients = cursor.fetchall()

    if not clients:
        print("Клиенты не найдены.")
        return

    for client in clients:
        print(client)


def change_deal_status():
    show_deals()

    deal_id = input("ID сделки: ")
    print("1. Новая")
    print("2. В работе")
    print("3. Завершена")
    print("4. Отменена")

    statuses = {
        "1": "Новая",
        "2": "В работе",
        "3": "Завершена",
        "4": "Отменена"
    }

    choice = input("Выберите новый статус: ")

    if choice not in statuses:
        print("Неверный статус.")
        return

    cursor.execute(
        "SELECT id FROM deals WHERE id = ?", (deal_id,)
    )

    if cursor.fetchone() is None:
        print("Сделка не найдена.")
        return

    cursor.execute(
        "UPDATE deals SET status = ? WHERE id = ?",
        (statuses[choice], deal_id)
    )

    conn.commit()
    print("Статус изменён!")


def delete_client():
    show_clients()
    client_id = input("ID клиента для удаления: ")

    cursor.execute(
        "SELECT id FROM clients WHERE id = ?", (client_id,)
    )

    if cursor.fetchone() is None:
        print("Клиент не найден.")
        return

    cursor.execute(
        "DELETE FROM clients WHERE id = ?", (client_id,)
    )

    conn.commit()
    print("Клиент и его сделки удалены!")


def count_clients():
    cursor.execute("SELECT COUNT(*) FROM clients")
    print("Количество клиентов:", cursor.fetchone()[0])


def completed_deals_sum():
    cursor.execute("""
        SELECT SUM(amount) FROM deals
        WHERE status = 'Завершена'
    """)

    result = cursor.fetchone()[0]
    print("Сумма завершённых сделок:", result or 0)


def average_deal():
    cursor.execute("SELECT AVG(amount) FROM deals")
    result = cursor.fetchone()[0]
    print("Средняя сумма сделки:", result if result is not None else 0)


def max_min_deal():
    cursor.execute("""
        SELECT MAX(amount), MIN(amount) FROM deals
    """)

    max_amount, min_amount = cursor.fetchone()

    print("Самая дорогая сделка:", max_amount if max_amount is not None else 0)
    print("Самая дешёвая сделка:", min_amount if min_amount is not None else 0)


def employee_deal_count():
    cursor.execute("""
        SELECT employees.name, COUNT(deals.id)
        FROM employees
        LEFT JOIN deals ON employees.id = deals.employee_id
        GROUP BY employees.id, employees.name
        ORDER BY employees.name
    """)

    for row in cursor.fetchall():
        print(f"Сотрудник: {row[0]} | Количество сделок: {row[1]}")


def employee_completed_sum():
    cursor.execute("""
        SELECT employees.name, COALESCE(SUM(deals.amount), 0)
        FROM employees
        LEFT JOIN deals
            ON employees.id = deals.employee_id
            AND deals.status = 'Завершена'
        GROUP BY employees.id, employees.name
        ORDER BY employees.name
    """)

    for row in cursor.fetchall():
        print(f"Сотрудник: {row[0]} | Завершённые сделки: {row[1]}")


def employees_above_amount():
    try:
        amount = float(input("Введите минимальную сумму: "))
    except ValueError:
        print("Введите корректную сумму.")
        return

    cursor.execute("""
        SELECT employees.name, SUM(deals.amount) AS total
        FROM employees
        JOIN deals ON employees.id = deals.employee_id
        WHERE deals.status = 'Завершена'
        GROUP BY employees.id, employees.name
        HAVING SUM(deals.amount) > ?
        ORDER BY total DESC
    """, (amount,))

    results = cursor.fetchall()

    if not results:
        print("Подходящих сотрудников нет.")
        return

    for row in results:
        print(f"Сотрудник: {row[0]} | Общая сумма: {row[1]}")


def menu():
    while True:
        print("\n===== CRM-СИСТЕМА =====")
        print("1. Добавить клиента")
        print("2. Добавить сотрудника")
        print("3. Создать сделку")
        print("4. Показать всех клиентов")
        print("5. Показать все сделки")
        print("6. Найти клиента")
        print("7. Изменить статус сделки")
        print("8. Удалить клиента")
        print("9. Количество клиентов")
        print("10. Сумма завершённых сделок")
        print("11. Средняя сумма сделки")
        print("12. Самая дорогая и дешёвая сделка")
        print("13. Количество сделок каждого сотрудника")
        print("14. Сумма завершённых сделок по сотрудникам")
        print("15. Сотрудники с суммой выше заданной")
        print("16. Показать сотрудников")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_client()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            create_deal()
        elif choice == "4":
            show_clients()
        elif choice == "5":
            show_deals()
        elif choice == "6":
            search_client()
        elif choice == "7":
            change_deal_status()
        elif choice == "8":
            delete_client()
        elif choice == "9":
            count_clients()
        elif choice == "10":
            completed_deals_sum()
        elif choice == "11":
            average_deal()
        elif choice == "12":
            max_min_deal()
        elif choice == "13":
            employee_deal_count()
        elif choice == "14":
            employee_completed_sum()
        elif choice == "15":
            employees_above_amount()
        elif choice == "16":
            show_employees()
        elif choice == "0":
            conn.close()
            print("Программа завершена.")
            break
        else:
            print("Неверный пункт меню.")


menu()
