from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NNLFBHCELOG(_message.Message):
    __slots__ = ("MKEFPAAIHKP", "CBOHPEMFMPL", "JHNFDBBBMJC", "JCOINGDOBMD", "HKPDFIIEHPA", "CLJLDMKNEGD")
    MKEFPAAIHKP_FIELD_NUMBER: _ClassVar[int]
    CBOHPEMFMPL_FIELD_NUMBER: _ClassVar[int]
    JHNFDBBBMJC_FIELD_NUMBER: _ClassVar[int]
    JCOINGDOBMD_FIELD_NUMBER: _ClassVar[int]
    HKPDFIIEHPA_FIELD_NUMBER: _ClassVar[int]
    CLJLDMKNEGD_FIELD_NUMBER: _ClassVar[int]
    MKEFPAAIHKP: _containers.RepeatedScalarFieldContainer[int]
    CBOHPEMFMPL: _containers.RepeatedScalarFieldContainer[int]
    JHNFDBBBMJC: _OMBEIFNNEDF_pb2.OMBEIFNNEDF
    JCOINGDOBMD: _OMBEIFNNEDF_pb2.OMBEIFNNEDF
    HKPDFIIEHPA: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    CLJLDMKNEGD: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, MKEFPAAIHKP: _Optional[_Iterable[int]] = ..., CBOHPEMFMPL: _Optional[_Iterable[int]] = ..., JHNFDBBBMJC: _Optional[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]] = ..., JCOINGDOBMD: _Optional[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]] = ..., HKPDFIIEHPA: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., CLJLDMKNEGD: _Optional[_Iterable[int]] = ...) -> None: ...
