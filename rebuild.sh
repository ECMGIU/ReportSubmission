rm app.db
rm -rf migrations/

flask db init
flask db migrate
flask db upgrade

git add .
git commit -m 'rebuild migrations'
git push origin main

git push heroku main
heroku logs --tail