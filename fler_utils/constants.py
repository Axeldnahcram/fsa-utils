# coding: utf-8
"""
.. module:: fler_utils.constants
Constants module for fler utilities
"""

__author__ = "Axel Marchand"

# Globals
###############################################################################

# Redis store
SET = "set"
GET = "get"
PKL_ROOT = "pkl_root"
CSV_ROOT = "csv_root"
TXT_ROOT = "txt_root"
JSON_ROOT = "json_root"
TRAININGDATASETS_ROOT = "trainingdatasets_root"
API_CONFIGURATION = "api_configuration"
REDIS_URL = "redis_url"
PG_DSN = "pg_dsn"

# MAILJET constants
MAILJET_API_MAIL = 'MAILJET_API_MAIL'
MAILJET_API_NAME = 'MAILJET_API_NAME'
MAILJET_API_KEY = 'MAILJET_API_KEY'
MAILJET_API_SECRET = 'MAILJET_API_SECRET'

# Sentry constants
SENTRY_LOG_ACTIVATED = False
SENTRY_DSN = "SENTRY_DSN"
SENTRY_ACTIVATED = 'SENTRY_ACTIVATED'