import database

def add_part(name, category,qty, reorder_point, description) :
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO parts (name, category, qty, reorder_point, description) VALUES (?, ?, ?, ?, ?)",
        (name, category,qty, reorder_point, description)
    )
    conn.commit()
    conn.close()

def adjust_quantity(part_id, change):
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT qty FROM parts WHERE id = ?", (part_id,)) 
    row = cursor.fetchone()
    if row is None:
        conn.close()
        return False
    
    new_qty = row[0] + change
    cursor.execute("UPDATE parts SET qty = ? WHERE id = ?", (new_qty, part_id))
    conn.commit()
    conn.close()
    return True
