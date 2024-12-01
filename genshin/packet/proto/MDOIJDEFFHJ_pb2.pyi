from genshin.packet.proto import EDAPKOEFNDA_pb2 as _EDAPKOEFNDA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MDOIJDEFFHJ(_message.Message):
    __slots__ = ("equip_guid_list", "MEJLFKPFPGK", "FNBMMFBMKDO")
    EQUIP_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    FNBMMFBMKDO_FIELD_NUMBER: _ClassVar[int]
    equip_guid_list: _containers.RepeatedScalarFieldContainer[int]
    MEJLFKPFPGK: int
    FNBMMFBMKDO: _EDAPKOEFNDA_pb2.EDAPKOEFNDA
    def __init__(self, equip_guid_list: _Optional[_Iterable[int]] = ..., MEJLFKPFPGK: _Optional[int] = ..., FNBMMFBMKDO: _Optional[_Union[_EDAPKOEFNDA_pb2.EDAPKOEFNDA, str]] = ...) -> None: ...
