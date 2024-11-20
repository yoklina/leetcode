class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                answer -= 1
            else:
                answer += 1
        return answer
