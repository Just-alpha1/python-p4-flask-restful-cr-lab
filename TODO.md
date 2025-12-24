# TODO for Flask Plant Store API

- [ ] Edit server/models.py: Add name (string), image (string), price (decimal) columns to Plant model
- [ ] Run flask db revision --autogenerate -m'add columns to table'
- [ ] Run flask db upgrade head
- [ ] Run python seed.py
- [ ] Edit server/app.py: Implement GET /plants (index), GET /plants/:id (show), POST /plants (create) routes
- [ ] Run tests to verify implementation
- [ ] Start Flask and React apps to test frontend integration
