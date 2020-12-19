from app import Team, db

teams = [
    Team(name='Domestic Equity', manager='pwgould', color='red'),
    Team(name='International Equity', manager='spsahoo', color='yellow'),
    Team(name='Sustainable Investing', manager='madamann', color='green'),
    Team(name='Commodities', manager='sahmehta', color='purple'),
    Team(name='Real Estate', manager='evanhunt', color='pink'),
    Team(name='Macro Research', manager='ypande', color='blue')
]

db.session.add_all(teams)
db.session.commit()
