from genshin.packet.proto import FDIGDFDCNJC_pb2 as _FDIGDFDCNJC_pb2
from genshin.packet.proto import HJKIGLGDDON_pb2 as _HJKIGLGDDON_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CHGNHDCHNDD(_message.Message):
    __slots__ = ("AMBDAFCLIAG", "DDIGGFPIFNB", "PEMALBHPMKF")
    AMBDAFCLIAG_FIELD_NUMBER: _ClassVar[int]
    DDIGGFPIFNB_FIELD_NUMBER: _ClassVar[int]
    PEMALBHPMKF_FIELD_NUMBER: _ClassVar[int]
    AMBDAFCLIAG: _FDIGDFDCNJC_pb2.FDIGDFDCNJC
    DDIGGFPIFNB: int
    PEMALBHPMKF: _HJKIGLGDDON_pb2.HJKIGLGDDON
    def __init__(self, AMBDAFCLIAG: _Optional[_Union[_FDIGDFDCNJC_pb2.FDIGDFDCNJC, str]] = ..., DDIGGFPIFNB: _Optional[int] = ..., PEMALBHPMKF: _Optional[_Union[_HJKIGLGDDON_pb2.HJKIGLGDDON, str]] = ...) -> None: ...
