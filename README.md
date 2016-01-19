EmotionDiary
==================
An application for evaluating emotions on Facebook.

## How to Work on this Project (on a mac)

### Setting up your system
```sh
git clone https://github.com/pinetree408/emotiondiary.git

cd emotiondiary

//pip install virtualenv

virtualenv venv

. venv/bin/activate 

pip install -r requirements.txt

cd emotiondiary

python manage.py migrate

python manage.py createsuperuser
```
###Add Site facebook.com at admin page & Add facebook application at Social applications page
```
python manage.py shell < facebook.py
```

### Running on local
```
python manage.py runserver
```

#License
all directories and their contents are Copyright Lee Sang-Yoon.

You may not reuse anything therein without my permission.
