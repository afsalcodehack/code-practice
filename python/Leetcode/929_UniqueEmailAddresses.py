from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        count = 0
        _map = set()

        for mail in emails:

            idx = mail.find('@')

            name = mail[0:idx]
            domain = mail[idx:]

            name = name.replace('.','').split('+')[0]

            if name+domain not in _map:
                count += 1
                _map.add(name+domain)
        print(_map)
        return count


driver = Solution()
print(driver.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(driver.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))