from genshin.packet.proto import CutSceneExtraParam_pb2 as _CutSceneExtraParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CutSceneBeginNotify(_message.Message):
    __slots__ = ("cutscene_id", "is_wait_others", "extra_param_list")
    CUTSCENE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_WAIT_OTHERS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    cutscene_id: int
    is_wait_others: bool
    extra_param_list: _containers.RepeatedCompositeFieldContainer[_CutSceneExtraParam_pb2.CutSceneExtraParam]
    def __init__(self, cutscene_id: _Optional[int] = ..., is_wait_others: bool = ..., extra_param_list: _Optional[_Iterable[_Union[_CutSceneExtraParam_pb2.CutSceneExtraParam, _Mapping]]] = ...) -> None: ...
