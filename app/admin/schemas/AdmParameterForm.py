from app.admin.models.AdmParameter import AdmParameter
from typing import Dict


class AdmParameterForm:
    code: str
    description: str
    idParameterCategory: int
    value: str
    #admParameterCategory: AdmParameterCategory 

    def __init__(self, admParameter: Dict):
        self.code=admParameter["code"]
        self.description=admParameter["description"]
        self.idParameterCategory=admParameter["idParameterCategory"]
        self.value=admParameter["value"]
        #self.admParameterCategory=admParameter["admParameterCategory"]

    def to_AdmParameter(self):
        newAdmParameter = AdmParameter(
            code=self.code,
            description=self.description,
            idParameterCategory=self.idParameterCategory,
            value=self.value
            #admParameterCategory=self.admParameterCategory
        )
        return newAdmParameter

    def from_AdmParameter(self, admParameter: AdmParameter):
        admParameter.code=self.code
        admParameter.description=self.description
        admParameter.idParameterCategory=self.idParameterCategory
        admParameter.value=self.value
        #admParameter.admParameterCategory=self.admParameterCategory

        return admParameter
