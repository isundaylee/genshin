from genshin.packet.proto import EJOBMPBBBIA_pb2 as _EJOBMPBBBIA_pb2
from genshin.packet.proto import JNMHJONHLAG_pb2 as _JNMHJONHLAG_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OBJFJALGAOK(_message.Message):
    __slots__ = ("HHAAPMKKHOE", "AMANMHAPIDG", "MEJLFKPFPGK", "MDFKDAJIGEM", "OPLBKMAKNAG", "item_id")
    HHAAPMKKHOE_FIELD_NUMBER: _ClassVar[int]
    AMANMHAPIDG_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    MDFKDAJIGEM_FIELD_NUMBER: _ClassVar[int]
    OPLBKMAKNAG_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    HHAAPMKKHOE: _EJOBMPBBBIA_pb2.EJOBMPBBBIA
    AMANMHAPIDG: _JNMHJONHLAG_pb2.JNMHJONHLAG
    MEJLFKPFPGK: int
    MDFKDAJIGEM: int
    OPLBKMAKNAG: int
    item_id: int
    def __init__(self, HHAAPMKKHOE: _Optional[_Union[_EJOBMPBBBIA_pb2.EJOBMPBBBIA, _Mapping]] = ..., AMANMHAPIDG: _Optional[_Union[_JNMHJONHLAG_pb2.JNMHJONHLAG, _Mapping]] = ..., MEJLFKPFPGK: _Optional[int] = ..., MDFKDAJIGEM: _Optional[int] = ..., OPLBKMAKNAG: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...
