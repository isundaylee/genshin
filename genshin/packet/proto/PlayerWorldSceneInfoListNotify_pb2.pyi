from genshin.packet.proto import PlayerWorldSceneInfo_pb2 as _PlayerWorldSceneInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerWorldSceneInfoListNotify(_message.Message):
    __slots__ = ("info_list", "KNFOKJBGBEI")
    INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    KNFOKJBGBEI_FIELD_NUMBER: _ClassVar[int]
    info_list: _containers.RepeatedCompositeFieldContainer[_PlayerWorldSceneInfo_pb2.PlayerWorldSceneInfo]
    KNFOKJBGBEI: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, info_list: _Optional[_Iterable[_Union[_PlayerWorldSceneInfo_pb2.PlayerWorldSceneInfo, _Mapping]]] = ..., KNFOKJBGBEI: _Optional[_Iterable[int]] = ...) -> None: ...
