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
        """
        """


class ITagCloudView(Interface):
    """
    """

    def getCloud(weblog=None):
        """For `weblog', or the nearest weblog, return a list of tuples containing the:
            - topic object
            - relative weight of the topic, 0.0 to 1.0
            - number of entries for that topic, since we already calculated it.
        Skip topics that have no entries.
        """

    def getClouds():
        """Return a list of dictionaries like:
            [ {'blog' : blog1, 'cloud' : cloud1},
              {'blog' : blog2, 'cloud' : cloud2},
              ...
             ]
        Where `cloud1' is the return value from self.getCloud(blog1), etc.
        """
