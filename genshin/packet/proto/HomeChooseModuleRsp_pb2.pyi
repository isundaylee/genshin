from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeChooseModuleRsp(_message.Message):
    __slots__ = ("retcode", "module_id")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    module_id: int
    def __init__(self, retcode: _Optional[int] = ..., module_id: _Optional[int] = ...) -> None: ...
