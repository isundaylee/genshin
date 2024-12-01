from genshin.packet.proto import ALDKFFOGBBD_pb2 as _ALDKFFOGBBD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EOMGGPPGKAI(_message.Message):
    __slots__ = ("ALDMOGBAHNI", "EJNINFFFKJP", "OFNOGJPGBNA")
    ALDMOGBAHNI_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    OFNOGJPGBNA_FIELD_NUMBER: _ClassVar[int]
    ALDMOGBAHNI: _containers.RepeatedCompositeFieldContainer[_ALDKFFOGBBD_pb2.ALDKFFOGBBD]
    EJNINFFFKJP: int
    OFNOGJPGBNA: int
    def __init__(self, ALDMOGBAHNI: _Optional[_Iterable[_Union[_ALDKFFOGBBD_pb2.ALDKFFOGBBD, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., OFNOGJPGBNA: _Optional[int] = ...) -> None: ...
