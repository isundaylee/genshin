from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import LCFLJAAIBIO_pb2 as _LCFLJAAIBIO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BKHELFCNAGD(_message.Message):
    __slots__ = ("item_list", "LBBKKKBBFFP", "PNBDCFALKPG", "LBMCNLFDHKL", "FCLHHLBCNIN", "EJNINFFFKJP")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    LBBKKKBBFFP_FIELD_NUMBER: _ClassVar[int]
    PNBDCFALKPG_FIELD_NUMBER: _ClassVar[int]
    LBMCNLFDHKL_FIELD_NUMBER: _ClassVar[int]
    FCLHHLBCNIN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    LBBKKKBBFFP: _LCFLJAAIBIO_pb2.LCFLJAAIBIO
    PNBDCFALKPG: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    LBMCNLFDHKL: int
    FCLHHLBCNIN: int
    EJNINFFFKJP: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., LBBKKKBBFFP: _Optional[_Union[_LCFLJAAIBIO_pb2.LCFLJAAIBIO, _Mapping]] = ..., PNBDCFALKPG: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., LBMCNLFDHKL: _Optional[int] = ..., FCLHHLBCNIN: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
