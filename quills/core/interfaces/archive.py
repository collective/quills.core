# Zope3 imports
from zope.interface import Interface

class IWeblogArchive(Interface):
    """An archive folder for a weblog.
    """

    def getSubArchives():
        """Get a listing of all sub-archives.
        """

    def getEntries(max=None, offset=0):
        """Return a sequence of published IWeblogEntry instances, sorted by
        publishing date.  Only return a maximum of `max' (where None means no
        limit), and use `offset' to determine where in the full sequence the
        returned sequence starts from.
        """

    def __len__():
        """Return the number of IWeblogEntry instances in this archive.
        """


class IWeblogArchiveContainer(IWeblogArchive):
    """Marker interface for the root archive container for an IWeblog.
    """
