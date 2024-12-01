from genshin.packet.proto import OLNCPFJIEKM_pb2 as _OLNCPFJIEKM_pb2
from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KJGAENHLKHP(_message.Message):
    __slots__ = ("AKGOOIIBCOM", "JGIEAJJBPNC", "item_list")
    AKGOOIIBCOM_FIELD_NUMBER: _ClassVar[int]
    JGIEAJJBPNC_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    AKGOOIIBCOM: _OLNCPFJIEKM_pb2.OLNCPFJIEKM
    JGIEAJJBPNC: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    def __init__(self, AKGOOIIBCOM: _Optional[_Union[_OLNCPFJIEKM_pb2.OLNCPFJIEKM, _Mapping]] = ..., JGIEAJJBPNC: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ...) -> None: ...
