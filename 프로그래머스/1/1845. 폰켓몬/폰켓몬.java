import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> result = new HashSet<>();
        
        for (int i=0; i<nums.length; i++) {
            result.add(nums[i]);
        }
        if (result.size() < (nums.length / 2)) {
            return result.size();
        }
        else {
            return nums.length / 2;
        }
    }
}