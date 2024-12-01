from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KMDAEPAENAB(_message.Message):
    __slots__ = ("item_list", "DIGPDMKMGAF", "EJNINFFFKJP", "JPHIOJMOMIG")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    DIGPDMKMGAF_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    JPHIOJMOMIG_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    DIGPDMKMGAF: int
    EJNINFFFKJP: int
    JPHIOJMOMIG: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., DIGPDMKMGAF: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ..., JPHIOJMOMIG: _Optional[int] = ...) -> None: ...
