# %%
import mysql.connector


# Connect to MySQL
def db_connection():
    db = mysql.connector.connect(
        host="3.138.156.32",
        port="3309",
        user="pruebas",
        password="VGbt3Day5R",
        database="habi_db"
    )
    return db


def filtered_search(db: mysql.connector.connect, year=None, city=None, status=None):
    condition = "WHERE 1=1"
    if year:
        try:
            year_int= int(year)
        except Exception:
            raise ValueError("The year should be a number")
        else:
            condition += f" AND year = {year_int}"

    if city:
        condition += f" AND city = '{city}'"
    if status:
        try:
            status_int = int(status)
        except Exception:
            raise ValueError("The status should be a number between 3 and 5")
        if 3 <= int(status_int) <= 5:
            raise ValueError("The status should be a number between 3 and 5")
        else:
            condition += f" AND stat_h.status_id  = {status_int}"
    else:
        condition += " AND (stat_h.status_id  = 3 or stat_h.status_id  = 4 or stat_h.status_id  = 5)"
    query = f'''SELECT * FROM property 
    INNER JOIN (
    SELECT *
    FROM status_history
    WHERE (property_id, update_date) IN (
        SELECT property_id, MAX(update_date)
        FROM status_history
        GROUP BY property_id
        )
    ) AS stat_h on property.id = stat_h.property_id
    inner join status as stat on stat_h.status_id = stat.id
    {condition} '''
    print(query)
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    return results
