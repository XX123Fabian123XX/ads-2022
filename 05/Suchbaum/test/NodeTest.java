import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class NodeTest {
    
    @Test
    public void checkEquals1() {
        Node<String> node = new Node<>("test");
        Node<String> node2 = new Node<>("test");
        Node<String> node3 =new Node<>("123");

        assertEquals(true, node.equals(node2));
        assertEquals(false, node2.equals(node3));
    }

    @Test
    public void checkEquals2() {
        Node<Integer> node = new Node<>(123);
        Node<Integer> node2 = new Node<>(12345);
        Node<Integer> node3 = new Node<>(123);

        assertEquals(true, node.equals(node3));
        assertEquals(false, node2.equals(node3));
    }
}
