from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalSceneJumpRsp(_message.Message):
    __slots__ = ("dest_pos", "dest_scene_id", "retcode")
    DEST_POS_FIELD_NUMBER: _ClassVar[int]
    DEST_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    dest_pos: _Vector_pb2.Vector
    dest_scene_id: int
    retcode: int
    def __init__(self, dest_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., dest_scene_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
