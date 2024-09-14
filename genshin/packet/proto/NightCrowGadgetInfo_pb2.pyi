from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NightCrowGadgetInfo(_message.Message):
    __slots__ = ("argument_list",)
    ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    argument_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, argument_list: _Optional[_Iterable[int]] = ...) -> None: ...