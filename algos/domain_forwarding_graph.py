# task
# https://app.codesignal.com/challenge/ZPDyptQjyTLdS3QR6
# Domain name forwarding lets GoDaddy domain owners automatically redirect their site visitors to a different site URL. Sometimes the visitors have to go through multiple redirects before ending up on the correct site.
#
# Using the DNS Manager, GoDaddy customers can view redirects in a simple visual format. One handy feature is the ability to group the domains by the final website they redirect to. Your task is to implement this feature.
#
# For the given redirects list, organize its domains into groups where for a specific group each domain eventually redirects visitors to the same website.
#
# Example
#
# For
#
# redirects = [["godaddy.net", "godaddy.com"],
#              ["godaddy.org", "godaddycares.com"],
#              ["godady.com", "godaddy.com"],
#              ["godaddy.ne", "godaddy.net"]]
#
# the output should be
#
# solution(redirects) = [["godaddy.com", "godaddy.ne", "godaddy.net", "godady.com"],
#                                ["godaddy.org", "godaddycares.com"]]
#
# In the first group, "godaddy.ne" redirects to "godaddy.net", which in turn redirects to "godaddy.com". "godady.com" redirects visitors to "godaddy.com" as well.
# In the second group, "godaddy.org" redirects visitors to "godaddycares.com".
#
# Note, that domains in each group are sorted lexicographically and groups themselves are sorted lexicographically by the domain they redirect to. So in the example, the first group goes before the second because "godaddy.com" is lexicographically smaller than "godaddycares.com".
#
# Input/Output
#
#     [execution time limit] 4 seconds (py3)
#
#     [input] array.array.string redirects
#
#     Each of redirects[i] consists of two domains. The second element is the domain to which the first element redirects. Each domain is a string that may consist of lowercase English letters, hyphens ('-') and full stops ('.').
#     It is guaranteed that domain redirects do not contain cycles, i.e. it is impossible to get back to the current site after any number of redirects. It is also guaranteed that each domain redirects to no more than one another domain, i.e. for each i ≠ j redirects[i][0] ≠ redirects[j][0].
#
#     Guaranteed constraints:
#     1 ≤ redirects.length ≤ 15,
#     redirects[i].length == 2,
#     1 ≤ redirects[i][j].length ≤ 25.
#
#     [output] array.array.string
#
#     Return the array of domain groups, such that each domain from redirects belongs to one of the group, and domains from one group redirect visitors to the same website. Arrange the domains in each group in lexicographical order, and sort the groups by the domains they redirect to (also lexicographically).
#
# [Python 3] Syntax Tips
#
# # Prints help message to the console
# # Returns a string
# def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name
#


from copy import copy
from typing import List, Tuple, Dict


def solution(redirects):
    mapping = create_mapping(redirects)
    entries = create_entries(redirects, copy(mapping))
    last_to_trace = create_last_to_trace(mapping, entries)
    return sorted([sorted(trace) for trace in last_to_trace.values()])


def create_mapping(redirects: List[Tuple[str, str]]) -> Dict[str, str]:
    return {entry: ending for entry, ending in redirects}


def create_entries(redirects: List[Tuple[str, str]], mapping: Dict[str, str]) -> List[str]:
    visited = set()
    acc = set()
    for entry, _ in redirects:
        if entry in visited:
            continue
        visited.add(entry)
        new_entry = entry
        while new_entry:
            temp_entry = mapping.get(new_entry)
            if new_entry in acc:
                acc.remove(new_entry)
            if temp_entry:
                visited.add(temp_entry)
            else:
                mapping[entry] = new_entry
            new_entry = temp_entry
        acc.add(entry)
    return acc


def create_last_to_trace(mapping: Dict[str, str], entries: List[str]) -> Dict[str, List[str]]:
    last_to_trace = {}
    for entry in entries:
        temp_trace = [entry]
        while entry:
            temp_entry = mapping.get(entry)
            if temp_entry:
                temp_trace.append(temp_entry)
            else:
                if entry in last_to_trace:
                    temp_trace = list(set([*temp_trace, *last_to_trace[entry]]))
                last_to_trace[entry] = temp_trace
            entry = temp_entry
    return last_to_trace


# redirects = [["godaddy.net", "godaddy.com"],
#              ["godaddy.org", "godaddycares.com"],
#              ["godady.com", "godaddy.com"],
#              ["godaddy.ne", "godaddy.net"]]
# print(solution(redirects))