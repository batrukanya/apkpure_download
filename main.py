import sys, getopt
import time
from selenium import webdriver

def usage():
    print('python main.py --PkgName <PkgName> --VersionCode <VersionCode>')

def getDownloadURL(PkgName,VersionCode):
    if len(VersionCode) == 0:
        return f'https://d.apkpure.com/b/APK/{PkgName}?version=latest'
    else:
        return f'https://d.apkpure.com/b/APK/{PkgName}?versionCode={VersionCode}'

def Download(url):
    # chrome obj
    path = 'chromedriver.exe'

    browser = webdriver.Chrome(path)
    browser.get(url)
    time.sleep(10000)
    browser.quit()

if __name__ == '__main__':
    PkgName = ""
    VersionCode = ""

    # read pkgname and versionCode from cmd
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:v:",
                                   ["PkgName=", "VersionCode="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--h'):
            usage()
            sys.exit()
        elif opt in ("-p", "--PkgName"):
            PkgName = arg
        elif opt in ("-c", "--VersionCode"):
            VersionCode = arg

    if len(PkgName) == 0:
        print('PkgName cannot be empty')
        sys.exit()
    downloadURL = getDownloadURL(PkgName, VersionCode)
    Download(downloadURL)

