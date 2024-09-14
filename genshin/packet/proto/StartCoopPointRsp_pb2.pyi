from genshin.packet.proto import MainCoop_pb2 as _MainCoop_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartCoopPointRsp(_message.Message):
    __slots__ = ("start_main_coop", "coop_point", "retcode", "is_start")
    START_MAIN_COOP_FIELD_NUMBER: _ClassVar[int]
    COOP_POINT_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    IS_START_FIELD_NUMBER: _ClassVar[int]
    start_main_coop: _MainCoop_pb2.MainCoop
    coop_point: int
    retcode: int
    is_start: bool
    def __init__(self, start_main_coop: _Optional[_Union[_MainCoop_pb2.MainCoop, _Mapping]] = ..., coop_point: _Optional[int] = ..., retcode: _Optional[int] = ..., is_start: bool = ...) -> None: ...
