# PROBLEM NUMBER: 929
# https://leetcode.com/problems/unique-email-addresses/
# 929. Unique Email Addresses
# DIFFICULTY: EASY
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # Approach:
        # - Split each email into local and domain parts using '@'.  
        # - In the local part:
        #   • Ignore everything after '+' (as per problem rule).  
        #   • Remove all '.' characters.  
        # - Recombine the cleaned local part with the domain to form the normalized email.  
        # - Store all normalized emails in a set to ensure uniqueness.  
        # - Return the count of unique emails.
        # Time: O(n * m), Space: O(n), where n = number of emails, m = average length of an email.
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)
        