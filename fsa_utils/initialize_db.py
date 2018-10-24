#!/usr/bin/env python
# coding: utf-8

"""
.. module:: populate_db.py
Initialize the database with the base data
"""

# standard
import logging
import asyncio
import argparse
# installed
import sqlalchemy as sa
from aiopg.sa import create_engine
import pandas as pd
from logzero import logger as LOGGER
import fsa_sql.commons as commons



async def initialize_db(query:str=""):
    """
    .. function:: initialize_db
    Chain the differents procedure feeding the database
    """
    LOGGER.info("Reading reset schema DDL")
    LOGGER.info("Recreating tables on database")
    async with create_engine(dsn=commons.DSN_VAL) as engine:
        async with engine.acquire() as conn:
            await conn.execute(query)
    LOGGER.info(query)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(initialize_db("CREATE TABLE portfolios_values (ptv_id BIGSERIAL PRIMARY KEY);"))

