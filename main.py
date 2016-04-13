#!/usr/bin/python2
#
# A miner for F-Droid (https://f-droid.org/about/)
#
# Contributors:
#     Jeanderson Candido <http://jeandersonbc.github.io>
import os
import time

from xml.etree import ElementTree
from urllib import urlretrieve


class FileManager:
    def __init__(self):
        self._createOutputDir()

    def createDir(self, name):
        path = self._outputDir + os.sep + name + os.sep
        os.mkdir(path)
        return path

    def _createOutputDir(self, name="downloads", suffixId=0):
        try:
            name = name if suffixId == 0 else "%s-%s" %(name, str(suffixId))
            os.mkdir(name)
            self._outputDir = name
        except OSError:
            suffixId += 1
            self._createOutputDir(suffixId=suffixId)


class AppEntry:
    """ Represents data from a registered App """

    def __init__(self, entryId="", apkRef="", srcRef="", size="0"):
        self._id = entryId
        self._apkRef = apkRef
        self._srcRef = srcRef
        self._size = size

    def getId(self):
        return self._id

    def getApkRef(self):
        return self._apkRef

    def getSrcRef(self):
        return self._srcRef

    def getSize(self):
        return self._size

    def __str__(self):
        return "%s,%s,%s,%s" %(self._id, self._apkRef, self._srcRef, self._size)


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
        self._indexDataXmlTree = ElementTree.parse(localPath)
        self._fileManager = FileManager()

    def download(self, appData=AppEntry()):
        """ Downloads an app based on the given app entry """
        baseUrl = "http://f-droid.org/repo/"
        path = self._fileManager.createDir(appData.getId())
        urlretrieve(baseUrl + appData.getSrcRef(), path + appData.getSrcRef())
        urlretrieve(baseUrl + appData.getApkRef(), path + appData.getApkRef())

    def getAppsData(self, n=None):
        """ Returns a list of App data """
        root = self._indexDataXmlTree.getroot()
        data = []
        for xmlEntry in root.iter("application"):
            appId = xmlEntry.get("id").replace(".", "-")
            latestPkgRelease = xmlEntry.iter("package").next()
            try:
                appApkRef = latestPkgRelease.find("apkname").text
                appSrcRef = latestPkgRelease.find("srcname").text
                appSize = latestPkgRelease.find("size").text
                data.append(AppEntry(entryId=appId, apkRef=appApkRef, srcRef=appSrcRef, size=appSize))
            except AttributeError as error:
                print "Skipped app \"%s\" because a required attribute was not found." %(appId)
        return data


if __name__ == "__main__":
    fdroid = FDroidWrapper()
    apps = fdroid.getAppsData()
    for app in apps:
        fdroid.download(app)
        time.sleep(60)
