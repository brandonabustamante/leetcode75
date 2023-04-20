def isSubsequence(self, s: str, t: str) -> bool:

    i = 0
    j = 0
    s_size = len(s)
    t_size = len(t)

    if s_size == 0:
        return True

    if t_size == 0:
        return False

    while j < t_size:

        if s[i] == t[j]:
            i += 1

        j += 1

        if i == s_size:
            return True
    return False
