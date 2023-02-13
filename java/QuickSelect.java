import java.util.Random;

public class QuickSelect {
    public int findKthLargest(int[] nums, int k) {
        shuffle(nums);
        int lo = 0, hi = nums.length - 1;
        k = nums.length - k;
        while (lo <= hi) {
            int p = partition(nums, lo, hi);
            if (p == k) {
                return nums[p];
            } else if (p < k) {
                lo = p + 1;
            } else {
                hi = p - 1;
            }
        }
        return -1;
    }
    public int partition(int[] nums, int lo, int hi) {
        int pivot = nums[lo];
        int left = lo+1, right = hi;
        while (left <= right) {
            while (left < hi && nums[left] <= pivot) {
                left++;
            }
            while (right > lo && nums[right] > pivot) {
                right--;
            }
            if (left >= right) {
                break;
            }
            swap(nums, left, right);
        }
        swap(nums, lo, right);
        return right;
    }

    public void shuffle(int[] nums) {
        Random rand = new Random();
        for (int i = 0; i < nums.length;i++) {
            int idx = i + rand.nextInt(nums.length - i);
            swap(nums, i, idx);
        }
    }

    private void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
}
