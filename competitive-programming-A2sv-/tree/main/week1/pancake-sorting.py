class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans, totalFlips = [], 0
        while arr:
            maxElem = max(arr)
            maxIdx = arr.index(maxElem)
            if arr[-1] == maxElem:
                arr.pop(-1)
                continue
            if arr[0] == maxElem:
                ans.append(len(arr))
                arr.reverse()
                arr.pop(-1)
                continue
            ans.append(maxIdx + 1)
            arr = arr[:maxIdx + 1][::-1] + arr[maxIdx + 1:]
        return ans