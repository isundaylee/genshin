from genshin.packet.proto import AAENLNIBFOP_pb2 as _AAENLNIBFOP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NNFDIHPAGHC(_message.Message):
    __slots__ = ("HBJHPFFJNNB", "BDCBLNLCAGE", "GLKNGDDNOCN", "IEJPGHNLIDB", "EAIPGEMKNPO")
    class HBJHPFFJNNBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AAENLNIBFOP_pb2.AAENLNIBFOP
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AAENLNIBFOP_pb2.AAENLNIBFOP, _Mapping]] = ...) -> None: ...
    HBJHPFFJNNB_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    IEJPGHNLIDB_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    HBJHPFFJNNB: _containers.MessageMap[int, _AAENLNIBFOP_pb2.AAENLNIBFOP]
    BDCBLNLCAGE: bool
    GLKNGDDNOCN: bool
    IEJPGHNLIDB: int
    EAIPGEMKNPO: int
    def __init__(self, HBJHPFFJNNB: _Optional[_Mapping[int, _AAENLNIBFOP_pb2.AAENLNIBFOP]] = ..., BDCBLNLCAGE: bool = ..., GLKNGDDNOCN: bool = ..., IEJPGHNLIDB: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
