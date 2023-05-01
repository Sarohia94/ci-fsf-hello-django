# import os

# if os.path.isfile("env.py"):
#     import env

# os.environ.get("DATABASE_URL")

 from pathlib import Path
 import os
 import dj_database_url
 import env

 DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
 }