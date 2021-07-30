import os

CONNECTION_STRING = (
    f"postgresql://{os.environ['POSTGRES_USER']}"
    f":{os.environ['POSTGRES_PASSWORD']}"
    f"@{os.environ['DB_HOSTNAME']}:5432/{os.environ['APPLICATION_DB']}"
)
