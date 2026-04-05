# Copyright (C) The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.


import zcash.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.12.2'

class MainParams(zcash.core.CoreMainParams):
    MESSAGE_START = b'\xf9\xbe\xb4\xd9'
    DEFAULT_PORT = 8233
    RPC_PORT = 8232
    DNS_SEEDS = (('mainnet.z.cash', 'dnsseed.z.cash'),
                 ('zfnd.org', 'dnsseed.zfnd.org'),
                 ('dashjr.org', 'dnsseed.str4d.xyz'),
                 ('z.cash', 'dnsseed2.z.cash'),
                 ('petertodd.org', 'seed.btc.petertodd.net'),
                 ('xf2.org', 'bitseed.xf2.org'),
                 ('z.cash', 'dnsseed3.z.cash'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':0,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :128}
    BECH32_HRP = 'bc'

class TestNetParams(zcash.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07'
    DEFAULT_PORT = 18233
    RPC_PORT = 18232
    DNS_SEEDS = (('testnetz.cash', 'testnet-dnsseed3.z.cash'),
                 ('petertodd.org', 'seed.tbtc.petertodd.net'),
                 ('zfnd.org', 'testnet-seed.zfnd.org'),
                 ('testnet.zfnd.org', 'dnsseed.testnet.zfnd.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'tb'

class SigNetParams(zcash.core.CoreSigNetParams):
    MESSAGE_START = b'\x0a\x03\xcf\x40'
    DEFAULT_PORT = 38333
    RPC_PORT = 38332
    DNS_SEEDS = (("testnet.z.cash", "seed.testnet.z.cash"))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

    BECH32_HRP = 'tb'

class RegTestParams(zcash.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18344
    RPC_PORT = 18232
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'bcrt'

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
zcash.core.params correctly too.
"""
#params = zcash.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    zcash.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = zcash.core.coreparams = MainParams()
    elif name == 'testnet':
        params = zcash.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = zcash.core.coreparams = RegTestParams()
    elif name == 'signet':
        params = zcash.core.coreparams = SigNetParams()
    else:
        raise ValueError('Unknown chain %r' % name)
