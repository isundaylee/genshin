from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MMKACCNOLJO(_message.Message):
    __slots__ = ("equip_guid_list", "MEJLFKPFPGK")
    EQUIP_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    equip_guid_list: _containers.RepeatedScalarFieldContainer[int]
    MEJLFKPFPGK: int
    def __init__(self, equip_guid_list: _Optional[_Iterable[int]] = ..., MEJLFKPFPGK: _Optional[int] = ...) -> None: ...
