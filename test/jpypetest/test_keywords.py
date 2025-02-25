# *****************************************************************************
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   See NOTICE file for details.
#
# *****************************************************************************
import jpype
import common
import keyword


class KeywordsTestCase(common.JPypeTestCase):
    def setUp(self):
        common.JPypeTestCase.setUp(self)

    def testKeywords(self):
        for kw in keyword.kwlist:
            safe = jpype._pykeywords.pysafe(kw)
            if kw.startswith("_"):
                continue
            self.assertEqual(type(safe), str, "Fail on keyword %s" % kw)
            self.assertTrue(safe.endswith("_"))
        self.assertEqual(jpype._pykeywords.pysafe("__del__"), None)
