"""module contains database variables"""

#!/usr/bin/env python3

PG_USER = "postgres"
PG_PASSWORD = "data123"
PG_HOSTNAME = "127.0.0.1"
PG_PORT = "5432"
PG_DB_NAME = "dailypricedata"

connect = f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOSTNAME}:{PG_PORT}/{PG_DB_NAME}"
