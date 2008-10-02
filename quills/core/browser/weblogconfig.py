# Zope imports
from persistent.dict import PersistentDict
from zope.annotation.interfaces import IAnnotations
from zope.interface import implements
from zope.formlib import form

# Plone imports
from Products.statusmessages.interfaces import IStatusMessage

# Quills imports
from quills.core import QuillsCoreMessageFactory as _
from quills.core.interfaces import IWeblogConfiguration


ANNO_KEY = 'quills.core.weblogconfiguration'

# XXX These default values should be taken directly from the
# IWeblogViewConfiguration schema.
DEFAULT_VIEW_CONFIG = {
    'only_excerpt_in_weblog_view'   : False,
    'group_by_dates'                : True,
    'entries_per_page'              : 20,
    'topic_images_in_weblog_view'   : True,
    'trackback_enabled'             : False,
    'archive_format'                : '',
    'show_about'                    : True,
    }


class WeblogConfigAnnotations(object):
    """
    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IWeblogConfiguration, WeblogConfigAnnotations)
    True
    """

    implements(IWeblogConfiguration)

    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(self.context)
        self._config = annotations.setdefault(ANNO_KEY, PersistentDict())

    def _get_onlyExcerptInWeblogView(self):
        default = DEFAULT_VIEW_CONFIG['only_excerpt_in_weblog_view']
        return self._config.setdefault('only_excerpt_in_weblog_view', default)
    def _set_onlyExcerptInWeblogView(self, value):
        self._config['only_excerpt_in_weblog_view'] = value
    only_excerpt_in_weblog_view = property(_get_onlyExcerptInWeblogView,
                                           _set_onlyExcerptInWeblogView)

    def _get_groupByDates(self):
        default = DEFAULT_VIEW_CONFIG['group_by_dates']
        return self._config.setdefault('group_by_dates', default)
    def _set_groupByDates(self, value):
        self._config['group_by_dates'] = value
    group_by_dates = property(_get_groupByDates, _set_groupByDates)

    def _get_entriesPerPage(self):
        default = DEFAULT_VIEW_CONFIG['entries_per_page']
        return self._config.setdefault('entries_per_page', default)
    def _set_entriesPerPage(self, value):
        self._config['entries_per_page'] = value
    entries_per_page = property(_get_entriesPerPage, _set_entriesPerPage)

    def _get_showTopicImagesInWeblogView(self):
        default = DEFAULT_VIEW_CONFIG['topic_images_in_weblog_view']
        return self._config.setdefault('topic_images_in_weblog_view', default)
    def _set_showTopicImagesInWeblogView(self, value):
        self._config['topic_images_in_weblog_view'] = value
    topic_images_in_weblog_view = property(_get_showTopicImagesInWeblogView,
                                           _set_showTopicImagesInWeblogView)

    def _get_trackbackEnabled(self):
        default = DEFAULT_VIEW_CONFIG['trackback_enabled']
        return self._config.setdefault('trackback_enabled', default)
    def _set_trackbackEnabled(self, value):
        self._config['trackback_enabled'] = value
    trackback_enabled = property(_get_trackbackEnabled, _set_trackbackEnabled)

    def _get_archiveFormat(self):
        default = DEFAULT_VIEW_CONFIG['archive_format']
        return self._config.setdefault('archive_format', default)
    def _set_archiveFormat(self, value):
        self._config['archive_format'] = value
    archive_format = property(_get_archiveFormat, _set_archiveFormat)
    
    def _get_showAbout(self):
        default = DEFAULT_VIEW_CONFIG['show_about']
        return self._config.setdefault('show_about', default)
    def _set_showAbout(self, value):
        self._config['show_about'] = value
    show_about = property(_get_showAbout, _set_showAbout)


class WeblogConfigEditForm(form.EditForm):
    """Edit form for weblog view configuration.
    """

    form_fields = form.Fields(IWeblogConfiguration)
    label = u'Weblog View Configuration'

    def setUpWidgets(self, ignore_request=False):
        self.adapters = {}
        wvconfig = IWeblogConfiguration(self.context)
        self.widgets = form.setUpEditWidgets(
            self.form_fields, self.prefix, wvconfig, self.request,
            adapters=self.adapters, ignore_request=ignore_request
            )

    @form.action("submit")
    def submit(self, action, data):
        """
        """
        wvconfig = IWeblogConfiguration(self.context)
        form.applyChanges(wvconfig, self.form_fields, data)
        msg = _(u'Configuration saved.')
        IStatusMessage(self.request).addStatusMessage(msg, type='info')
