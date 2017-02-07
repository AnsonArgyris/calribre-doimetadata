import os
from calibre.customize import MetadataReaderPlugin

class doimetadata(MetadataReaderPlugin):

    name                = 'DOI Metadata' # Name of the plugin
    description         = 'Add Metadata to Books from their doi'
    supported_platforms = ['linux'] # Platforms this plugin will run on
    author              = 'Erich M. Wappis' # The author of this plugin
    version             = (0, 1, 0)   # The version number of this plugin
    file_types          = set(['epub', 'mobi']) # The file types that this plugin will be applied to
    on_postprocess      = True # Run this plugin after conversion is complete
    minimum_calibre_version = (0, 7, 53)
    can_be_disabled = True

    def run(self, path_to_ebook):
        from calibre.ebooks.metadata.meta import get_metadata, set_metadata
        file = open(path_to_ebook, 'r+b')
        ext  = os.path.splitext(path_to_ebook)[-1][1:].lower()
        mi = get_metadata(file, ext)
        mi.publisher = 'Hello World'
        set_metadata(file, mi, ext)
        return path_to_ebook

    def is_customizable(self):
        '''
        This method must return True to enable customization via
        Preferences->Plugins
        '''
        return False