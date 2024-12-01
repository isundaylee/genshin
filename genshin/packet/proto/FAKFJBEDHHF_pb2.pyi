from genshin.packet.proto import PFKMFKPLBPD_pb2 as _PFKMFKPLBPD_pb2
from genshin.packet.proto import CLIHEJNNIEC_pb2 as _CLIHEJNNIEC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FAKFJBEDHHF(_message.Message):
    __slots__ = ("AOOOFNMPOHP", "EHADPGHMJEF")
    AOOOFNMPOHP_FIELD_NUMBER: _ClassVar[int]
    EHADPGHMJEF_FIELD_NUMBER: _ClassVar[int]
    AOOOFNMPOHP: _containers.RepeatedCompositeFieldContainer[_PFKMFKPLBPD_pb2.PFKMFKPLBPD]
    EHADPGHMJEF: _CLIHEJNNIEC_pb2.CLIHEJNNIEC
    def __init__(self, AOOOFNMPOHP: _Optional[_Iterable[_Union[_PFKMFKPLBPD_pb2.PFKMFKPLBPD, _Mapping]]] = ..., EHADPGHMJEF: _Optional[_Union[_CLIHEJNNIEC_pb2.CLIHEJNNIEC, _Mapping]] = ...) -> None: ...
