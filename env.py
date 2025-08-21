import os

os.environ["SECRET_KEY"] = 'DeHftg345$£$th7'

os.environ["DEVELOPMENT"] = 'True'
os.environ.setdefault("DATABASE_URL", "psql 'postgresql://neondb_owner:npg_OqbNY9DtUJ8m@ep-dawn-firefly-abwgzj1g-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'")