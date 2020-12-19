from app import db, Report, Team

NUM_REPORTS = 40

db.session.add(
    Team(name='Domestic Equity', manager='pwgould', color='Red'),
    Team(name='International Equity', manager='spsahoo', color='Yellow'),
    Team(name='Sustainable Investing', manager='madamann', color='Green'),
    Team(name='Commodities', manager='sahmehta', color='Purple'),
    Team(name='Real Estate', manager='evanhunt', color='Orange'),
    Team(name='Macro Research', manager='ypande', color='Blue')
)

db.session.commit()

for x in range(NUM_REPORTS):
    db.session.add(Report(
        'args'
    ))
db.session.commit()
