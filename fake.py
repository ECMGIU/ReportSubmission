import random

from app import db, Report, Team
from faker import Faker

NUM_REPORTS = 40

fake = Faker()

db.session.add(
    Team(name='', manager='', color='')
)

db.session.commit()

for x in range(NUM_REPORTS):
    db.session.add(Report(
        username=fake.pystr(8, 8).lower(),
        title=fake.sentence(7),
        ticker=fake.pystr(4, 4).upper(),
        date=fake.date_this_month(),
        team=random.choice(db.session.query(Team))
    ))
db.session.commit()
