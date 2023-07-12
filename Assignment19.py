q1>import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    dummy = ListNode()
    curr = dummy

    # Insert the first node from each linked list into the min-heap
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    # Merge the linked lists using the min-heap
    while heap:
        val, list_idx = heapq.heappop(heap)
        curr.next = ListNode(val)
        curr = curr.next

        if lists[list_idx]:
            heapq.heappush(heap, (lists[list_idx].val, list_idx))
            lists[list_idx] = lists[list_idx].next

    return dummy.next



q2>def mergeAndCount(left, right):
    left_len = len(left)
    right_len = len(right)
    left_index = right_index = count = 0
    merged = []

    while left_index < left_len and right_index < right_len:
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            count += left_len - left_index

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged, count

def mergeSortAndCount(nums):
    if len(nums) <= 1:
        return nums, 0

    mid = len(nums) // 2
    left, left_count = mergeSortAndCount(nums[:mid])
    right, right_count = mergeSortAndCount(nums[mid:])
    merged, merge_count = mergeAndCount(left, right)

    return merged, left_count + right_count + merge_count

def countSmaller(nums):
    _, counts = mergeSortAndCount(list(enumerate(nums)))
    return counts





q3>def merge(left, right):
    left_ptr = right_ptr = 0
    merged = []

    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] <= right[right_ptr]:
            merged.append(left[left_ptr])
            left_ptr += 1
        else:
            merged.append(right[right_ptr])
            right_ptr += 1

    merged.extend(left[left_ptr:])
    merged.extend(right[right_ptr:])

    return merged

def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left, right)

def sortArray(nums):
    return mergeSort(nums)





q4>def pushZerosToEnd(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] != 0:
            left += 1

        if nums[right] == 0:
            right -= 1

    return nums





q5>def rearrangeAlternate(nums):
    pos_ptr = 0
    neg_ptr = 0

    while pos_ptr < len(nums) and neg_ptr < len(nums):
        if nums[pos_ptr] >= 0:
            pos_ptr += 2
        elif nums[neg_ptr] < 0:
            neg_ptr += 1
        else:
            nums[pos_ptr], nums[neg_ptr] = nums[neg_ptr], nums[pos_ptr]
            pos_ptr += 2
            neg_ptr += 1

    return nums





q6>def mergeSortedArrays(arr1, arr2):
    ptr1 = ptr2 = 0
    result = []

    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] <= arr2[ptr2]:
            result.append(arr1[ptr1])
            ptr1 += 1
        else:
            result.append(arr2[ptr2])
            ptr2 += 1

    result.extend(arr1[ptr1:])
    result.extend(arr2[ptr2:])

    return result






q7>def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set()

    for num in nums2:
        if num in set1:
            set2.add(num)

    result = []
    for num in set2:
        result.append(num)

    return result





q8>from collections import Counter

def intersection(nums1, nums2):
    count1 = Counter(nums1)
    count2 = Counter(nums2)

    result = []
    for num in count1.keys() & count2.keys():
        result.extend([num] * min(count1[num], count2[num]))

    return result
