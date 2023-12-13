
from ..service.BaseModelService import BaseModelService
class CourseCategoryService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'courseCategory')
    def getByFilter(self, filter={}):
        return super().getByFilter(filter)

