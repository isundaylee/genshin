from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JPGINAGIFAH(_message.Message):
    __slots__ = ("GJEBAJAJPII", "item_id", "JLGJBALEIOI", "FCPANCMAOIE")
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    JLGJBALEIOI_FIELD_NUMBER: _ClassVar[int]
    FCPANCMAOIE_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    item_id: int
    JLGJBALEIOI: int
    FCPANCMAOIE: int
    def __init__(self, GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., item_id: _Optional[int] = ..., JLGJBALEIOI: _Optional[int] = ..., FCPANCMAOIE: _Optional[int] = ...) -> None: ...
