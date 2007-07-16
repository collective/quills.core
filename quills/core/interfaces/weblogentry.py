# Zope3 imports
from zope.interface import Interface


class IReadWeblogEntry(Interface):
    """A weblog entry.
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
