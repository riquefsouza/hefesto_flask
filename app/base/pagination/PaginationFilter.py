class PaginationFilter:

    __pageNumber: int

    __size: int

    __sort: str

    __columnOrder: int

    __columnTitle: str

    def __init__(self):
        self.__pageNumber = 1
        self.__size = 10
        self.__sort = "ASC,id"
        self.__columnOrder = 0
        self.__columnTitle = "id"

    def Create(self, pageNumber: int, size: int, sort: str, columnOrder: int, columnTitle: str):
        self.__pageNumber = 1 if pageNumber < 1 else pageNumber
        self.__size = 10 if size < 10 else size
        self.__sort = "ASC, id" if len(sort.strip()) == 0 else sort
        self.__columnOrder = 0 if columnOrder < 0 else columnOrder
        self.__columnTitle = "id" if len(columnTitle.strip()) == 0 else columnTitle

    def getPageNumber(self) -> int:
        return self.__pageNumber

    def setPageNumber(self, value: int):
        self.__pageNumber = value

    def getSize(self) -> int:
        return self.__size

    def setSize(self, value: int):
        self.__size = value

    def getSort(self) -> str:
        return self.__sort

    def setSort(self, value: str):
        self.__sort = value

    def getColumnOrder(self) -> int:
        return self.__columnOrder

    def setColumnOrder(self, value: int):
        self.__columnOrder = value

    def getColumnTitle(self) -> str:
        return self.__columnTitle

    def setColumnTitle(self, value: str):
        self.__columnTitle = value        