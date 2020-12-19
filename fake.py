from sqlfaker.database import Database

db = Database(db_name='app')

db.tables["app"].add_primary_key(column_name="student_id")
db.tables["app"].add_column(column_name="username", data_type="varchar(50)", data_target="name")
db.tables["app"].add_column(column_name="title", data_type="varchar(50)", data_target="name")
db.tables["app"].add_column(column_name="ticker", data_type="varchar(4)", data_target="file")
db.tables["app"].add_column(column_name="date", data_type="date", data_target="date")
db.tables["app"].add_column(column_name="team", data_type="varchar(30", data_target="job")

db.generate_data()
db.export_sql("app.sql")
