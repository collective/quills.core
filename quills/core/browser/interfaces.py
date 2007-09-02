# Zope3 imports
from zope.interface import Interface


class IBaseView(Interface):
    """Base Quills view.
    """

    def isWeblogContent(obj=None):
        """Return True if obj is one of the weblog content types in the sense of
        the interface it provides; False otherwise.
        If `obj' is None, then self.context is used.
        """

    def getArchiveURLFor(weblogentry):
        """Return an archive URL for the object represented by the IWeblogEntry.
        """

    def getArchivePathFor(weblogentry):
        """Return an archive path for the object represented by the
        IWeblogEntry.
        """

    def displayingOneEntry(context, weblogentry):
        """Return True if the absolute_url of context equals that for
        weblogentry; False otherwise.
        """


class IWeblogView(IBaseView):
    """An interface for a helper view.
    """

    def getWeblog():
        """Return an object that provides IWeblog for the object being viewed.
        """

    def getWeblogContent():
        """Return the content object that can be adapted to IWeblog for the
        object being viewed.
        """

    def getConfig():
        """Return an IWeblogViewConfiguration instance for the weblog.
        """

    def getWeblogEntriesDates(entries_dict):
        """Return a sorted list of dates for dict of entries.
        """

    def sortWeblogEntriesToDates(lazy_entries, resolution='day'):
        """Sort the lazy entries into a dictionary keyed on dates with values a
        lists of WeblogEntry (catalog brains) that were posted on those days.
        The default 'resolution' is 'day', meaning the returned dictionary
        will be keyed on individual days.  Other options are 'month' and 'year'.
        """


class IWeblogEntryView(IBaseView):
    """
    """

    def getWeblogEntryContent():
        """Return the content object that can be adapted to IWeblogEntry for the
        entry being viewed.
        """

    def getWeblogEntry():
        """Return an object that provides IWeblogEntry for the entry being
        viewed.
        """


class ITopicView(IWeblogView):
    """
    """

    def getLastModified():
        """Return the datetime for when the most recently modified IWeblogEntry
        in this topic was modified.
        """

    def absolute_url():
        """Return the absolute URL for this topic.
        """
