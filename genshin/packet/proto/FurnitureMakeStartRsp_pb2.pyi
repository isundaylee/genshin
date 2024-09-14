from genshin.packet.proto import FurnitureMakeSlot_pb2 as _FurnitureMakeSlot_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FurnitureMakeStartRsp(_message.Message):
    __slots__ = ("retcode", "furniture_make_slot")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_MAKE_SLOT_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    furniture_make_slot: _FurnitureMakeSlot_pb2.FurnitureMakeSlot
    def __init__(self, retcode: _Optional[int] = ..., furniture_make_slot: _Optional[_Union[_FurnitureMakeSlot_pb2.FurnitureMakeSlot, _Mapping]] = ...) -> None: ...
