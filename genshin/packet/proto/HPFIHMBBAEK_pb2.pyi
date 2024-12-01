from genshin.packet.proto import PBKKCEOCHEB_pb2 as _PBKKCEOCHEB_pb2
from genshin.packet.proto import GPCMGDAKOEM_pb2 as _GPCMGDAKOEM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HPFIHMBBAEK(_message.Message):
    __slots__ = ("PEOILIHAHJK", "IJJLKLPAOAA")
    PEOILIHAHJK_FIELD_NUMBER: _ClassVar[int]
    IJJLKLPAOAA_FIELD_NUMBER: _ClassVar[int]
    PEOILIHAHJK: _containers.RepeatedCompositeFieldContainer[_PBKKCEOCHEB_pb2.PBKKCEOCHEB]
    IJJLKLPAOAA: _containers.RepeatedCompositeFieldContainer[_GPCMGDAKOEM_pb2.GPCMGDAKOEM]
    def __init__(self, PEOILIHAHJK: _Optional[_Iterable[_Union[_PBKKCEOCHEB_pb2.PBKKCEOCHEB, _Mapping]]] = ..., IJJLKLPAOAA: _Optional[_Iterable[_Union[_GPCMGDAKOEM_pb2.GPCMGDAKOEM, _Mapping]]] = ...) -> None: ...
