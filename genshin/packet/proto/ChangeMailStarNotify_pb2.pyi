from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeMailStarNotify(_message.Message):
    __slots__ = ("mail_id_list", "is_star")
    MAIL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_STAR_FIELD_NUMBER: _ClassVar[int]
    mail_id_list: _containers.RepeatedScalarFieldContainer[int]
    is_star: bool
    def __init__(self, mail_id_list: _Optional[_Iterable[int]] = ..., is_star: bool = ...) -> None: ...
