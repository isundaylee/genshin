from genshin.packet.proto import ProfilePicture_pb2 as _ProfilePicture_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetPlayerHeadImageRsp(_message.Message):
    __slots__ = ("profile_picture", "retcode")
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    profile_picture: _ProfilePicture_pb2.ProfilePicture
    retcode: int
    def __init__(self, profile_picture: _Optional[_Union[_ProfilePicture_pb2.ProfilePicture, _Mapping]] = ..., retcode: _Optional[int] = ...) -> None: ...
