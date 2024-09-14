from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PingReq(_message.Message):
    __slots__ = ("PDHFGJIBCLA", "sc_data", "NHLLKPHMFGP", "total_tick_time", "client_time", "ue_time", "DFALBBBCFMO", "seq")
    PDHFGJIBCLA_FIELD_NUMBER: _ClassVar[int]
    SC_DATA_FIELD_NUMBER: _ClassVar[int]
    NHLLKPHMFGP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TICK_TIME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TIME_FIELD_NUMBER: _ClassVar[int]
    UE_TIME_FIELD_NUMBER: _ClassVar[int]
    DFALBBBCFMO_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    PDHFGJIBCLA: bytes
    sc_data: bytes
    NHLLKPHMFGP: int
    total_tick_time: float
    client_time: int
    ue_time: float
    DFALBBBCFMO: int
    seq: int
    def __init__(self, PDHFGJIBCLA: _Optional[bytes] = ..., sc_data: _Optional[bytes] = ..., NHLLKPHMFGP: _Optional[int] = ..., total_tick_time: _Optional[float] = ..., client_time: _Optional[int] = ..., ue_time: _Optional[float] = ..., DFALBBBCFMO: _Optional[int] = ..., seq: _Optional[int] = ...) -> None: ...
