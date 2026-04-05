# Migration Map — Bitcoin → Zcash RPC

This file maps every Bitcoin RPC call found in the source code to its Zcash equivalent.
Use `zcash_rpc.*` (in zcash-enhancements/) as a drop-in replacement.

## RPC Call Mapping

| File | Line | Bitcoin Call | Zcash Equivalent | Shielded? | Notes |
|------|------|-------------|------------------|-----------|-------|
| `examples/bip-0070-payment-protocol.py` | 38 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `examples/make-bootstrap-rpc.py` | 43 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `examples/publish-text.py` | 167 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `examples/publish-text.py` | 213 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `examples/spend-p2wpkh.py` | 29 | `getblockchaininfo` | `getblockchaininfo` | No | Same RPC — works identically on Zcash. |
| `examples/spend-p2wpkh.py` | 29 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `examples/spend-p2wpkh.py` | 43 | `listunspent` | `z_listunspent` | Yes | Lists shielded notes. Different schema from transparent listunspent. |
| `examples/spend-p2wpkh.py` | 44 | `importprivkey` | `z_importkey` | Yes | Imports shielded spending key. Triggers rescan. |
| `examples/spend-p2wpkh.py` | 47 | `listunspent` | `z_listunspent` | Yes | Lists shielded notes. Different schema from transparent listunspent. |
| `examples/spend-p2wpkh.py` | 65 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `examples/spend-p2wpkh.py` | 100 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `examples/ssl-rpc-connection.py` | 37 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `examples/timestamp-op-ret.py` | 44 | `listunspent` | `z_listunspent` | Yes | Lists shielded notes. Different schema from transparent listunspent. |
| `examples/timestamp-op-ret.py` | 49 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `examples/timestamp-op-ret.py` | 50 | `validateaddress` | `z_validateaddress` | Yes | Validates z-addresses (zs... prefix). |
| `examples/timestamp-op-ret.py` | 71 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `zcash/messages.py` | 288 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/messages.py` | 289 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/messages.py` | 292 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/messages.py` | 308 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/messages.py` | 494 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/messages.py` | 520 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 385 | `dumpprivkey` | `z_exportkey` | Yes | Exports shielded spending key for z-address. |
| `zcash/rpc.py` | 388 | `dumpprivkey` | `z_exportkey` | Yes | Exports shielded spending key for z-address. |
| `zcash/rpc.py` | 446 | `getbalance` | `z_gettotalbalance` | Yes | Returns {transparent, private, total}. Use 'private' for shielded balance. |
| `zcash/rpc.py` | 458 | `getbalance` | `z_gettotalbalance` | Yes | Returns {transparent, private, total}. Use 'private' for shielded balance. |
| `zcash/rpc.py` | 465 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 469 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 477 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 480 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 482 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 498 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 506 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 512 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 514 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 518 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 520 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 522 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 528 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 530 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/rpc.py` | 546 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/rpc.py` | 554 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/rpc.py` | 556 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/rpc.py` | 578 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `zcash/rpc.py` | 594 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `zcash/rpc.py` | 596 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `zcash/rpc.py` | 598 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `zcash/rpc.py` | 640 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `zcash/rpc.py` | 670 | `listunspent` | `z_listunspent` | Yes | Lists shielded notes. Different schema from transparent listunspent. |
| `zcash/rpc.py` | 679 | `listunspent` | `z_listunspent` | Yes | Lists shielded notes. Different schema from transparent listunspent. |
| `zcash/rpc.py` | 682 | `listunspent` | `z_listunspent` | Yes | Lists shielded notes. Different schema from transparent listunspent. |
| `zcash/rpc.py` | 708 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `zcash/rpc.py` | 716 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `zcash/rpc.py` | 718 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `zcash/rpc.py` | 731 | `sendtoaddress` | `z_sendmany` | Yes | Async operation — returns opid. Supports multiple recipients + memos. |
| `zcash/rpc.py` | 735 | `sendtoaddress` | `z_sendmany` | Yes | Async operation — returns opid. Supports multiple recipients + memos. |
| `zcash/rpc.py` | 773 | `validateaddress` | `z_validateaddress` | Yes | Validates z-addresses (zs... prefix). |
| `zcash/rpc.py` | 775 | `validateaddress` | `z_validateaddress` | Yes | Validates z-addresses (zs... prefix). |
| `zcash/tests/fakezcashproxy.py` | 136 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 138 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 139 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 140 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 147 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 148 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 150 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 152 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 171 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/fakezcashproxy.py` | 177 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/fakezcashproxy.py` | 189 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/fakezcashproxy.py` | 200 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/fakezcashproxy.py` | 209 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `zcash/tests/fakezcashproxy.py` | 220 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 225 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 227 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/fakezcashproxy.py` | 283 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `zcash/tests/fakezcashproxy.py` | 293 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `zcash/tests/test_fakezcashproxy.py` | 65 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 75 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 93 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 96 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 104 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 108 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 118 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 124 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 133 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 137 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 149 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 152 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 155 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 158 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 168 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 171 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `zcash/tests/test_fakezcashproxy.py` | 190 | `getrawtransaction` | `getrawtransaction` | No | Same RPC — but shielded outputs are encrypted. |
| `zcash/tests/test_fakezcashproxy.py` | 199 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/test_fakezcashproxy.py` | 206 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/test_fakezcashproxy.py` | 211 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/test_fakezcashproxy.py` | 213 | `getnewaddress` | `z_getnewaddress` | Yes | Pass 'sapling' for shielded address. Returns zs... prefix. |
| `zcash/tests/test_fakezcashproxy.py` | 283 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `zcash/tests/test_fakezcashproxy.py` | 289 | `sendrawtransaction` | `sendrawtransaction` | No | Same RPC — for transparent transactions. |
| `zcash/tests/test_fakezcashproxy.py` | 307 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 312 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 314 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 322 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 330 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 339 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 353 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 371 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_fakezcashproxy.py` | 376 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_messages.py` | 15 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_messages.py` | 61 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_messages.py` | 63 | `getblock` | `getblock` | No | Same RPC — works identically. |
| `zcash/tests/test_rpc.py` | 27 | `validateaddress` | `z_validateaddress` | Yes | Validates z-addresses (zs... prefix). |
| `zcash/tests/test_rpc.py` | 34 | `validateaddress` | `z_validateaddress` | Yes | Validates z-addresses (zs... prefix). |

## Quick Replace Guide

### `getnewaddress` → `z_getnewaddress`

**Pass 'sapling' for shielded address. Returns zs... prefix.**

```python
# Before (Bitcoin):
result = rpc.call("getnewaddress", [...])

# After (Zcash shielded):
from zcash_rpc import ZcashRPC
zrpc = ZcashRPC(port=18232)
result = zrpc.z_getnewaddress(...)
```

### `listunspent` → `z_listunspent`

**Lists shielded notes. Different schema from transparent listunspent.**

```python
# Before (Bitcoin):
result = rpc.call("listunspent", [...])

# After (Zcash shielded):
from zcash_rpc import ZcashRPC
zrpc = ZcashRPC(port=18232)
result = zrpc.z_listunspent(...)
```

### `importprivkey` → `z_importkey`

**Imports shielded spending key. Triggers rescan.**

```python
# Before (Bitcoin):
result = rpc.call("importprivkey", [...])

# After (Zcash shielded):
from zcash_rpc import ZcashRPC
zrpc = ZcashRPC(port=18232)
result = zrpc.z_importkey(...)
```

### `validateaddress` → `z_validateaddress`

**Validates z-addresses (zs... prefix).**

```python
# Before (Bitcoin):
result = rpc.call("validateaddress", [...])

# After (Zcash shielded):
from zcash_rpc import ZcashRPC
zrpc = ZcashRPC(port=18232)
result = zrpc.z_validateaddress(...)
```

### `dumpprivkey` → `z_exportkey`

**Exports shielded spending key for z-address.**

```python
# Before (Bitcoin):
result = rpc.call("dumpprivkey", [...])

# After (Zcash shielded):
from zcash_rpc import ZcashRPC
zrpc = ZcashRPC(port=18232)
result = zrpc.z_exportkey(...)
```

### `getbalance` → `z_gettotalbalance`

**Returns {transparent, private, total}. Use 'private' for shielded balance.**

```python
# Before (Bitcoin):
result = rpc.call("getbalance", [...])

# After (Zcash shielded):
from zcash_rpc import ZcashRPC
zrpc = ZcashRPC(port=18232)
result = zrpc.z_gettotalbalance(...)
```

### `sendtoaddress` → `z_sendmany`

**Async operation — returns opid. Supports multiple recipients + memos.**

```python
# Before (Bitcoin):
result = rpc.call("sendtoaddress", [...])

# After (Zcash shielded):
from zcash_rpc import ZcashRPC
zrpc = ZcashRPC(port=18232)
opid = zrpc.z_sendmany(from_addr, [{"address": to_zaddr, "amount": 1.0}])
result = zrpc.wait_for_operation(opid)  # Blocks until confirmed
```
