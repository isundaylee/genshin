from genshin.packet.proto import JAHGJBJDHGG_pb2 as _JAHGJBJDHGG_pb2
from genshin.packet.proto import NFAGPIAIKGN_pb2 as _NFAGPIAIKGN_pb2
from genshin.packet.proto import BFLCGFAMILE_pb2 as _BFLCGFAMILE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GFPEMFIMOPO(_message.Message):
    __slots__ = ("NONGOFFOAOI", "KDAAAFMOJDF", "FLHFLNIOEOL", "OEENIKOABOD", "CGPJLKKDILM")
    NONGOFFOAOI_FIELD_NUMBER: _ClassVar[int]
    KDAAAFMOJDF_FIELD_NUMBER: _ClassVar[int]
    FLHFLNIOEOL_FIELD_NUMBER: _ClassVar[int]
    OEENIKOABOD_FIELD_NUMBER: _ClassVar[int]
    CGPJLKKDILM_FIELD_NUMBER: _ClassVar[int]
    NONGOFFOAOI: _JAHGJBJDHGG_pb2.JAHGJBJDHGG
    KDAAAFMOJDF: _NFAGPIAIKGN_pb2.NFAGPIAIKGN
    FLHFLNIOEOL: _containers.RepeatedCompositeFieldContainer[_BFLCGFAMILE_pb2.BFLCGFAMILE]
    OEENIKOABOD: int
    CGPJLKKDILM: int
    def __init__(self, NONGOFFOAOI: _Optional[_Union[_JAHGJBJDHGG_pb2.JAHGJBJDHGG, _Mapping]] = ..., KDAAAFMOJDF: _Optional[_Union[_NFAGPIAIKGN_pb2.NFAGPIAIKGN, _Mapping]] = ..., FLHFLNIOEOL: _Optional[_Iterable[_Union[_BFLCGFAMILE_pb2.BFLCGFAMILE, _Mapping]]] = ..., OEENIKOABOD: _Optional[int] = ..., CGPJLKKDILM: _Optional[int] = ...) -> None: ...
