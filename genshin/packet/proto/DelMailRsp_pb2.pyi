from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DelMailRsp(_message.Message):
    __slots__ = ("mail_id_list", "retcode")
    MAIL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    mail_id_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    def __init__(self, mail_id_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ...) -> None: ...
