# build.sh
echo "Starting build script"

pip install -r requirements.txt

python manage.py makemigrations --noinput
python manage.py migrate --noinput

python manage.py test
python manage.py runserver
python manage.py createsuperuser --noinput --username admin --email
python manage.py collectstatic --noinput
