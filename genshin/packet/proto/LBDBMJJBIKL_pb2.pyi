from genshin.packet.proto import IMOKHHLJPIE_pb2 as _IMOKHHLJPIE_pb2
from genshin.packet.proto import DEBENKFIGJP_pb2 as _DEBENKFIGJP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LBDBMJJBIKL(_message.Message):
    __slots__ = ("FHNBLGGIOJA", "FOOKDBCNGAL")
    FHNBLGGIOJA_FIELD_NUMBER: _ClassVar[int]
    FOOKDBCNGAL_FIELD_NUMBER: _ClassVar[int]
    FHNBLGGIOJA: _containers.RepeatedCompositeFieldContainer[_IMOKHHLJPIE_pb2.IMOKHHLJPIE]
    FOOKDBCNGAL: _containers.RepeatedCompositeFieldContainer[_DEBENKFIGJP_pb2.DEBENKFIGJP]
    def __init__(self, FHNBLGGIOJA: _Optional[_Iterable[_Union[_IMOKHHLJPIE_pb2.IMOKHHLJPIE, _Mapping]]] = ..., FOOKDBCNGAL: _Optional[_Iterable[_Union[_DEBENKFIGJP_pb2.DEBENKFIGJP, _Mapping]]] = ...) -> None: ...
