#!/usr/bin/python2
#
# A miner for F-Droid (https://f-droid.org/about/)
#
# Contributors:
#     Jeanderson Candido <http://jeandersonbc.github.io>
from xml.etree import ElementTree
from urllib import urlretrieve

class FDroidWrapper:

    def __init__(self):
        """ Constructor.
        Initializes this wrapper by fetching an index file from F-Droid server.
        This file contains all metadata about stored apps.
        """
        # URL retrieved from "get_apps" in "wp-fdroid.php"
        # It's a part of the fdroidserver implementation
        indexUrl = "https://f-droid.org/repo/index.xml"
        localPath = "f-droid-meta.xml"
        urlretrieve(indexUrl, localPath)
        self._indexDataXmlTree = ElementTree.parse(localPath);

    def showMetadataContent(self):
        """ Helper method to print XML content. """
        root = self._indexDataXmlTree.getroot()
        for child in root:
            print child.tag, child.attrib


if __name__ == "__main__":
    fdroid = FDroidWrapper()
    fdroid.showMetadataContent()
