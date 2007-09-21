# Zope imports
from zope.interface import Interface


class IBaseContent(Interface):
    """Base interface for Quills content-ish types.
    """

    def getWeblog():
        """Return the IWeblog object that this content lives in.  This may be an
        object adapted to IWeblog.
        """

    def getWeblogContentObject():
        """Return the content object that can be adapted to IWeblog, and in
        which this content lives.
        """
