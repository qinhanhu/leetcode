import java.util.HashMap;

class ListNode {
    public int key;
    public int val;
    public ListNode next;
    public ListNode pre;

    public ListNode(int key, int val){
        this.key = key;
        this.val = val;
    }
}

class DoubleLinkedList {
    private int size;
    private ListNode head = new ListNode(-1, -1);
    private ListNode tail = new ListNode(-1, -1);
    public DoubleLinkedList() {
        head.next = tail;
        tail.pre = head;
    }

    public void append(ListNode node) {
        tail.pre.next = node;
        node.pre = tail.pre;
        node.next = tail;
        tail.pre = node;
        size++;
    }

    public void remove(ListNode node) {
        node.pre.next = node.next;
        node.next.pre = node.pre;
        size--;
    }

    public ListNode popFirst() {
        ListNode node = head.next;
        if (node == tail) {
            return null;
        }
        remove(node);
        return node;
    }

    public int size() {
        return this.size;
    }

}

class LRUCache {
    private int capacity;
    private HashMap<Integer, ListNode> key2node = new HashMap<>();
    private DoubleLinkedList cache = new DoubleLinkedList();

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {
        if (!key2node.containsKey(key)) {
            return -1;
        }
        makeRecent(key);
        return key2node.get(key).val;

    }

    public void put(int key, int value) {
        if (key2node.containsKey(key)){
            removeKey(key);
        } else if (cache.size() == capacity) {
            popLRU();
        }
        addNew(key, value);
    }

    private void makeRecent(int key) {
        ListNode node = key2node.get(key);
        cache.remove(node);
        cache.append(node);
    }

    private void addNew(int key, int val) {
        ListNode node = new ListNode(key, val);
        cache.append(node);
        key2node.put(key, node);
    }

    private void removeKey(int key) {
        ListNode node = key2node.get(key);
        cache.remove(node);
        key2node.remove(key);
    }

    private void popLRU() {
        ListNode node = cache.popFirst();
        key2node.remove(node.key);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */