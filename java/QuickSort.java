import java.util.Random;

class QuickSort {
    public static void quickSort(int[] nums) {
        // shuffle
        shuffle(nums);
        quickSort(nums, 0, nums.length - 1);
    }

    private static void quickSort(int[] nums, int lo, int hi) {
        if (lo >= hi) return;
        int p = partition(nums, lo, hi);
        quickSort(nums, lo, p-1);
        quickSort(nums, p+1, hi);
    }

    private static int partition(int[] nums, int lo, int hi) {
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

    private static void shuffle(int[] nums) {
        Random rand = new Random();
        for (int i = 0; i < nums.length;i++) {
            int idx = i + rand.nextInt(nums.length - i);
            swap(nums, i, idx);
        }
    }

    private static void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
}