"""
https://leetcode.com/problems/simplify-path/

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory,
so it can be ignored in a simplified path. Additionally, a double period ("..")
moves up a directory, so it cancels out whatever the last directory was. For
more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".


"""


class Solution(object):

    UP_DIR = ".."
    CURRENT_DIR = "."

    def simplifyPath(self, path: str) -> str:
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        simplified_path = []
        for directory in path:
            if len(directory) > 0:
                if directory == Solution.UP_DIR:
                    if len(simplified_path) > 0:
                        simplified_path.pop(-1)
                elif directory == Solution.CURRENT_DIR:
                    continue
                else:
                    simplified_path.append(directory)
        return "/" + "/".join(simplified_path)


if __name__ == "__main__":
    solution = Solution()

    path = "/home/"
    ans = "/home"
    assert solution.simplifyPath(path) == ans

    path = "/a/./b/../../c/"
    ans = "/c"
    assert solution.simplifyPath(path) == ans

    path = "/a/../../b/../c//.//"
    ans = "/c"
    assert solution.simplifyPath(path) == ans

    path = "/a//b////c/d//././/.."
    ans = "/a/b/c"
    assert solution.simplifyPath(path) == ans

