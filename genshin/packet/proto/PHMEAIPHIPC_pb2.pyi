from genshin.packet.proto import HDNFCEMGFOJ_pb2 as _HDNFCEMGFOJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PHMEAIPHIPC(_message.Message):
    __slots__ = ("GLJHMDNLJEH",)
    class GLJHMDNLJEHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _HDNFCEMGFOJ_pb2.HDNFCEMGFOJ
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_HDNFCEMGFOJ_pb2.HDNFCEMGFOJ, _Mapping]] = ...) -> None: ...
    GLJHMDNLJEH_FIELD_NUMBER: _ClassVar[int]
    GLJHMDNLJEH: _containers.MessageMap[int, _HDNFCEMGFOJ_pb2.HDNFCEMGFOJ]
    def __init__(self, GLJHMDNLJEH: _Optional[_Mapping[int, _HDNFCEMGFOJ_pb2.HDNFCEMGFOJ]] = ...) -> None: ...
