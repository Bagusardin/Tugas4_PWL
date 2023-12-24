from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Sepatu(_message.Message):
    __slots__ = ("id", "name", "description", "price", "image_url", "stock")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[int] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class SepatuListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SepatuListResponse(_message.Message):
    __slots__ = ("sepatus",)
    SEPATUS_FIELD_NUMBER: _ClassVar[int]
    sepatus: _containers.RepeatedCompositeFieldContainer[Sepatu]
    def __init__(self, sepatus: _Optional[_Iterable[_Union[Sepatu, _Mapping]]] = ...) -> None: ...

class SepatuRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class SepatuResponse(_message.Message):
    __slots__ = ("sepatu",)
    SEPATU_FIELD_NUMBER: _ClassVar[int]
    sepatu: Sepatu
    def __init__(self, sepatu: _Optional[_Union[Sepatu, _Mapping]] = ...) -> None: ...

class SepatuCreateRequest(_message.Message):
    __slots__ = ("name", "description", "price", "image_url", "stock")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[int] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class SepatuCreateResponse(_message.Message):
    __slots__ = ("sepatu",)
    SEPATU_FIELD_NUMBER: _ClassVar[int]
    sepatu: Sepatu
    def __init__(self, sepatu: _Optional[_Union[Sepatu, _Mapping]] = ...) -> None: ...

class SepatuUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "description", "price", "image_url", "stock")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[int] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class SepatuUpdateResponse(_message.Message):
    __slots__ = ("sepatu",)
    SEPATU_FIELD_NUMBER: _ClassVar[int]
    sepatu: Sepatu
    def __init__(self, sepatu: _Optional[_Union[Sepatu, _Mapping]] = ...) -> None: ...

class SepatuDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class SepatuDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
