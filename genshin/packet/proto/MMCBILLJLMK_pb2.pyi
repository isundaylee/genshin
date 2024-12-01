from genshin.packet.proto import HKPGNGDDOCL_pb2 as _HKPGNGDDOCL_pb2
from genshin.packet.proto import LJCNGNGDGPH_pb2 as _LJCNGNGDGPH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MMCBILLJLMK(_message.Message):
    __slots__ = ("BIKKDDDLDHP", "JPIECJLIGIP", "PONKPLPMFEI")
    class BIKKDDDLDHPEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BIKKDDDLDHP_FIELD_NUMBER: _ClassVar[int]
    JPIECJLIGIP_FIELD_NUMBER: _ClassVar[int]
    PONKPLPMFEI_FIELD_NUMBER: _ClassVar[int]
    BIKKDDDLDHP: _containers.ScalarMap[int, int]
    JPIECJLIGIP: _HKPGNGDDOCL_pb2.HKPGNGDDOCL
    PONKPLPMFEI: _LJCNGNGDGPH_pb2.LJCNGNGDGPH
    def __init__(self, BIKKDDDLDHP: _Optional[_Mapping[int, int]] = ..., JPIECJLIGIP: _Optional[_Union[_HKPGNGDDOCL_pb2.HKPGNGDDOCL, _Mapping]] = ..., PONKPLPMFEI: _Optional[_Union[_LJCNGNGDGPH_pb2.LJCNGNGDGPH, str]] = ...) -> None: ...
