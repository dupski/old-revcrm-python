
from rev.db.models import DBModel, fields
from rev.models.mixins import XMLDataMixin
from rev.i18n import translate as _

class RevCRMModel(DBModel, XMLDataMixin):
    """
    Base class for rev_app metadata models
    """
    
    id = fields.RecordIDField(_('Record ID'))
    #created_by
    #created_date
    #updated_by
    #updated_date