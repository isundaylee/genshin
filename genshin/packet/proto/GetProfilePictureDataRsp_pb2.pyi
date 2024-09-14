from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetProfilePictureDataRsp(_message.Message):
    __slots__ = ("special_profile_picture_list", "retcode")
    SPECIAL_PROFILE_PICTURE_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    special_profile_picture_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    def __init__(self, special_profile_picture_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ...) -> None: ...
