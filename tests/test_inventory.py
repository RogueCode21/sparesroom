import pytest
import sqlite3
import inventory
import database

@pytest.fixture
def temp_db(monkeypatch, tmp_path):
    test_db_path = tmp_path / "test_sparesroom.db"
    monkeypatch.setattr(database, "DB_PATH", str(test_db_path))
    yield test_db_path

def test_add_part_inserts_row(temp_db):
    inventory.add_part("Test bolt","Fasteners", 10, 5, "M8 hex bolt")

    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, category, qty FROM parts WHERE name = ?", ("Test bolt",))
    row = cursor.fetchone()
    conn.close()

    assert row is not None
    assert row[0] == "Test bolt"
    assert row[1] == "Fasteners"
    assert row[2] == 10

def test_adjust_quantity_increases_qty(temp_db):
    inventory.add_part("Test bolt", "Fasterners", 10, 5, "M8 hex bolt")

    conn = database.get_connection()
    part_id = conn.execute("SELECT id FROM parts WHERE name = ?", ("Test bolt",)).fetchone()[0]
    conn.close()

    result = inventory.adjust_quantity(part_id, 5)

    conn = database.get_connection()
    new_qty = conn.execute("SELECT qty FROM parts WHERE id = ?", (part_id,)).fetchone()[0]
    conn.close()

    assert result is True
    assert new_qty == 15

def test_adjust_quantity_missing_part_return_false(temp_db):
    result = inventory.adjust_quantity(9999, 5)
    assert result is False