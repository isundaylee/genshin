from genshin.packet.proto import ActivityShopSheetInfo_pb2 as _ActivityShopSheetInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetActivityShopSheetInfoRsp(_message.Message):
    __slots__ = ("sheet_info_list", "shop_type", "retcode")
    SHEET_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    SHOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    sheet_info_list: _containers.RepeatedCompositeFieldContainer[_ActivityShopSheetInfo_pb2.ActivityShopSheetInfo]
    shop_type: int
    retcode: int
    def __init__(self, sheet_info_list: _Optional[_Iterable[_Union[_ActivityShopSheetInfo_pb2.ActivityShopSheetInfo, _Mapping]]] = ..., shop_type: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
