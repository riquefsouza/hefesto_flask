from typing import List
from app.base.report.ReportGroupVO import ReportGroupVO
from app.base.report.ReportType import ReportType
from app.base.BaseController import BaseController
from app.controllers.Messages import MESSAGES

class BaseViewReportController(BaseController):

    def getListReportType() -> List[ReportGroupVO]:
        listaVO = []
        listaEnum = ReportType.allTypes()
        subtipos = []

        for grupo in ReportType.groups():
            igrupo = ""
            subtipos = []

            for item in listaEnum:
                if (item.getGroup() == grupo):
                    subtipos.append(item)

            if (grupo == ReportType.groups()[0]):
                igrupo = MESSAGES["reportTypeGroups.docs"]
            if (grupo == ReportType.groups()[1])
                igrupo = MESSAGES["reportTypeGroups.sheets"]
            if (grupo == ReportType.groups()[2])
                igrupo = MESSAGES["reportTypeGroups.text"]
            if (grupo == ReportType.groups()[3])
                igrupo = MESSAGES["reportTypeGroups.others"]

            grupoVO = ReportGroupVO(igrupo, subtipos)

            listaVO.append(grupoVO)

        return listaVO
