from genshin.packet.proto import ProfilePicture_pb2 as _ProfilePicture_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FurnitureMakeBeHelpedData(_message.Message):
    __slots__ = ("profile_picture", "uid", "time", "icon", "player_name")
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    profile_picture: _ProfilePicture_pb2.ProfilePicture
    uid: int
    time: int
    icon: int
    player_name: str
    def __init__(self, profile_picture: _Optional[_Union[_ProfilePicture_pb2.ProfilePicture, _Mapping]] = ..., uid: _Optional[int] = ..., time: _Optional[int] = ..., icon: _Optional[int] = ..., player_name: _Optional[str] = ...) -> None: ...
