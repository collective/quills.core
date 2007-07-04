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


class IReadWeblogEntry(Interface):
    """A weblog entry.
    """

    def getTopics():
        """Return a sequence of ITopic instances for this IWeblogEntry.
        """

    def getAuthors():
        """Return a sequence of IAuthorTopic instances for this IWeblogEntry.
        This will usually be a sequence of length == 1.
        """

    def getExcerpt():
        """Return an excerpt/description of the post.
        """

    def getText():
        """Return the HTML text body of the post.
        """

    def getPublicationDate():
        """Return a DateTime instance for when this IWeblogEntry was/will-be
        published.
        """


class IEditWeblogEntry(Interface):
    """
    """

    def setTopics(topic_ids):
        """
        """

    def setExcerpt(excerpt):
        """
        """

    def setText(text):
        """
        """

    def edit(self, title, excerpt, text, topics):
        """
        """

    def setPublicationDate(datetime):
        """Set when this IWeblogEntry was/will-be published.
        """


class IWeblogEntry(IReadWeblogEntry, IEditWeblogEntry):
    """A weblog entry.
    """


class IWorkflowedWeblogEntry(IWeblogEntry):
    """A very simple workflow implementation for weblog entries.
    """

    def publish(effective_date):
        """Publish this weblog entry.  Do nothing if it is already published.
        """

    def retract():
        """Retract this weblog entry to 'draft' status.  Do nothing if it is
        already a draft.
        """

    def isPublished():
        """Return True if this weblog entry is currently published, False
        otherwise.
        """


class ITopic(Interface):
    """A keyword, with an optionally associated image, that knows
    how to find content tagged with it.
    """

    def getId():
        """Return the keyword/id for this topic.
        """

    def getTitle():
        """Return title.
        """

    def getDescription():
        """Return the description for this topic.
        """

    def getImage():
        """Return an image object for this topic.
        """

    def getEntries(max=None, offset=0):
        """Return a sequence of published IWeblogEntry instances, sorted by
        publishing date.  Only return a maximum of `max' (where None means no
        limit), and use `offset' to determine where in the full sequence the
        returned sequence starts from.
        """

    def __len__():
        """Return the number of posts for this ITopic.
        """

    def __str__():
        """Return a string representation of one or more the keywords.
        """


class IAuthorTopic(ITopic):
    """Represents a topic that queries based on authors (aka 'Creators').
    """


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
