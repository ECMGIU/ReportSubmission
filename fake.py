from app import db, Report, Team

NUM_REPORTS = 40

db.session.add(
    Team(name='Domestic Equity', manager='pwgould', color='red'),
    Team(name='International Equity', manager='spsahoo', color='yellow'),
    Team(name='Sustainable Investing', manager='madamann', color='green'),
    Team(name='Commodities', manager='sahmehta', color='purple'),
    Team(name='Real Estate', manager='evanhunt', color='orange'),
    Team(name='Macro Research', manager='ypande', color='blue')
)

db.session.commit()

for x in range(NUM_REPORTS):
    db.session.add(Report(
        'args'
    ))
db.session.commit()
