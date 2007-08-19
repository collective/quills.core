from persistent.dict import PersistentDict
from zope.annotation.interfaces import IAnnotations
from zope.interface import implements
from zope.formlib import form
from quills.core.interfaces import IWeblogConfiguration
from Products.statusmessages.interfaces import IStatusMessage

ANNO_KEY = 'quills.core.weblogconfiguration'

# XXX These default values should be taken directly from the
# IWeblogViewConfiguration schema.
DEFAULT_VIEW_CONFIG = {
    'onlyExcerptInWeblogView'     : False,
    'groupByDates'                : True,
    'entriesPerPage'              : 20,
    'showTopicImagesInWeblogView' : True,
    'entriesPerPortlet'           : 5,
    'trackbackEnabled'            : False,
    'archiveFormat'               : '',
    }


class WeblogConfigAnnotations(object):
    """
    """

    implements(IWeblogConfiguration)

    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(self.context)
        self._config = annotations.get(ANNO_KEY, None)
        if self._config is None:
            self._config = PersistentDict(DEFAULT_VIEW_CONFIG.copy())
            annotations[ANNO_KEY] = self._config

    def _get_onlyExcerptInWeblogView(self):
        return self._config['onlyExcerptInWeblogView']
    def _set_onlyExcerptInWeblogView(self, value):
        self._config['onlyExcerptInWeblogView'] = value
    onlyExcerptInWeblogView = property(_get_onlyExcerptInWeblogView,
                                       _set_onlyExcerptInWeblogView)

    def _get_groupByDates(self):
        return self._config['groupByDates']
    def _set_groupByDates(self, value):
        self._config['groupByDates'] = value
    groupByDates = property(_get_groupByDates, _set_groupByDates)

    def _get_entriesPerPage(self):
        return self._config['entriesPerPage']
    def _set_entriesPerPage(self, value):
        self._config['entriesPerPage'] = value
    entriesPerPage = property(_get_entriesPerPage, _set_entriesPerPage)

    def _get_showTopicImagesInWeblogView(self):
        return self._config['showTopicImagesInWeblogView']
    def _set_showTopicImagesInWeblogView(self, value):
        self._config['showTopicImagesInWeblogView'] = value
    showTopicImagesInWeblogView = property(_get_showTopicImagesInWeblogView,
                                           _set_showTopicImagesInWeblogView)

    def _get_entriesPerPortlet(self):
        return self._config['entriesPerPortlet']
    def _set_entriesPerPortlet(self, value):
        self._config['entriesPerPortlet'] = value
    entriesPerPortlet = property(_get_entriesPerPortlet, _set_entriesPerPortlet)

    def _get_trackbackEnabled(self):
        return self._config['trackbackEnabled']
    def _set_trackbackEnabled(self, value):
        self._config['trackbackEnabled'] = value
    trackbackEnabled = property(_get_trackbackEnabled, _set_trackbackEnabled)

    def _get_archiveFormat(self):
        return self._config['archiveFormat']
    def _set_archiveFormat(self, value):
        self._config['archiveFormat'] = value
    archiveFormat = property(_get_archiveFormat, _set_archiveFormat)


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
        msg = 'Configuration saved.'
        IStatusMessage(self.request).addStatusMessage(msg, type='info')
