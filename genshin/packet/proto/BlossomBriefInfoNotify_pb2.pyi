from genshin.packet.proto import BlossomBriefInfo_pb2 as _BlossomBriefInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlossomBriefInfoNotify(_message.Message):
    __slots__ = ("brief_info_list",)
    BRIEF_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    brief_info_list: _containers.RepeatedCompositeFieldContainer[_BlossomBriefInfo_pb2.BlossomBriefInfo]
    def __init__(self, brief_info_list: _Optional[_Iterable[_Union[_BlossomBriefInfo_pb2.BlossomBriefInfo, _Mapping]]] = ...) -> None: ...
