from genshin.packet.proto import MPCBGINJKKD_pb2 as _MPCBGINJKKD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BFFALDPOKFE(_message.Message):
    __slots__ = ("NKICBOBIDAF", "EFCDELGMMKG")
    NKICBOBIDAF_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    NKICBOBIDAF: _containers.RepeatedScalarFieldContainer[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_MPCBGINJKKD_pb2.MPCBGINJKKD]
    def __init__(self, NKICBOBIDAF: _Optional[_Iterable[int]] = ..., EFCDELGMMKG: _Optional[_Iterable[_Union[_MPCBGINJKKD_pb2.MPCBGINJKKD, _Mapping]]] = ...) -> None: ...
