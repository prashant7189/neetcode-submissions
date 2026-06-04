class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        initial_pointer = 0
        final_pointer = len(s1)
        current_str = s2[:final_pointer]
        sorted_s1 = sorted(s1)

        for slider in range(final_pointer, len(s2)+1):
            if sorted_s1 == sorted(current_str):
                return True
            initial_pointer+=1
            final_pointer+=1
            current_str = s2[initial_pointer:final_pointer]
            slider+=1

        return False

        