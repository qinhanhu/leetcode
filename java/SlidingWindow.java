import java.util.HashMap;

public class SlidingWindow {
    public void slidingWindow(String s) {
        HashMap<Character, Integer> window = new HashMap<>();

        int left = 0, right = 0;
        while (right < s.length()) {
            // c is the char to add to window
            char c = s.charAt(right);
            right++;
            // update window here

            // debug here
            // System.out.println(window + " " + left + "" + right) ;

            while (/*window needs shrink*/true) {
                char d = s.charAt(left);
                left++;
                // update window
            }
        }
    }
}


