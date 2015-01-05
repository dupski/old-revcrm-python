
from . import RevCRMModel, fields
from rev.i18n import translate as _

ACCOUNT_TYPES = [
    ('company', _('Company')),
    ('contact', _('Contact')),
]

class Account(RevCRMModel):

    _description = 'Account'
    
    name = fields.TextField(_('Account Name'))
    type = fields.SelectionField(_('Account Type'), ACCOUNT_TYPES)
    
    email = fields.EmailAddressField(_('E-mail Address'))
    phone = fields.PhoneNumberField(_('Main Phone Number'))
    phone2 = fields.PhoneNumberField(_('Alternative Phone Number'))

    notes = fields.TextField(_("Notes"))