from genshin.packet.proto import CKPIJBMMBGJ_pb2 as _CKPIJBMMBGJ_pb2
from genshin.packet.proto import LEGKIBHIHFA_pb2 as _LEGKIBHIHFA_pb2
from genshin.packet.proto import NGDKIEINDNN_pb2 as _NGDKIEINDNN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MDMMHLCDBJL(_message.Message):
    __slots__ = ("EPHDIIJJGNE", "OAGANLFHMBK", "GGJALEEPEDP", "MEKEFMAJEMF", "BMFAADBOCFN")
    EPHDIIJJGNE_FIELD_NUMBER: _ClassVar[int]
    OAGANLFHMBK_FIELD_NUMBER: _ClassVar[int]
    GGJALEEPEDP_FIELD_NUMBER: _ClassVar[int]
    MEKEFMAJEMF_FIELD_NUMBER: _ClassVar[int]
    BMFAADBOCFN_FIELD_NUMBER: _ClassVar[int]
    EPHDIIJJGNE: _CKPIJBMMBGJ_pb2.CKPIJBMMBGJ
    OAGANLFHMBK: _LEGKIBHIHFA_pb2.LEGKIBHIHFA
    GGJALEEPEDP: _containers.RepeatedScalarFieldContainer[int]
    MEKEFMAJEMF: _NGDKIEINDNN_pb2.NGDKIEINDNN
    BMFAADBOCFN: bool
    def __init__(self, EPHDIIJJGNE: _Optional[_Union[_CKPIJBMMBGJ_pb2.CKPIJBMMBGJ, _Mapping]] = ..., OAGANLFHMBK: _Optional[_Union[_LEGKIBHIHFA_pb2.LEGKIBHIHFA, _Mapping]] = ..., GGJALEEPEDP: _Optional[_Iterable[int]] = ..., MEKEFMAJEMF: _Optional[_Union[_NGDKIEINDNN_pb2.NGDKIEINDNN, _Mapping]] = ..., BMFAADBOCFN: bool = ...) -> None: ...
