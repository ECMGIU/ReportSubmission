from app import db, Report, Team

NUM_REPORTS = 40

db.session.add(
    Team(name='', manager='', color='')
)

db.session.commit()

for x in range(NUM_REPORTS):
    db.session.add(Report(
        'args'
    ))
db.session.commit()
