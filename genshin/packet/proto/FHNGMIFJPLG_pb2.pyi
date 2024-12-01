from genshin.packet.proto import DINNMHNOCGD_pb2 as _DINNMHNOCGD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FHNGMIFJPLG(_message.Message):
    __slots__ = ("EKDOKDOGPIB", "EJNINFFFKJP", "HEPIBKMFGJI", "JCCKKCMGFME", "HGBBGLKPLFI", "CJOKFLDEFMB")
    EKDOKDOGPIB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    HEPIBKMFGJI_FIELD_NUMBER: _ClassVar[int]
    JCCKKCMGFME_FIELD_NUMBER: _ClassVar[int]
    HGBBGLKPLFI_FIELD_NUMBER: _ClassVar[int]
    CJOKFLDEFMB_FIELD_NUMBER: _ClassVar[int]
    EKDOKDOGPIB: _containers.RepeatedCompositeFieldContainer[_DINNMHNOCGD_pb2.DINNMHNOCGD]
    EJNINFFFKJP: int
    HEPIBKMFGJI: int
    JCCKKCMGFME: int
    HGBBGLKPLFI: int
    CJOKFLDEFMB: int
    def __init__(self, EKDOKDOGPIB: _Optional[_Iterable[_Union[_DINNMHNOCGD_pb2.DINNMHNOCGD, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., HEPIBKMFGJI: _Optional[int] = ..., JCCKKCMGFME: _Optional[int] = ..., HGBBGLKPLFI: _Optional[int] = ..., CJOKFLDEFMB: _Optional[int] = ...) -> None: ...
