# build.sh
echo "Starting build script"


pip install -r requirements.txt

# make migrations
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# collectstatic
python3 manage.py collectstatic --noinput  

echo "Build script completed"
