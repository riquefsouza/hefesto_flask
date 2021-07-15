from typing import List
import string

class BasePaged:
    
    __page: List

    __paging: BasePaging

    def __init__(self, page: List, paging: BasePaging):
        try:
            paramSort = paging.getPageSort.split(",")
            sortFieldName = ""

            if (len(paramSort) > 0):
                sortFieldName = paramSort[1].lower()

                if (paramSort[0]).upper() == "ASC"):
                    #page = page.OrderBy(s => s.GetType().GetProperty(sortFieldName).GetValue(s)).ToList()
                    page.sort()
                else:
                    #page = page.OrderByDescending(s => s.GetType().GetProperty(sortFieldName).GetValue(s)).ToList()
                    page.sort(reverse=True)

        except Exception as err:
            print("Error Sort BasePaged: {0}".format(err))

        self.setPage(page)
        self.setPaging(paging)

    def getPage(self):
        return self.__page

    def setPage(self, page: List):
        self.__page = page

    def getPaging(self):
        return self.__paging

    def setPaging(paging: BasePaging):
        self.__paging = paging        