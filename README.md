# USERS REST API

# Requisites

- python
- mysql-server
- mysql-devel
- virtualenv (Optional)
- virtualenvwrapper (Optional)

# Create a Python Virtual Environment (optional)

```
mkvirtualenv sampleapp
```

#Configuration

- MYSQL parameters must be configured on the config.cfg file.
- Install the required packages:
```
pip install -r requirements.txt
```
- Once MYSQL is configured locally, run the following command line to create the neccesary tables:
```
python manage.py migrate
```

#Run the development server
```
python manage.py runserver
```