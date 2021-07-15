from typing import List
from app.base.pagination.PaginationFilter import PaginationFilter
from app.base.pagination.BasePageItem import BasePageItem
from app.base.pagination.BasePageItemType import BasePageItemType
from app.base.services.UriService import UriService

PAGINATION_STEP = 3

class BasePaging:
    
    __nextEnabled: bool
    __prevEnabled: bool
    __pageSize: int
    __pageNumber: int

    __pageSort: str
    __columnOrder: int
    __columnTitle: str

    __items: List[BasePageItem]

    __totalRecords: int
    __firstPage: str
    __lastPage: str
    __nextPage: str
    __previousPage: str

    __nextEnabledClass: str
    __prevEnabledClass: str

    __validFilter: PaginationFilter
    __uriService: UriService
    __route: str
    
    def __init__(self, validFilter: PaginationFilter, uriService: UriService, route: str):
        self.__validFilter = validFilter
        self.__uriService = uriService
        self.__route = route

        self.__totalRecords = 0
        self.__items = []

    def Create(self, nextEnabled: bool, prevEnabled: bool, pageSize: int, pageNumber: int,
        pageSort: str, columnOrder: int, columnTitle: str, items: List[BasePageItem]):
        self.__nextEnabled = nextEnabled
        self.__prevEnabled = prevEnabled
        self.__pageSize = pageSize
        self.__pageNumber = pageNumber

        self.__pageSort = pageSort
        self.__columnOrder = columnOrder
        self.__columnTitle = columnTitle

        self.__items = items

    def getCurrentPage(self, pageNumber: int) -> str:
        return self.__uriService.getPageUri(PaginationFilter(self.__pageNumber,
            self.__validFilter.getSize(), self.__validFilter.getSort(),
            self.__validFilter.getColumnOrder(), self.__validFilter.getColumnTitle()), self.__route)

    def addPageItems(self, from: int, to: int, pageNumber: int):
        for i in range(from, to+1):
            self.__items.append(
                BasePageItem.builder().active(pageNumber != i).index(i)
                    .pageItemType(BasePageItemType.PAGE).build())

    def last(self, pageSize: int):
        self.__items.append(
            BasePageItem.builder().active(False)
                .pageItemType(BasePageItemType.DOTS).build())

        self.__items.append(
            BasePageItem.builder().active(True).index(pageSize)
                .pageItemType(BasePageItemType.PAGE).build())

    def first(self, pageNumber: int):
        self.__items.append(
            BasePageItem.builder().active(pageNumber != 1).index(1)
                .pageItemType(BasePageItemType.PAGE).build())

        self.__items.append(
            BasePageItem.builder().active(False)
                .pageItemType(BasePageItemType.DOTS).build())
