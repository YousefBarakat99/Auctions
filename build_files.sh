# Remove existing static files build directory
rm -rf staticfiles_build

# Run Django collectstatic command to generate static files
python manage.py collectstatic --noinput

# Move static files to the build directory
mkdir staticfiles_build
mv static/* staticfiles_build/

# Remove any remaining empty 'static' directory
rm -rf static