from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class McoinExchangeHcoinReq(_message.Message):
    __slots__ = ("hcoin", "mcoin_cost")
    HCOIN_FIELD_NUMBER: _ClassVar[int]
    MCOIN_COST_FIELD_NUMBER: _ClassVar[int]
    hcoin: int
    mcoin_cost: int
    def __init__(self, hcoin: _Optional[int] = ..., mcoin_cost: _Optional[int] = ...) -> None: ...
