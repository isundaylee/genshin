from genshin.packet.proto import NLCDHFNMHLD_pb2 as _NLCDHFNMHLD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CBNCFKJIFNA(_message.Message):
    __slots__ = ("AGKPEKAANCA", "GFCKAOEOLBL", "JBPHCHJPDEM", "EMPEJFOGNPA", "EJNINFFFKJP")
    AGKPEKAANCA_FIELD_NUMBER: _ClassVar[int]
    GFCKAOEOLBL_FIELD_NUMBER: _ClassVar[int]
    JBPHCHJPDEM_FIELD_NUMBER: _ClassVar[int]
    EMPEJFOGNPA_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    AGKPEKAANCA: _containers.RepeatedScalarFieldContainer[int]
    GFCKAOEOLBL: _containers.RepeatedCompositeFieldContainer[_NLCDHFNMHLD_pb2.NLCDHFNMHLD]
    JBPHCHJPDEM: _containers.RepeatedCompositeFieldContainer[_NLCDHFNMHLD_pb2.NLCDHFNMHLD]
    EMPEJFOGNPA: _containers.RepeatedCompositeFieldContainer[_NLCDHFNMHLD_pb2.NLCDHFNMHLD]
    EJNINFFFKJP: int
    def __init__(self, AGKPEKAANCA: _Optional[_Iterable[int]] = ..., GFCKAOEOLBL: _Optional[_Iterable[_Union[_NLCDHFNMHLD_pb2.NLCDHFNMHLD, _Mapping]]] = ..., JBPHCHJPDEM: _Optional[_Iterable[_Union[_NLCDHFNMHLD_pb2.NLCDHFNMHLD, _Mapping]]] = ..., EMPEJFOGNPA: _Optional[_Iterable[_Union[_NLCDHFNMHLD_pb2.NLCDHFNMHLD, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
