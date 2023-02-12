import java.util.HashMap;

public class BinarySearch {
    public static int lowerBound(int[] nums, int value) {
        int left = 0;
        int right = nums.length;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == value) {
                right = mid;
            } else if (nums[mid] > value) {
                right = mid;
            } else if (nums[mid] < value) {
                left = mid + 1;
            }
        }
        return left;
    }

    public static int upperBound(int[] nums, int value) {
        int left = 0;
        int right = nums.length;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == value) {
                left = mid + 1;
            } else if (nums[mid] > value) {
                right = mid;
            } else if (nums[mid] < value) {
                left = mid + 1;
            }
        }
        return left;
    }

    public static void main(String args[]){
        int[] nums = new int[]{1, 2, 2, 3};
        System.out.println(lowerBound(nums, 2));
        System.out.println(upperBound(nums, 2));
        HashMap<Character, Integer> h1 = new HashMap<Character, Integer>();
    }

}
