# Live display demo 
import random
import time 

from rich.live import Live
from rich.table import Table

def generate_table() -> Table:
    """Make a new Table"""

    table = Table()
    table.add_column("Row_ID")
    table.add_column("Description")
    table.add_column("Level")
    
    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
    f"{row}", f"{value: 3f}", "[red]ERROR" if value < 50 else "[gree]SUCCESS"
        )
    return table 
#with Live(table, refresh_per_second=4):
with Live(generate_table(), refresh_per_second=4) as live:
    for row in range(12):
        time.sleep(0.4)
        live.update(generate_table())
        # table.add_row(f"{row}", f"description {row}", "[red]ERROR")

