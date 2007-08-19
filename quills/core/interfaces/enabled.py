# Zope imports
from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory

# Quills imports
from quills.core.interfaces import IWeblogConfiguration


class IPossibleWeblog(Interface):
    """A marker interface for representing what *could* be a weblog.
    """


class IWeblogEnhanced(Interface):
    """A marker interface to indicate an item that has weblog functionality.
    """


class IPossibleWeblogEntry(Interface):
    """A marker interface for representing what *could* be a weblog entry.
    """


_ = MessageFactory('quills')

class IWeblogEnhancedConfiguration(IWeblogConfiguration):
    """
    """

    defaultType = schema.TextLine(
        title=_(u'Default type.'),
        description=_(u'The default portal_type to add for this weblog.'),
        default=u'Document',
        required=False,
        )
