from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KHPFEKNJDOF(_message.Message):
    __slots__ = ("CHEHPFEHBOP", "CMKFFDOALEM", "DIFIMMMNJFO", "MEOHEILLEBH", "KNGJHMLLCNP", "FDMKMFBOCLA", "JPDBMDLEEEC", "JFGGPGKHJCK")
    class CHEHPFEHBOPEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class CMKFFDOALEMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CHEHPFEHBOP_FIELD_NUMBER: _ClassVar[int]
    CMKFFDOALEM_FIELD_NUMBER: _ClassVar[int]
    DIFIMMMNJFO_FIELD_NUMBER: _ClassVar[int]
    MEOHEILLEBH_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    FDMKMFBOCLA_FIELD_NUMBER: _ClassVar[int]
    JPDBMDLEEEC_FIELD_NUMBER: _ClassVar[int]
    JFGGPGKHJCK_FIELD_NUMBER: _ClassVar[int]
    CHEHPFEHBOP: _containers.ScalarMap[int, int]
    CMKFFDOALEM: _containers.ScalarMap[int, int]
    DIFIMMMNJFO: int
    MEOHEILLEBH: int
    KNGJHMLLCNP: int
    FDMKMFBOCLA: int
    JPDBMDLEEEC: int
    JFGGPGKHJCK: int
    def __init__(self, CHEHPFEHBOP: _Optional[_Mapping[int, int]] = ..., CMKFFDOALEM: _Optional[_Mapping[int, int]] = ..., DIFIMMMNJFO: _Optional[int] = ..., MEOHEILLEBH: _Optional[int] = ..., KNGJHMLLCNP: _Optional[int] = ..., FDMKMFBOCLA: _Optional[int] = ..., JPDBMDLEEEC: _Optional[int] = ..., JFGGPGKHJCK: _Optional[int] = ...) -> None: ...
