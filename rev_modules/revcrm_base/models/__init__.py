
from rev.db import Model, fields
from rev.db.mixins import XMLDataMixin
from rev.i18n import translate as _

class RevCRMModel(XMLDataMixin, Model):
    """
    Base class for rev_app metadata models
    """
    
    id = fields.RecordIDField(_('Record ID'))
    #created_by
    #created_date
    #updated_by
    #updated_date