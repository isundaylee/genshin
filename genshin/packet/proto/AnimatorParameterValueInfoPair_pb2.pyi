from genshin.packet.proto import AnimatorParameterValueInfo_pb2 as _AnimatorParameterValueInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnimatorParameterValueInfoPair(_message.Message):
    __slots__ = ("name_id", "animator_para")
    NAME_ID_FIELD_NUMBER: _ClassVar[int]
    ANIMATOR_PARA_FIELD_NUMBER: _ClassVar[int]
    name_id: int
    animator_para: _AnimatorParameterValueInfo_pb2.AnimatorParameterValueInfo
    def __init__(self, name_id: _Optional[int] = ..., animator_para: _Optional[_Union[_AnimatorParameterValueInfo_pb2.AnimatorParameterValueInfo, _Mapping]] = ...) -> None: ...
