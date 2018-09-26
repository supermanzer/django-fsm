#--------------------------------------------------
# Defining a simple set of terminal commands
# to be run when the web container starts up
#--------------------------------------------------

# Check for any changes to our models
eval "./manage.py makemigrations"
# Apply any DB migrations we just made
eval "./manage.py migrate"
# Spin up the development server
eval "./manage.py runserver"
