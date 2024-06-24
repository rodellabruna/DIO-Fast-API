import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy.engine import Connection
from alembic import context

# Certifique-se de que as importações são corretas
from workout_api.contrib.models import BaseModel
from workout_api.contrib.repository.models import *

# Configurar o logger
config = context.config
fileConfig(config.config_file_name)

# Adicione seus modelos aqui para 'target_metadata'
target_metadata = BaseModel.metadata

# Outra configuração...

def run_migrations_online():
    """
    Run migrations in 'online' mode.
    """
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async def do_run_migrations(connection: Connection):
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

    asyncio.run(do_run_migrations(connectable))

if context.is_offline_mode():
    raise Exception("Only online migrations are supported in this configuration")
else:
    run_migrations_online()
