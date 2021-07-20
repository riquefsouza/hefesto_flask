from typing import List
from app.base.report.ReportTypeEnum import ReportTypeEnum

class ReportType:

    __type: int

    __group: str

    __contentType: str

    __description: str

    __fileExtension: str

    def __init__(self, ntype: int, group: str,
        contentType: str, description: str, fileExtension: str):
        self.__type = ntype
        self.__group = group
        self.__contentType = contentType
        self.__description = description
        self.__fileExtension = fileExtension
    
    @staticmethod
    def groups(self) -> List[str]:
        return ["Documentos", "Planilhas", "Texto puro", "Outros"]
    
    @staticmethod
    def allTypes(self):
        rt = []

        rt.append(ReportType(ReportTypeEnum.PDF, "Documentos", "application/pdf", "Portable Document Format (.pdf)", "pdf"))
        rt.append(ReportType(ReportTypeEnum.DOCX, "Documentos", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "Microsoft Word XML (.docx)", "docx"))
        rt.append(ReportType(ReportTypeEnum.RTF, "Documentos", "application/rtf", "Rich Text Format (.rtf)", "rtf"))
        rt.append(ReportType(ReportTypeEnum.ODT, "Documentos", "application/vnd.oasis.opendocument.text", "OpenDocument Text (.odt)", "odt"))
        #rt.append(ReportType(ReportTypeEnum.XLS, "Planilhas", "application/vnd.ms-excel", "Microsoft Excel (.xls)"))
        rt.append(ReportType(ReportTypeEnum.XLSX, "Planilhas", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "Microsoft Excel XML (.xlsx)", "xlsx"))
        rt.append(ReportType(ReportTypeEnum.ODS, "Planilhas", "application/vnd.oasis.opendocument.spreadsheet", "OpenDocument Spreadsheet (.ods)", "ods"))
        rt.append(ReportType(ReportTypeEnum.CSV, "Texto puro", "text/plain", "Valores Separados Por Vírgula (.csv)", "csv"))
        rt.append(ReportType(ReportTypeEnum.TXT, "Texto puro", "text/plain", "Somente Texto (.txt)", "txt"))
        rt.append(ReportType(ReportTypeEnum.PPTX, "Outros", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "Microsoft Powerpoint XML (.pptx)", "pptx"))
        #rt.append(ReportType(ReportTypeEnum.HTML, "Outros", "text/html", "Linguagem de Marcação de Hipertexto (.html)"))
        rt.append(ReportType(ReportTypeEnum.HTML, "Outros", "application/zip", "Linguagem de Marcação de Hipertexto (.html)", "html"))

        return rt

    @staticmethod
    def getReportType(self, ntype: int):
        rt = ReportType.allTypes()

        for item in rt:
            if (item.getType() == ntype):
                return item
    
    @staticmethod
    def getType(self) -> int:
        return self.__type

    def setType(self, value: int):
        self.__type = value

    def getGroup(self) -> str:
        return self.__group

    def setGroup(self, value: str):
        self.__group = value

    def getDescription(self) -> str:
        return self.__description

    def setDescription(self, value: str):
        self.__description = value

    def getFileExtension(self) -> str:
        return self.__fileExtension

    def setFileExtension(self, value: str):
        self.__fileExtension = value
