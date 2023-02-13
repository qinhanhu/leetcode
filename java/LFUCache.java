import java.util.HashMap;
import java.util.LinkedHashSet;

class LFUCache {
    private int cap;
    private HashMap<Integer, Integer> key2val;
    private HashMap<Integer, Integer> key2freq;
    private HashMap<Integer, LinkedHashSet<Integer>> freq2keys;
    private int minFreq;

    public LFUCache(int capacity) {
        cap = capacity;
        minFreq = 0;
        key2val = new HashMap<>();
        key2freq = new HashMap<>();
        freq2keys = new HashMap<>();
    }

    public int get(int key) {
        if (!key2val.containsKey(key)) {
            return -1;
        }
        increaseFreq(key);
        return key2val.get(key);
    }

    public void put(int key, int value) {
        if (key2val.containsKey(key)) {
            key2val.put(key, value);
            increaseFreq(key);
            return;
        }
        if (key2val.size() == cap) {
            removeLFUKey();
        }
        addNew(key, value);
    }

    private void increaseFreq(int key) {
        int freq = key2freq.get(key);
        key2freq.put(key, freq+1);
        freq2keys.get(freq).remove(key);
        if (freq2keys.get(freq).isEmpty()) {
            freq2keys.remove(freq);
            if (freq == minFreq) {
                minFreq++;
            }
        }
        freq2keys.putIfAbsent(freq+1, new LinkedHashSet<>());
        freq2keys.get(freq+1).add(key);
    }

    private void removeLFUKey() {
        LinkedHashSet<Integer> keyList = freq2keys.get(minFreq);
        int deleteKey = keyList.iterator().next();
        keyList.remove(deleteKey);
        if (keyList.isEmpty()) {
            freq2keys.remove(minFreq);
        }
        key2freq.remove(deleteKey);
        key2val.remove(deleteKey);
    }

    private void addNew(int key, int value) {
        key2val.put(key,value);
        key2freq.put(key, 1);
        freq2keys.putIfAbsent(1, new LinkedHashSet<>());
        freq2keys.get(1).add(key);
        minFreq = 1;
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */