#class for brakets task, slow but I solved it
class Solution:
    brackets_map = {
    ")": "(",
    "]": "[",
    "}": "{"
}

    def is_closed(element):
        return element in [")", "]", "}"]

    def isValid(self, s: str) -> bool:
        list_s_copy = ' '.join(s).split()
        if len(s) % 2 != 0 or s[0] in [")", "]", "}"]:
            return False


        for current_element in s:
            if Solution.is_closed(current_element):
                target_index = list_s_copy.index(current_element)
                if target_index == 0 and list_s_copy[target_index] in [")", "]", "}"]:
                    return False
                    
                if list_s_copy[target_index -1 ] != Solution.brackets_map[current_element]:
                    return False
                    
                del list_s_copy[target_index]
                del list_s_copy[target_index-1]
                
                
        if not list_s_copy:
            return True
        
        return False
        
