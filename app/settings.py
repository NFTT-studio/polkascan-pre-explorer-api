#  Polkascan PRE Explorer API
#
#  Copyright 2018-2020 openAware BV (NL).
#  This file is part of Polkascan.
#
#  Polkascan is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Polkascan is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Polkascan. If not, see <http://www.gnu.org/licenses/>.
#
#  settings.py
import os

DB_NAME = os.environ.get("DB_NAME", "polkascan")
DB_HOST = os.environ.get("DB_HOST", "mysql")
DB_PORT = os.environ.get("DB_PORT", 3306)
DB_USERNAME = os.environ.get("DB_USERNAME", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "root")

DB_CONNECTION = os.environ.get("DB_CONNECTION", "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(
    DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
))

SUBSTRATE_RPC_URL = os.environ.get("SUBSTRATE_RPC_URL", "http://substrate-node:9933/")
SUBSTRATE_ADDRESS_TYPE = int(os.environ.get("SUBSTRATE_ADDRESS_TYPE", 42))
SUBSTRATE_TOKEN_DECIMALS = int(os.environ.get("SUBSTRATE_TOKEN_DECIMALS", 12))
SUBSTRATE_METADATA_VERSION = int(os.environ.get("SUBSTRATE_METADATA_VERSION", 8))

TYPE_REGISTRY = os.environ.get("TYPE_REGISTRY", "default")

DOGPILE_CACHE_SETTINGS = {

    'default_list_cache_expiration_time': 6,
    'default_detail_cache_expiration_time': 3600,
    'host': os.environ.get("DOGPILE_CACHE_HOST", "redis"),
    'port': os.environ.get("DOGPILE_CACHE_PORT", 6379),
    'db': os.environ.get("DOGPILE_CACHE_DB", 0),
    'password': os.environ.get("DOGPILE_CACHE_PASSWORD", '')
}


DEBUG = False

MAX_RESOURCE_PAGE_SIZE = 100
LOG_TYPE_AUTHORITIESCHANGE = 1

SEARCH_INDEX_SLASHED_ACCOUNT = 1
SEARCH_INDEX_BALANCETRANSFER = 2
SEARCH_INDEX_HEARTBEATRECEIVED = 3
SEARCH_INDEX_COUNCIL_PROPOSED = 4
SEARCH_INDEX_COUNCIL_VOTE = 5
SEARCH_INDEX_STAKING_BONDED = 6
SEARCH_INDEX_STAKING_UNBONDED = 7
SEARCH_INDEX_STAKING_WITHDRAWN = 8
SEARCH_INDEX_IMONLINE_SOMEOFFLINE = 9
SEARCH_INDEX_STAKING_NOMINATE = 10
SEARCH_INDEX_STAKING_VALIDATE = 11
SEARCH_INDEX_STAKING_CHILL = 12
SEARCH_INDEX_STAKING_SET_PAYEE = 19
SEARCH_INDEX_IDENTITY_SET = 13
SEARCH_INDEX_IDENTITY_SET_SUBS = 14
SEARCH_INDEX_IDENTITY_CLEARED = 15
SEARCH_INDEX_IDENTITY_KILLED = 16
SEARCH_INDEX_IDENTITY_JUDGEMENT_REQUESTED = 17
SEARCH_INDEX_IDENTITY_JUDGEMENT_GIVEN = 18
SEARCH_INDEX_IDENTITY_JUDGEMENT_UNREQUESTED = 20
SEARCH_INDEX_ACCOUNT_KILLED = 21
SEARCH_INDEX_ACCOUNT_CREATED = 22
SEARCH_INDEX_COUNCIL_MEMBER_ELECTED = 23
SEARCH_INDEX_COUNCIL_MEMBER_KICKED = 24
SEARCH_INDEX_COUNCIL_CANDIDACY_RENOUNCED = 25
SEARCH_INDEX_COUNCIL_CANDIDACY_SUBMIT = 26
SEARCH_INDEX_COUNCIL_CANDIDACY_VOTE = 27
SEARCH_INDEX_TREASURY_PROPOSED = 28
SEARCH_INDEX_TREASURY_AWARDED = 37
SEARCH_INDEX_DEMOCRACY_VOTE = 29
SEARCH_INDEX_DEMOCRACY_PROXY_VOTE = 30
SEARCH_INDEX_DEMOCRACY_PROPOSE = 31
SEARCH_INDEX_DEMOCRACY_SECOND = 32
SEARCH_INDEX_TECHCOMM_VOTED = 33
SEARCH_INDEX_TECHCOMM_PROPOSED = 34
SEARCH_INDEX_BALANCES_DEPOSIT = 35
SEARCH_INDEX_CLAIMS_CLAIMED = 36
SEARCH_INDEX_STAKING_SESSION = 38
SEARCH_INDEX_STAKING_REWARD = 39
SEARCH_INDEX_SIGNED_EXTRINSIC = 99

SUBSTRATE_STORAGE_BALANCE = os.environ.get("SUBSTRATE_STORAGE_BALANCE", "FreeBalance")
USE_NODE_RETRIEVE_BALANCES = os.environ.get("USE_NODE_RETRIEVE_BALANCES", "False")

try:
    from app.local_settings import *
except ImportError:
    pass
