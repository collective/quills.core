# Zope3 imports
from zope.interface import Interface

from quills.core.interfaces.basecontent import IBaseContent


class IBaseView(IBaseContent):
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

    def isDiscussionAllowedFor(obj):
        """Check if discussion is allowed on obj, but in a way that can handle
        obj being a catalog brain.
        """

    def getCommentCountFor(obj):
        """Check how many discussion comments there are on obj, but in a way
        that can handle obj being a catalog brain.
        """


class IWeblogView(IBaseView):
    """An interface for a helper view.
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

    def getWeblogEntry():
        """
        """


class ITopicView(IWeblogView):
    """
    """

    def getLastModified():
        """Return the datetime for when the most recently modified IWeblogEntry
        in this topic was modified.
        """
