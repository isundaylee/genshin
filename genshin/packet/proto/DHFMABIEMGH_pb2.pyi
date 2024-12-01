from genshin.packet.proto import FLMMANLPMNB_pb2 as _FLMMANLPMNB_pb2
from genshin.packet.proto import APLFHDMBKHC_pb2 as _APLFHDMBKHC_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DHFMABIEMGH(_message.Message):
    __slots__ = ("JOFCOMOMBDO", "IBIPCGCOIFG", "AMGKAOJAKGM")
    JOFCOMOMBDO_FIELD_NUMBER: _ClassVar[int]
    IBIPCGCOIFG_FIELD_NUMBER: _ClassVar[int]
    AMGKAOJAKGM_FIELD_NUMBER: _ClassVar[int]
    JOFCOMOMBDO: str
    IBIPCGCOIFG: _FLMMANLPMNB_pb2.FLMMANLPMNB
    AMGKAOJAKGM: _APLFHDMBKHC_pb2.APLFHDMBKHC
    def __init__(self, JOFCOMOMBDO: _Optional[str] = ..., IBIPCGCOIFG: _Optional[_Union[_FLMMANLPMNB_pb2.FLMMANLPMNB, str]] = ..., AMGKAOJAKGM: _Optional[_Union[_APLFHDMBKHC_pb2.APLFHDMBKHC, str]] = ...) -> None: ...
