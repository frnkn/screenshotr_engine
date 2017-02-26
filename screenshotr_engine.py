"""
Basic Requirement for the screenshotr engine is using Phantom JS.

It's installed via ubuntu package manager, details: http://phantomjs.org/build.html

sudo apt-get update
sudo apt-get install build-essential g++ flex bison gperf ruby perl \
  libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
  libpng-dev libjpeg-dev python libx11-dev libxext-dev


  git clone git://github.com/ariya/phantomjs.git
cd phantomjs
git checkout 2.1.1
git submodule init
git submodule update


python build.py
"""

"""
Todos:

Logging
Testing
Screenshot File Handling

"""


class ScreenshotrEngine(object):
    def __init__(self):
        pass

    def __str__(self):
        return u"ScreenshotrEngine"

    def main(self):
        print("Hello World!")

    def make_screenshot(self, url, breakpoint):
        pass
    
    def upload_screenshot_to_s3(self, screenshot, user_id):
        pass

    def save_screenshot_to_db(self, screenshot):
        pass


if __name__ == '__main__':
    se = ScreenshotrEngine()
    se.main()
    