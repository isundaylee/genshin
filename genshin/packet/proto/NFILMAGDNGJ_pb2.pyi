from genshin.packet.proto import KAPLJMBLBME_pb2 as _KAPLJMBLBME_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFILMAGDNGJ(_message.Message):
    __slots__ = ("BAGJBBKNADL", "OADMKDGJLAM")
    BAGJBBKNADL_FIELD_NUMBER: _ClassVar[int]
    OADMKDGJLAM_FIELD_NUMBER: _ClassVar[int]
    BAGJBBKNADL: _containers.RepeatedCompositeFieldContainer[_KAPLJMBLBME_pb2.KAPLJMBLBME]
    OADMKDGJLAM: bool
    def __init__(self, BAGJBBKNADL: _Optional[_Iterable[_Union[_KAPLJMBLBME_pb2.KAPLJMBLBME, _Mapping]]] = ..., OADMKDGJLAM: bool = ...) -> None: ...
