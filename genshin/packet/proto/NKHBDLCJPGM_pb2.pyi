from genshin.packet.proto import EALKFDEADIC_pb2 as _EALKFDEADIC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NKHBDLCJPGM(_message.Message):
    __slots__ = ("EFCDELGMMKG", "OFNMJNCBNHK", "GLKNGDDNOCN", "EAIPGEMKNPO", "IENCBCEGPBC")
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    OFNMJNCBNHK_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    IENCBCEGPBC_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_EALKFDEADIC_pb2.EALKFDEADIC]
    OFNMJNCBNHK: int
    GLKNGDDNOCN: bool
    EAIPGEMKNPO: int
    IENCBCEGPBC: int
    def __init__(self, EFCDELGMMKG: _Optional[_Iterable[_Union[_EALKFDEADIC_pb2.EALKFDEADIC, _Mapping]]] = ..., OFNMJNCBNHK: _Optional[int] = ..., GLKNGDDNOCN: bool = ..., EAIPGEMKNPO: _Optional[int] = ..., IENCBCEGPBC: _Optional[int] = ...) -> None: ...
