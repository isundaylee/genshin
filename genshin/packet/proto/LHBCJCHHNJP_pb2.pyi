from genshin.packet.proto import BPOBBMNGMDL_pb2 as _BPOBBMNGMDL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LHBCJCHHNJP(_message.Message):
    __slots__ = ("BMNFBPGHFJB", "PHJJLGFFMOM", "type")
    class BMNFBPGHFJBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class PHJJLGFFMOMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BMNFBPGHFJB_FIELD_NUMBER: _ClassVar[int]
    PHJJLGFFMOM_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BMNFBPGHFJB: _containers.ScalarMap[int, int]
    PHJJLGFFMOM: _containers.ScalarMap[int, int]
    type: _BPOBBMNGMDL_pb2.BPOBBMNGMDL
    def __init__(self, BMNFBPGHFJB: _Optional[_Mapping[int, int]] = ..., PHJJLGFFMOM: _Optional[_Mapping[int, int]] = ..., type: _Optional[_Union[_BPOBBMNGMDL_pb2.BPOBBMNGMDL, str]] = ...) -> None: ...
