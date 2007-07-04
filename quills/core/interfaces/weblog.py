# Zope3 imports
from zope.interface import Interface


class IReadWeblog(Interface):
    """
    """

    def getEntries(max=None, offset=0):
        """Return a sequence of published IWeblogEntry instances, sorted by
        publishing date.  Only return a maximum of `max' (where None means no
        limit), and use `offset' to determine where in the full sequence the
        returned sequence starts from.
        """

    def getArchives():
        """Return an IWeblogArchiveContainer instance for this blog.
        """

    def getTopics():
        """Return a sequence of ITopic instances for this blog.
        """

    def getTopicById(id):
        """Return an ITopic instance corresponding to `id'.
        """

    def getAuthors():
        """Return a sequence of IAuthorTopic instances, one for every portal
        member id that has posted to this IWeblog.
        """

    def getAuthorById(id):
        """Return an IAuthorTopic instance for id.
        """


class IWriteWeblog(Interface):
    """
    """

    def addEntry(title, excerpt, text, topics=[], id=None, pubdate=None):
        """Add an entry from the provided arguments.  If id is None, normalize
        the title to create an id.  If pubdate is None, ignore it.
        Return the new entry.
        """


class IEditWeblog(Interface):
    """
    """

    def getDrafts(max=None, offset=None):
        """Return a sequence of unpublished IWeblogEntry instances, sorted by
        creation date.  Only return a maximum of `max' (where None means no
        limit), and use `offset' to determine where in the full sequence the
        returned sequence starts from.
        """

    def getAllEntries(max=None, offset=None):
        """Return a sequence all IWeblogEntry instances (published or not),
        sorted by publishing date.  Only return a maximum of `max' (where None
        means no limit), and use `offset' to offset where in the full sequence
        the returned sequence starts from.
        """

    def deleteEntry(entry_id):
        """Delete the IWeblogEntry corresponding to `entry_id'.
        """


class IWeblog(IReadWeblog, IWriteWeblog, IEditWeblog):
    """A weblog.
    """
