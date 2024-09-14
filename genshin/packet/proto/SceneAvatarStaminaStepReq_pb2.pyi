from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneAvatarStaminaStepReq(_message.Message):
    __slots__ = ("rot", "use_client_rot")
    ROT_FIELD_NUMBER: _ClassVar[int]
    USE_CLIENT_ROT_FIELD_NUMBER: _ClassVar[int]
    rot: _Vector_pb2.Vector
    use_client_rot: bool
    def __init__(self, rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., use_client_rot: bool = ...) -> None: ...
