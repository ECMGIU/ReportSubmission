import random

from faker import Faker

from app import db, Report, Team

NUM_REPORTS = 40

fake = Faker()

teams = [
    Team(name='Domestic Equity', manager='pwgould', color='red'),
    Team(name='International Equity', manager='spsahoo', color='yellow'),
    Team(name='Sustainable Investing', manager='madamann', color='green'),
    Team(name='Commodities', manager='sahmehta', color='purple'),
    Team(name='Real Estate', manager='evanhunt', color='orange'),
    Team(name='Macro Research', manager='ypande', color='blue')
]

db.session.add_all(teams)
db.session.commit()

reports = [
    Report(
        username=fake.pystr(8, 8).lower(),
        title=fake.sentence(7),
        ticker=fake.pystr(4, 4).upper(),
        date=fake.date_this_month(),
        team=db.session.query(Team)[random.randrange(0, db.session.query(Team).count()) ]
    )
    for x in range(NUM_REPORTS)
]

db.session.add_all(reports)
db.session.commit()
