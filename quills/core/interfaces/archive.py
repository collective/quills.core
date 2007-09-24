# Local imports
from basecontent import IBaseContent

class IWeblogArchive(IBaseContent):
    """An archive folder for a weblog.
    """

    def getSubArchives():
        """Get a listing of all sub-archives.
        """

    def getEntries(maximum=None, offset=0):
        """Return a sequence of published IWeblogEntry instances, sorted by
        publishing date.  Only return a maximum of `maximum' (where None means no
        limit), and use `offset' to determine where in the full sequence the
        returned sequence starts from.
        """

    def __len__():
        """Return the number of IWeblogEntry instances in this archive.
        """


class IWeblogArchiveContainer(IWeblogArchive):
    """An interface for the root archive container for an IWeblog when there is
    an extra 'archive' URL segment in use: e.g. '.../weblog/archive/2007/07'
    """
