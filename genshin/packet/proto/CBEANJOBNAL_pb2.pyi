from genshin.packet.proto import CAIMBAMKDAL_pb2 as _CAIMBAMKDAL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CBEANJOBNAL(_message.Message):
    __slots__ = ("AOOEDBJIBIL", "GFPDHHIHBPN")
    AOOEDBJIBIL_FIELD_NUMBER: _ClassVar[int]
    GFPDHHIHBPN_FIELD_NUMBER: _ClassVar[int]
    AOOEDBJIBIL: _containers.RepeatedCompositeFieldContainer[_CAIMBAMKDAL_pb2.CAIMBAMKDAL]
    GFPDHHIHBPN: int
    def __init__(self, AOOEDBJIBIL: _Optional[_Iterable[_Union[_CAIMBAMKDAL_pb2.CAIMBAMKDAL, _Mapping]]] = ..., GFPDHHIHBPN: _Optional[int] = ...) -> None: ...
