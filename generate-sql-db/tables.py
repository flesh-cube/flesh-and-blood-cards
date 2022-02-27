import generate_table.edition
import generate_table.foiling
import generate_table.icon
import generate_table.keyword
import generate_table.rarity
import generate_table.type

def create_tables(conn = None):
    print("Creating tables...")
    cur = conn.cursor()

    generate_table.edition.create_table(cur)
    generate_table.foiling.create_table(cur)
    generate_table.icon.create_table(cur)
    generate_table.keyword.create_table(cur)
    generate_table.rarity.create_table(cur)
    generate_table.type.create_table(cur)

    cur.close()
    print("Finished creating tables")

def drop_tables(conn = None):
    print("Dropping tables...")
    cur = conn.cursor()

    generate_table.edition.drop_table(cur)
    generate_table.foiling.drop_table(cur)
    generate_table.icon.drop_table(cur)
    generate_table.keyword.drop_table(cur)
    generate_table.rarity.drop_table(cur)
    generate_table.type.drop_table(cur)

    cur.close()
    print("Finished dropping tables")

def generate_table_data(conn = None):
    print("Generating table data...")
    cur = conn.cursor()

    generate_table.edition.generate_table(cur)
    generate_table.foiling.generate_table(cur)
    generate_table.icon.generate_table(cur)
    generate_table.keyword.generate_table(cur)
    generate_table.rarity.generate_table(cur)
    generate_table.type.generate_table(cur)

    cur.close()
    print("Finished generating table data")