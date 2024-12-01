from genshin.packet.proto import GFFIOKDNCLP_pb2 as _GFFIOKDNCLP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GFAGPBKLLMF(_message.Message):
    __slots__ = ("DLCDFKIOBCL", "ACPHEGPGPOH", "GJDPCOOMAJK", "FELNDGJJJIF", "IGBDOEBPPHO")
    DLCDFKIOBCL_FIELD_NUMBER: _ClassVar[int]
    ACPHEGPGPOH_FIELD_NUMBER: _ClassVar[int]
    GJDPCOOMAJK_FIELD_NUMBER: _ClassVar[int]
    FELNDGJJJIF_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    DLCDFKIOBCL: _containers.RepeatedScalarFieldContainer[int]
    ACPHEGPGPOH: _containers.RepeatedScalarFieldContainer[int]
    GJDPCOOMAJK: _containers.RepeatedCompositeFieldContainer[_GFFIOKDNCLP_pb2.GFFIOKDNCLP]
    FELNDGJJJIF: _containers.RepeatedScalarFieldContainer[int]
    IGBDOEBPPHO: int
    def __init__(self, DLCDFKIOBCL: _Optional[_Iterable[int]] = ..., ACPHEGPGPOH: _Optional[_Iterable[int]] = ..., GJDPCOOMAJK: _Optional[_Iterable[_Union[_GFFIOKDNCLP_pb2.GFFIOKDNCLP, _Mapping]]] = ..., FELNDGJJJIF: _Optional[_Iterable[int]] = ..., IGBDOEBPPHO: _Optional[int] = ...) -> None: ...
