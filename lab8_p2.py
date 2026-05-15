from lab8_p1 import Table
from typing import Optional, Tuple

TOMBSTONE = (100000, "")

def hash_fn(entry: Tuple[int, str], size: int) -> int:
    """
    Hashes the key of an entry using modulo.
    """
    key = entry[0]
    return key % size

def insert(table: Table, entry: Tuple[int, str]) -> Table:
    """
    Inserts a (key, value) entry using linear probing.
    Reuses tombstone slots if found.
    Overwrites if the key already exists.
    """
    index = hash_fn(entry, table.size)
    start_index = index

    while table.data[index] is not None and table.data[index] != TOMBSTONE:        
        if table.data[index][0] == entry[0]:
            break

        index = (index + 1) % table.size

        if index == start_index:
            raise OverflowError("Table is full")
        
    new_data = table.data[:]
    new_data[index] = entry
    return Table(size=table.size, data=new_data)



def delete(table: Table, key: int) -> Table:
    """
    Deletes the entry with the given key by marking the slot with TOMBSTONE.
    """
    index = key % table.size
    start_index = index
    while table.data[index] is not None:
        if table.data[index] != TOMBSTONE and table.data[index][0] == key:
            new_data = table.data[:]
            new_data[index] = TOMBSTONE
            return Table(table.size, new_data)

        index = (index + 1) % table.size

        if index == start_index:
            break

    raise ValueError("Key not found")

def get(table: Table, key: int) -> Optional[str]:
    """
    Retrieves the value associated with the given key using linear probing.
    Skips over tombstones.
    Returns None if not found.
    """
    index = key % table.size
    start_index = index

    while table.data[index] is not None:
        if table.data[index] != TOMBSTONE and table.data[index][0] == key:
            return table.data[index][1]
        
        index = (index + 1) % table.size

        if index == start_index:
            break

    return None

