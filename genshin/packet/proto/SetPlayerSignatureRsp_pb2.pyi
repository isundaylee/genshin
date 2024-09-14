from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPlayerSignatureRsp(_message.Message):
    __slots__ = ("retcode", "signature")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    signature: str
    def __init__(self, retcode: _Optional[int] = ..., signature: _Optional[str] = ...) -> None: ...
