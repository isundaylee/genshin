from genshin.packet.proto import NLCDHFNMHLD_pb2 as _NLCDHFNMHLD_pb2
from genshin.packet.proto import MGOBEIPGIJA_pb2 as _MGOBEIPGIJA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HHGHPHMABEN(_message.Message):
    __slots__ = ("GFCKAOEOLBL", "JBPHCHJPDEM", "EMPEJFOGNPA", "HIBEKDDOFHB", "EJNINFFFKJP")
    GFCKAOEOLBL_FIELD_NUMBER: _ClassVar[int]
    JBPHCHJPDEM_FIELD_NUMBER: _ClassVar[int]
    EMPEJFOGNPA_FIELD_NUMBER: _ClassVar[int]
    HIBEKDDOFHB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    GFCKAOEOLBL: _containers.RepeatedCompositeFieldContainer[_NLCDHFNMHLD_pb2.NLCDHFNMHLD]
    JBPHCHJPDEM: _containers.RepeatedCompositeFieldContainer[_NLCDHFNMHLD_pb2.NLCDHFNMHLD]
    EMPEJFOGNPA: _containers.RepeatedCompositeFieldContainer[_NLCDHFNMHLD_pb2.NLCDHFNMHLD]
    HIBEKDDOFHB: _MGOBEIPGIJA_pb2.MGOBEIPGIJA
    EJNINFFFKJP: int
    def __init__(self, GFCKAOEOLBL: _Optional[_Iterable[_Union[_NLCDHFNMHLD_pb2.NLCDHFNMHLD, _Mapping]]] = ..., JBPHCHJPDEM: _Optional[_Iterable[_Union[_NLCDHFNMHLD_pb2.NLCDHFNMHLD, _Mapping]]] = ..., EMPEJFOGNPA: _Optional[_Iterable[_Union[_NLCDHFNMHLD_pb2.NLCDHFNMHLD, _Mapping]]] = ..., HIBEKDDOFHB: _Optional[_Union[_MGOBEIPGIJA_pb2.MGOBEIPGIJA, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
