# Zope3 imports
from zope.interface import Interface
from zope import schema


# Quills import
from basecontent import IBaseContent
from topic import ITopicContainer
from topic import IAuthorContainer
from archive import IWeblogArchive

from quills.core import QuillsCoreMessageFactory as _

class IReadWeblog(IWeblogArchive,
                  ITopicContainer,
                  IAuthorContainer,
                  IBaseContent):
    """
    """

    def getId():
        """Return the id of the weblog.
        """

    def getTitle():
        """Return the title of the weblog.
        """

    def hasEntry(id):
        """Return True if this IReadWeblog holds an entry with an id of `id',
        and False otherwise.
        """

    def getEntry(id):
        """Return the IWeblogEntry associated with `id', or None if there is no
        such entry.
        """

    def getEntries(maximum=None, offset=0):
        """Return a sequence of published IWeblogEntry instances, sorted by
        publishing date.  Only return a maximum of `maximum' (where None means
        no limit), and use `offset' to determine where in the full sequence the
        returned sequence starts from.
        """


class IWriteWeblog(Interface):
    """
    """

    def addEntry(title, excerpt, text, topics=[], id=None, pubdate=None, mimetype=None):
        """Add an entry from the provided arguments.  If id is None, normalize
        the title to create an id.  If pubdate is None, ignore it.
        If mimetype is None, use the default.
        Return the new entry.
        """

    def addFile(content, mimetype, id=None, title=''):
        """Add a file-ish object corresponding to `mimetype' that stores
        `content'.  If `id' is provided, use it for the file; otherwise generate
        a new (unique) id.  If `id' is not provided, try normalizing a provided
        `title' argument (if available) to create the id.
        Return the added object.
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

    def getWeblogContentObject():
        """Return the content object that can be adapted to IWeblog, and which
        this IWeblog represents.
        """


class IWeblogConfiguration(Interface):
    """
    """

    only_excerpt_in_weblog_view = schema.Bool(
        title=_(u'label_only_excerpt_in_weblog_view', default=u'Only excerpt in weblog view.'),
        description=_(u'help_only_excerpt_in_weblog_view', default=u'When enabled, show only the title and excerpt in the main weblog view.  If an entry has no excerpt, only its title will be displayed.'),
        default=False,
        )

    group_by_dates = schema.Bool(
        title=_(u'label_group_by_dates', default=u'Group by dates'),
        description=_(u'help_group_by_dates', default=u'When enabled, entries will be grouped under a header showing the date. Otherwise, the entries will be just be shown underneath eachother.'),
        default=True,
        )

    entries_per_page = schema.Int(
        title=_(u'label_entries_per_page', default=u'Entries Per Page'),
        description=_(u'help_entries_per_page', default=u'Select the number of weblog entries you would like to display on the front page and any other batched pages.'),
        default=20,
        )

    topic_images_in_weblog_view = schema.Bool(
        title=_(u'label_show_topic_images_in_weblog_view', default=u'Show Topic Images In Weblog View?'),
        description=_(u'help_show_topic_images_in_weblog_view', default=u'This controls the display of topic images in the weblog view.'),
        default=True,
        )

    trackback_enabled = schema.Bool(
        title=_(u'label_trackback_enabled', default=u'Enable the receiving of trackback pings?'),
        description=_(u'help_trackback_enabled', default=u'This controls whether trackback are enabled in the weblog'),
        default=False,
        )

    archive_format = schema.TextLine(
        title=_(u'label_archive_url_prefix', default=u'Archive URL prefix'),
        description=_(u'help_archive_url_prefix', default="Allows for (optionally) injecting a segment into archive URLs after the weblog segment. E.g. to have URLs like [weblog]/archive/2007/07/21/entry_id, enter 'archive' here."),
        default=u'',
        required=False,
        )
    
    show_about = schema.Bool(
        title=_(u"Show 'About' info"),
        description=_(u"If selected, the item creator and modification date will be shown."),
        default=True,
        )


class IWeblogLocator(Interface):
    """Find a weblog."""

    def find():
        """Some IWeblog implementing object or empty list is returned.
        """
