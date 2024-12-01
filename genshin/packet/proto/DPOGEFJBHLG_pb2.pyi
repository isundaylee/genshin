from genshin.packet.proto import MIBLPEIKDBP_pb2 as _MIBLPEIKDBP_pb2
from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DPOGEFJBHLG(_message.Message):
    __slots__ = ("BAGJBBKNADL", "CHJLKBOCPAG", "LGCBFNJNGPD")
    BAGJBBKNADL_FIELD_NUMBER: _ClassVar[int]
    CHJLKBOCPAG_FIELD_NUMBER: _ClassVar[int]
    LGCBFNJNGPD_FIELD_NUMBER: _ClassVar[int]
    BAGJBBKNADL: _containers.RepeatedCompositeFieldContainer[_MIBLPEIKDBP_pb2.MIBLPEIKDBP]
    CHJLKBOCPAG: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    LGCBFNJNGPD: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, BAGJBBKNADL: _Optional[_Iterable[_Union[_MIBLPEIKDBP_pb2.MIBLPEIKDBP, _Mapping]]] = ..., CHJLKBOCPAG: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., LGCBFNJNGPD: _Optional[_Iterable[int]] = ...) -> None: ...
