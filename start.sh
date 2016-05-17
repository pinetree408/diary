#!/bin/bash

# Install virtualenv
if [ ! -d "venv" ]
then
    virtualenv venv
fi

# Activate virtualenv
. venv/bin/activate

# Install requirements
if [ -f "requirements.txt" ]
then
    pip install -r requirements.txt
else
    pip install django==1.8
fi

# Go to project folder
cd emotiondiary

# Migrate django sqlite DB
python manage.py migrate

# Settign django facebook auth
python manage.py shell < facebook.py

# Run django Web Server on local
python manage.py runserver
