# Local imports
from basecontent import IBaseContent

class ITopic(IBaseContent):
    """A keyword, with an optionally associated image, that knows how to find
    content tagged with it.
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
