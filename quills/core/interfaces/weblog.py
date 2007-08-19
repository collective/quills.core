# Zope3 imports
from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory


class IReadWeblog(Interface):
    """
    """

    def getEntries(maximum=None, offset=0):
        """Return a sequence of published IWeblogEntry instances, sorted by
        publishing date.  Only return a maximum of `maximum' (where None means
        no limit), and use `offset' to determine where in the full sequence the
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

    def getDrafts(maximum=None, offset=0):
        """Return a sequence of unpublished IWeblogEntry instances, sorted by
        creation date.  Only return a maximum of `maximum' (where None means no
        limit), and use `offset' to determine where in the full sequence the
        returned sequence starts from.
        """

    def getAllEntries(maximum=None, offset=0):
        """Return a sequence all IWeblogEntry instances (published or not),
        sorted by publishing date.  Only return a maximum of `maximum' (where
        None means no limit), and use `offset' to offset where in the full
        sequence the returned sequence starts from.
        """

    def deleteEntry(entry_id):
        """Delete the IWeblogEntry corresponding to `entry_id'.
        """


class IWeblog(IReadWeblog, IWriteWeblog, IEditWeblog):
    """A weblog.
    """

_ = MessageFactory('quills')

class IWeblogConfiguration(Interface):
    """
    """

    onlyExcerptInWeblogView = schema.Bool(
        title=_(u'Only excerpt in weblog view.'),
        description=_(u'When enabled, show only the title and excerpt in the main weblog view.  If an entry has no excerpt, only its title will be displayed.'),
        default=False,
        )

    groupByDates = schema.Bool(
        title=_(u'Group by dates'),
        description=_('When enabled, entries will be grouped under a header showing the date. Otherwise, the entries will be just be shown underneath eachother.'),
        default=True,
        )

    entriesPerPage = schema.Int(
        title=_(u'Entries Per Page'),
        description=_('Select the number of weblog entries you would like to display on the front page and any other batched pages.'),
        default=20,
        )

    showTopicImagesInWeblogView = schema.Bool(
        title=_(u'Show Topic Images In Weblog View?'),
        description=_(u'This controls the display of topic images in the weblog view.'),
        default=True,
        )

    entriesPerPortlet = schema.Int(
        title=_(u'Entries Per Portlet'),
        description=_('Select the number of entries you would like to display in the various Quills portlets.'),
        default=5,
        )

    trackbackEnabled = schema.Bool(
        title=_(u'Enable the receiving of trackback pings?'),
        description=_(u'This controls whether trackback are enabled in the weblog'),
        default=False,
        )

    archiveFormat = schema.TextLine(
        title=_(u'Archive format'),
        description=_(u"""Allows for (optionally) injecting a segment into archive URLs after the weblog segment.
        e.g. To have URLs like [weblog]/archive/2007/07/21/entry_id, enter 'archive' here."""),
        default=u'',
        required=False,
        )
