from genshin.packet.proto import FCHICPCAAGK_pb2 as _FCHICPCAAGK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HKGKJOGDGIL(_message.Message):
    __slots__ = ("ODIJHNLAOJO", "EJNINFFFKJP", "DNBEFLJLAMB")
    ODIJHNLAOJO_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    ODIJHNLAOJO: _containers.RepeatedCompositeFieldContainer[_FCHICPCAAGK_pb2.FCHICPCAAGK]
    EJNINFFFKJP: int
    DNBEFLJLAMB: int
    def __init__(self, ODIJHNLAOJO: _Optional[_Iterable[_Union[_FCHICPCAAGK_pb2.FCHICPCAAGK, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ...) -> None: ...
