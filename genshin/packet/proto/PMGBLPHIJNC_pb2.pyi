from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import StoreType_pb2 as _StoreType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PMGBLPHIJNC(_message.Message):
    __slots__ = ("GJEBAJAJPII", "guid", "store_type", "OFIPBEGGHCD")
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OFIPBEGGHCD_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    guid: int
    store_type: _StoreType_pb2.StoreType
    OFIPBEGGHCD: int
    def __init__(self, GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., guid: _Optional[int] = ..., store_type: _Optional[_Union[_StoreType_pb2.StoreType, str]] = ..., OFIPBEGGHCD: _Optional[int] = ...) -> None: ...
