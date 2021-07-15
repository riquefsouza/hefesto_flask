from app.base.pagination.PaginationFilter import PaginationFilter

class UriService:

    __baseUri: str

    def __init__(self, baseUri: str):
        self.__baseUri = baseUri

    def getPageUri(self, filter: PaginationFilter, route: str) -> str:
        enpointUri = self.__baseUri + "/" + route
        modifiedUri = enpointUri + "?pageNumber=" + filter.getPageNumber()
        modifiedUri = modifiedUri + "&size=" + filter.getSize()
        modifiedUri = modifiedUri + "&sort=" + filter.getSort()
        modifiedUri = modifiedUri + "&columnOrder=" + filter.getColumnOrder()
        modifiedUri = modifiedUri + "&columnTitle=" + filter.getColumnTitle()

        return modifiedUri
