from genshin.packet.proto import BDNAACFEDFG_pb2 as _BDNAACFEDFG_pb2
from genshin.packet.proto import HKDCDFDMPMO_pb2 as _HKDCDFDMPMO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GEGFCJCAOFO(_message.Message):
    __slots__ = ("HMCKPCENIDK", "BAGJBBKNADL", "EEHLMDNGELN", "BBJDAEJPOFE")
    HMCKPCENIDK_FIELD_NUMBER: _ClassVar[int]
    BAGJBBKNADL_FIELD_NUMBER: _ClassVar[int]
    EEHLMDNGELN_FIELD_NUMBER: _ClassVar[int]
    BBJDAEJPOFE_FIELD_NUMBER: _ClassVar[int]
    HMCKPCENIDK: _containers.RepeatedCompositeFieldContainer[_BDNAACFEDFG_pb2.BDNAACFEDFG]
    BAGJBBKNADL: _containers.RepeatedCompositeFieldContainer[_HKDCDFDMPMO_pb2.HKDCDFDMPMO]
    EEHLMDNGELN: int
    BBJDAEJPOFE: int
    def __init__(self, HMCKPCENIDK: _Optional[_Iterable[_Union[_BDNAACFEDFG_pb2.BDNAACFEDFG, _Mapping]]] = ..., BAGJBBKNADL: _Optional[_Iterable[_Union[_HKDCDFDMPMO_pb2.HKDCDFDMPMO, _Mapping]]] = ..., EEHLMDNGELN: _Optional[int] = ..., BBJDAEJPOFE: _Optional[int] = ...) -> None: ...
