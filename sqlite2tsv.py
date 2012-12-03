import sqlite3
import sys

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Usage: python sqlite2tsv.py db-name table-name"
		sys.exit(0)
	db_name = sys.argv[1]
	table_name = sys.argv[2]
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute('SELECT * FROM %s' % table_name)
	col_names = [x[0] for x in cur.description]
	print "\t".join(col_names)
	for row in cur.fetchall():
		vals = [str(x) for x in list(row)]
		print "\t".join(vals)
