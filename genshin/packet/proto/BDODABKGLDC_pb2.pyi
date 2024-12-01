from genshin.packet.proto import APMHHCOHPLD_pb2 as _APMHHCOHPLD_pb2
from genshin.packet.proto import DKIFDGNKPLD_pb2 as _DKIFDGNKPLD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BDODABKGLDC(_message.Message):
    __slots__ = ("DAIJGKPMKHJ", "GDJKCKNOGBD", "KGOJIPMFHBM", "CIENOKDHFOD")
    DAIJGKPMKHJ_FIELD_NUMBER: _ClassVar[int]
    GDJKCKNOGBD_FIELD_NUMBER: _ClassVar[int]
    KGOJIPMFHBM_FIELD_NUMBER: _ClassVar[int]
    CIENOKDHFOD_FIELD_NUMBER: _ClassVar[int]
    DAIJGKPMKHJ: _containers.RepeatedScalarFieldContainer[str]
    GDJKCKNOGBD: _APMHHCOHPLD_pb2.APMHHCOHPLD
    KGOJIPMFHBM: _containers.RepeatedScalarFieldContainer[int]
    CIENOKDHFOD: _DKIFDGNKPLD_pb2.DKIFDGNKPLD
    def __init__(self, DAIJGKPMKHJ: _Optional[_Iterable[str]] = ..., GDJKCKNOGBD: _Optional[_Union[_APMHHCOHPLD_pb2.APMHHCOHPLD, _Mapping]] = ..., KGOJIPMFHBM: _Optional[_Iterable[int]] = ..., CIENOKDHFOD: _Optional[_Union[_DKIFDGNKPLD_pb2.DKIFDGNKPLD, _Mapping]] = ...) -> None: ...
