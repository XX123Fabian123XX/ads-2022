import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;



public class TreeAxiomsTest {
    private Tree<String> tree1;
    private Tree<String> tree2;
    private Node<String> testNode;

    @Before
    public void setup() {
        tree1 = new Tree<>(new Node<String>("tree1"));
        tree2 = new Tree<>(new Node<String>("tree2"));
        
        testNode = new Node<>("join Tree");
    }



    @Test
    public void leftTest() {
        Tree<String> joinedTree = Tree.<String>bin(tree1, testNode, tree2);
        assertTrue(joinedTree.left().equals(tree1));
    }

    @Test 
    public void rightTest() {
        Tree<String> joinedTree = Tree.<String>bin(tree1, testNode, tree2);
        assertTrue(joinedTree.right().equals(tree2));
    }   

    @Test
    public void valueTest() {
        Tree<String> joinedTree = Tree.<String>bin(tree1, testNode, tree2);
        assertTrue(joinedTree.value().equals(testNode));
    }

    @Test
    public void isEmptyTest1() {
        Tree<Integer> emptyTree = new Tree<>();

        assertEquals(true, emptyTree.isEmpty());
    }

    @Test
    public void isEmptyTest2() {
        Tree<String> joinedTree = Tree.<String>bin(tree1, testNode, tree2);
        assertFalse(joinedTree.isEmpty());
    }

}
