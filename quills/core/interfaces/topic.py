# Local imports
from basecontent import IBaseContent


class ITopic(IBaseContent):
    """A keyword, with an optionally associated image, that knows how to find
    content tagged with it.
    """

    def getId():
        """Return the keyword/id for this topic.
        """

    def getKeywords():
        """Return a sequence of keywords that this topic represents.
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

    def getEntries(maximum=None, offset=0):
        """Return a sequence of published IWeblogEntry instances, sorted by
        publishing date.  Only return a maximum of `maximum' (where None means no
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


class ITopicContainer(IBaseContent):
    """Represents a container for ITopic objects.
    """

    def getTopics():
        """Return a sequence of ITopic instances for this blog.
        """

    def getTopicById(id):
        """Return an ITopic instance corresponding to `id'.
        """


class IAuthorContainer(IBaseContent):
    """Represents a container for IAuthor objects.
    """

    def getAuthors():
        """Return a sequence of IAuthorTopic instances, one for every portal
        member id that has posted to this IWeblog.
        """

    def getAuthorById(id):
        """Return an IAuthorTopic instance for id.
        """
