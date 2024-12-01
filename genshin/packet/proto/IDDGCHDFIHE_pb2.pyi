from genshin.packet.proto import EJLNBCBFOGL_pb2 as _EJLNBCBFOGL_pb2
from genshin.packet.proto import OJNEPIECHHJ_pb2 as _OJNEPIECHHJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IDDGCHDFIHE(_message.Message):
    __slots__ = ("CNBKDMINMHD", "FCPANCMAOIE", "NDHKABFFJPK")
    CNBKDMINMHD_FIELD_NUMBER: _ClassVar[int]
    FCPANCMAOIE_FIELD_NUMBER: _ClassVar[int]
    NDHKABFFJPK_FIELD_NUMBER: _ClassVar[int]
    CNBKDMINMHD: _containers.RepeatedCompositeFieldContainer[_EJLNBCBFOGL_pb2.EJLNBCBFOGL]
    FCPANCMAOIE: int
    NDHKABFFJPK: _OJNEPIECHHJ_pb2.OJNEPIECHHJ
    def __init__(self, CNBKDMINMHD: _Optional[_Iterable[_Union[_EJLNBCBFOGL_pb2.EJLNBCBFOGL, _Mapping]]] = ..., FCPANCMAOIE: _Optional[int] = ..., NDHKABFFJPK: _Optional[_Union[_OJNEPIECHHJ_pb2.OJNEPIECHHJ, str]] = ...) -> None: ...
