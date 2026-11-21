# build.sh
echo "Starting build script"


# make migrations
python3 manage.py makemigrations
python3 manage.py migrate

# collectstatic
python3 manage.py collectstatic --noinput  

echo "Build script completed"
