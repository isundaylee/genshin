from genshin.packet.proto import AnimatorParameterValueInfo_pb2 as _AnimatorParameterValueInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAnimatorParameterInfo(_message.Message):
    __slots__ = ("name_id", "value", "is_server_cache", "entity_id")
    NAME_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_SERVER_CACHE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    name_id: int
    value: _AnimatorParameterValueInfo_pb2.AnimatorParameterValueInfo
    is_server_cache: bool
    entity_id: int
    def __init__(self, name_id: _Optional[int] = ..., value: _Optional[_Union[_AnimatorParameterValueInfo_pb2.AnimatorParameterValueInfo, _Mapping]] = ..., is_server_cache: bool = ..., entity_id: _Optional[int] = ...) -> None: ...
