from typing import List
from app.admin.VO.ProfileVO import ProfileVO
from app.admin.VO.PageVO import PageVO

class PermissionVO:

    __profile: ProfileVO
    
    __pages: List[PageVO]

    def __init__(self):
        self.__pages = []
        self.Clean()

    def Clean(self):
        self.__profile = ProfileVO()
        self.__pages = []

    @property
    def getPages(self) -> List[PageVO]:
        return self.__pages

    @__pages.setter
    def setPages(self, pages: List[PageVO]):
        self.__pages = pages

    @property
    def getProfile(self) -> ProfileVO:
        return self.__profile

    @__profile.setter
    def setProfile(self, profile: ProfileVO):
        self.__profile = profile

    def __str__(self):
        return "PermissionVO [profile=" + self.__profile + ", pages=" + self.__pages + "]"
