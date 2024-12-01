from genshin.packet.proto import LLOBOJJFONB_pb2 as _LLOBOJJFONB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IHOKGDIHIDA(_message.Message):
    __slots__ = ("EMOJGIDCMFD", "ONJNHPGGEFO", "NKGDGKCIDJJ", "MGDEPMJLBAO", "HBELMAAKKIO", "LOHBCBDEPIB", "EAIPGEMKNPO")
    class EMOJGIDCMFDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _LLOBOJJFONB_pb2.LLOBOJJFONB
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_LLOBOJJFONB_pb2.LLOBOJJFONB, _Mapping]] = ...) -> None: ...
    EMOJGIDCMFD_FIELD_NUMBER: _ClassVar[int]
    ONJNHPGGEFO_FIELD_NUMBER: _ClassVar[int]
    NKGDGKCIDJJ_FIELD_NUMBER: _ClassVar[int]
    MGDEPMJLBAO_FIELD_NUMBER: _ClassVar[int]
    HBELMAAKKIO_FIELD_NUMBER: _ClassVar[int]
    LOHBCBDEPIB_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    EMOJGIDCMFD: _containers.MessageMap[int, _LLOBOJJFONB_pb2.LLOBOJJFONB]
    ONJNHPGGEFO: int
    NKGDGKCIDJJ: int
    MGDEPMJLBAO: int
    HBELMAAKKIO: bool
    LOHBCBDEPIB: bool
    EAIPGEMKNPO: int
    def __init__(self, EMOJGIDCMFD: _Optional[_Mapping[int, _LLOBOJJFONB_pb2.LLOBOJJFONB]] = ..., ONJNHPGGEFO: _Optional[int] = ..., NKGDGKCIDJJ: _Optional[int] = ..., MGDEPMJLBAO: _Optional[int] = ..., HBELMAAKKIO: bool = ..., LOHBCBDEPIB: bool = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
