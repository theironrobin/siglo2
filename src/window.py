
from gi.repository import Gtk


@Gtk.Template(resource_path='/com/github/theironrobin/siglo/json/window.ui')
class Siglo2Window(Gtk.ApplicationWindow):
    __gtype_name__ = 'Siglo2Window'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'siglo2'
        self.props.version = "0.1.0"
        self.props.authors = ['alex']
        self.props.copyright = '2022 alex'
        self.props.logo_icon_name = 'com.github.theironrobin.siglo.json'
        self.props.modal = True
        self.set_transient_for(parent)
