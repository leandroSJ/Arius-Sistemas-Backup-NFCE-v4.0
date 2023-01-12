from typing import Union, Any, Optional, IO

Buffer = Union[bytes, bytearray, memoryview]

import sys

def b(s: str) -> bytes: ...
def bchr(s: int) -> bytes: ...
def bord(s: bytes) -> int: ...
def tobytes(s: Union[bytes, str]) -> bytes: ...
def tostr(b: bytes) -> str: ...
def bytestring(x: Any) -> bool: ...

def is_native_int(s: Any) -> bool: ...
def is_string(x: Any) -> bool: ...
def is_bytes(x: Any) -> bool: ...

def BytesIO(b: bytes) -> IO[bytes]: ...
def StringIO(s: str) -> IO[str]: ...

if sys.version_info[0] == 2:
    from sys import maxint
    iter_range = xrange

else:
    from sys import maxsize as maxint
    iter_range = range

class FileNotFoundError:
    def __init__(self, err: int, msg: str, filename: str) -> None:
        pass

def _copy_bytes(start: Optional[int], end: Optional[int], seq: Buffer) -> bytes: ...
