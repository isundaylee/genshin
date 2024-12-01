from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import NLCDHFNMHLD_pb2 as _NLCDHFNMHLD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NMPODKOMAGD(_message.Message):
    __slots__ = ("FGAFONOJIPA", "item_list", "OLAELJFCMMN", "KIFDLGCOHEN", "DACDKGBNBFM", "BAPGGIKNLLH", "PJABEFAJBGB", "IMIOGMDOKCB")
    FGAFONOJIPA_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    OLAELJFCMMN_FIELD_NUMBER: _ClassVar[int]
    KIFDLGCOHEN_FIELD_NUMBER: _ClassVar[int]
    DACDKGBNBFM_FIELD_NUMBER: _ClassVar[int]
    BAPGGIKNLLH_FIELD_NUMBER: _ClassVar[int]
    PJABEFAJBGB_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    FGAFONOJIPA: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    item_list: _containers.RepeatedCompositeFieldContainer[_NLCDHFNMHLD_pb2.NLCDHFNMHLD]
    OLAELJFCMMN: _containers.RepeatedCompositeFieldContainer[_NLCDHFNMHLD_pb2.NLCDHFNMHLD]
    KIFDLGCOHEN: bool
    DACDKGBNBFM: bool
    BAPGGIKNLLH: bool
    PJABEFAJBGB: int
    IMIOGMDOKCB: int
    def __init__(self, FGAFONOJIPA: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., item_list: _Optional[_Iterable[_Union[_NLCDHFNMHLD_pb2.NLCDHFNMHLD, _Mapping]]] = ..., OLAELJFCMMN: _Optional[_Iterable[_Union[_NLCDHFNMHLD_pb2.NLCDHFNMHLD, _Mapping]]] = ..., KIFDLGCOHEN: bool = ..., DACDKGBNBFM: bool = ..., BAPGGIKNLLH: bool = ..., PJABEFAJBGB: _Optional[int] = ..., IMIOGMDOKCB: _Optional[int] = ...) -> None: ...
