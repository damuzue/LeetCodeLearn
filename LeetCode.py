code13:
class Solution:
    def romanToInt(self, s: str) -> int:
        romandict = {"I":1, "V":5,"X":10, "L":50, "C":100,
         "D":500, "M":1000}
        romandict_div = {"IV":4 ,"IX": 9, "XL":40, "XC":90,
         "CD":400, "CM":900}
        total = 0
        for k in romandict_div.keys():
                if k in s:
                    total += romandict_div[k]
                    s = "".join(s.split(k))
        for m in s:
            if m in romandict:
                total += romandict[m]
        return total
        
        
code14:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        fir_str, length = strs[0], len(strs)
        for i in strs[1:]:
            fir_str = self.scp(fir_str, i)
            if not fir_str:
                break
        return fir_str
    
    def scp(self, str1, str2) -> str:
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

    
code20:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            elif ch in (')', ']', '}'):
                if stack == []:
                    return False
                temp = stack.pop()
                if not ((temp == '(' and ch == ')') or
                        (temp == '[' and ch == ']') or
                        (temp == '{' and ch == '}')):
                    return False
        return stack == []
    
code21:
    '''
    关于return L1的个人理解: 递归的核心在于,我只关注我这一层要干什么,返回什么,至于我的下一层(规模减1),我不管,我就是甩手掌柜.
好,现在我要merge L1,L2.我要怎么做?
    显然,如果L1空或L2空,我直接返回L1或L2就行,这很好理解.
    如果L1第一个元素小于L2的? 那我得把L1的这个元素放到最前面,至于后面的那串长啥样 ,我不管. 我只要接过下级员工干完活后给我的包裹, 然后把我干的活附上去(令L1->next = 这个包裹)就行
这个包裹是下级员工干的活,即merge(L1->next, L2)
    我该返回啥?
    现在不管我的下一层干了什么,又返回了什么给我, 我只要知道,假设我的工具人们都完成了任务, 那我的任务也就完成了,可以返回最终结果了
    最终结果就是我一开始接手的L1头结点+下级员工给我的大包裹,要一并交上去, 这样我的boss才能根据我给它的L1头节点往下找,检查我完成的工作
    自己理解的：https://github.com/damuzue/LeetCodeLearn/blob/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20230316103559.png
    '''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        elif l2 is None:
            return l1

        elif l1.val <= l2.val:
            # print(l1.val, "l1before")
            l1.next = self.mergeTwoLists(l1.next, l2)
            print(l1.val, l1.next.val,  "l1")
            return l1
        else:
            # print(l2.val, "l2before")
            l2.next = self.mergeTwoLists(l1, l2.next)
            print(l2.val, l2.next.val, "l2")
            return l2


l1 = ListNode(1, ListNode(2, ListNode(4, )))
l2 = ListNode(1, ListNode(3, ListNode(4, )))

s = Solution()
res = s.mergeTwoLists(l1, l2)

code26:
class Solution:
    def removeDuplicates(self, nums) -> int:
        slow, fast = 0, 1
        while fast <= len(nums) - 1:
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast] 
        return slow + 1

    
code27:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b
    
       
code35:
'''O(n)'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,v in enumerate(nums):
            if v >= target:
                return i
            elif v < target and i == len(nums) - 1:
                return i + 1
'''O(logn)二分法''' 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid_index = (right + left) // 2
            if target == nums[mid_index]:
                return mid_index
            elif target < nums[mid_index]:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return left
