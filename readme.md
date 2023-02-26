### Project3 Python Backend for Actworks

##### Links
- GitHub: https://github.com/SWIRTH9092/artwork_backend
- Render: https://sw-artworks-bkend.onrender.com/

##### Dependencies  

asgiref==3.6.0
dj-database-url==1.2.0
Django==4.1.7
django-cors-headers==3.14.0
djangorestframework==3.14.0
gunicorn==20.1.0
psycopg2-binary==2.9.5
pytz==2022.7.1
sqlparse==0.4.3
- Postgres

##### Activity Tracker Tables
-   Postgres database name:  
    - project4
-   table name:
    - artworks_artwork
- Model (schema):
    - id (key)
    - subject
    - category
    - comments
    - image url

#### Routes 

| Table |Routes | Method | EndPoints | Expected Result |
|------|-------|--------|-----------|-----------------|
| artworks_artwork | Index | GET | /artworks | Gets all entries |
| artworks_artwork | Create | POST | /activity/ | Creates a new entry |
| artworks_artwork| Show | GET | /activity/:id | Gets 1 entry
| artworks_artwork | Update | PUT | /activity/:id/ | Updates Existing Entry |
| artworks_artwork | Delete | DELETE | /activity/:id/ | Removes entry |
