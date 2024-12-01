from genshin.packet.proto import AMNJNFKHHGG_pb2 as _AMNJNFKHHGG_pb2
from genshin.packet.proto import LDFOEHIKKML_pb2 as _LDFOEHIKKML_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EKHMDFIDDOD(_message.Message):
    __slots__ = ("GFKMHAGGHLP", "BEMMOHCGONK", "guid")
    GFKMHAGGHLP_FIELD_NUMBER: _ClassVar[int]
    BEMMOHCGONK_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    GFKMHAGGHLP: _containers.RepeatedCompositeFieldContainer[_AMNJNFKHHGG_pb2.AMNJNFKHHGG]
    BEMMOHCGONK: _containers.RepeatedCompositeFieldContainer[_LDFOEHIKKML_pb2.LDFOEHIKKML]
    guid: int
    def __init__(self, GFKMHAGGHLP: _Optional[_Iterable[_Union[_AMNJNFKHHGG_pb2.AMNJNFKHHGG, _Mapping]]] = ..., BEMMOHCGONK: _Optional[_Iterable[_Union[_LDFOEHIKKML_pb2.LDFOEHIKKML, _Mapping]]] = ..., guid: _Optional[int] = ...) -> None: ...
