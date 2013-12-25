import os

APP_DICRECOTRY = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(APP_DICRECOTRY, 'static'),
    os.path.join(APP_DICRECOTRY, 'media'),
    '/Users/jorgesilva/Sites/2013/BusTracker/static',
    '/var/www/static/',
)
