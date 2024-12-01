from genshin.packet.proto import JGHGPMMAMBL_pb2 as _JGHGPMMAMBL_pb2
from genshin.packet.proto import AHPPBJIAKAI_pb2 as _AHPPBJIAKAI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HOFLBHDIPII(_message.Message):
    __slots__ = ("IKKMDALLEED", "ENGANDFGAPN", "GJHADCDABGH", "OJOCDKLPEPE", "JKNGLHEMPHB", "IGCHPOHFLMK", "IJPJICFKDJL")
    IKKMDALLEED_FIELD_NUMBER: _ClassVar[int]
    ENGANDFGAPN_FIELD_NUMBER: _ClassVar[int]
    GJHADCDABGH_FIELD_NUMBER: _ClassVar[int]
    OJOCDKLPEPE_FIELD_NUMBER: _ClassVar[int]
    JKNGLHEMPHB_FIELD_NUMBER: _ClassVar[int]
    IGCHPOHFLMK_FIELD_NUMBER: _ClassVar[int]
    IJPJICFKDJL_FIELD_NUMBER: _ClassVar[int]
    IKKMDALLEED: _containers.RepeatedScalarFieldContainer[int]
    ENGANDFGAPN: _containers.RepeatedScalarFieldContainer[int]
    GJHADCDABGH: _containers.RepeatedScalarFieldContainer[int]
    OJOCDKLPEPE: _containers.RepeatedScalarFieldContainer[int]
    JKNGLHEMPHB: _containers.RepeatedScalarFieldContainer[int]
    IGCHPOHFLMK: _containers.RepeatedCompositeFieldContainer[_JGHGPMMAMBL_pb2.JGHGPMMAMBL]
    IJPJICFKDJL: _AHPPBJIAKAI_pb2.AHPPBJIAKAI
    def __init__(self, IKKMDALLEED: _Optional[_Iterable[int]] = ..., ENGANDFGAPN: _Optional[_Iterable[int]] = ..., GJHADCDABGH: _Optional[_Iterable[int]] = ..., OJOCDKLPEPE: _Optional[_Iterable[int]] = ..., JKNGLHEMPHB: _Optional[_Iterable[int]] = ..., IGCHPOHFLMK: _Optional[_Iterable[_Union[_JGHGPMMAMBL_pb2.JGHGPMMAMBL, _Mapping]]] = ..., IJPJICFKDJL: _Optional[_Union[_AHPPBJIAKAI_pb2.AHPPBJIAKAI, _Mapping]] = ...) -> None: ...
