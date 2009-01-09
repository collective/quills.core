# Zope3 imports
from zope.interface import Interface

# Local imports
from basecontent import IBaseContent


class IReadWeblogEntry(IBaseContent):
    """A weblog entry.
    """

    def getId():
        """Return the id of the entry.
        """

    def getTitle():
        """Return the title of the entry.
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

    def getWeblogEntryContentObject():
        """Return the content object that can be adapted to IWeblogEntry, and
        which this IWeblogEntry represents.
        """

    def getMimeType():
        """return the mimetype of the entry (i.e. text/plain, text/html etc.)"""
        pass


class IEditWeblogEntry(Interface):
    """
    """

    def setTitle(title):
        """
        """

    def setTopics(topic_ids):
        """
        """

    def setExcerpt(excerpt):
        """
        """

    def setText(text, mimetype=None):
        """
        If mimetype is None, use the default.
        """

    def edit(title, excerpt, text, topics, mimetype=None):
        """
        If mimetype is None, use the default.
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

    def publish(pubdate=None):
        """Publish this weblog entry.  Do nothing if it is already published.
        `pubdate' defaults to datetime.now().
        """

    def retract():
        """Retract this weblog entry to 'draft' status.  Do nothing if it is
        already a draft.
        """

    def isPublished():
        """Return True if this weblog entry is currently published, False
        otherwise.
        """
