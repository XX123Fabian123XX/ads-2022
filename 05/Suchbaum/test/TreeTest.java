import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.Collection;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

@RunWith(Parameterized.class)
public class TreeTest {

    private Tree tree1;
    private Tree tree2;
    private boolean result;

    public TreeTest(boolean result, Tree tree1, Tree tree2) {
        this.tree1 = tree1;
        this.tree2 = tree2;
        this.result = result;
    }

    @Test
    public void equalsTest() {
        assertEquals(result, tree1.equals(tree2));
    }

    @Parameters
    public static Collection<Object[]> values() {
        Tree<String> tree1 = new Tree<>(new Node<String>("tree1"));
        Tree<String> tree2 = new Tree<>(new Node<String>("tree2"));

        Tree<String> tree3 = new Tree<>(new Node<String>("tree3"));
        Tree<String> tree4 = new Tree<>(new Node<String>("tree3"));

        Tree<Integer> tree5 = new Tree<>(new Node<Integer>(100));

        Tree<String> tree6 = new Tree<>(new Node<String>("test"));
        tree6.getRootNode().setLeftChild(new Node<String>("test"));

        Tree<String> tree7 = new Tree<>(new Node<String>("test"));
        tree7.getRootNode().setRightChild(new Node<String>("test"));

        Tree<String> tree8 = new Tree<>(new Node<String>("test"));
        tree8.getRootNode().setRightChild(new Node<String>("test"));

        Tree<String> tree9 = new Tree<>(new Node<String>("test"));
        tree9.getRootNode().setLeftChild(new Node<String>("test"));

        Tree<String> tree10 = new Tree<>(new Node<String>("test"));
        tree10.getRootNode().setLeftChild(new Node<String>("test"));
        tree10.getRootNode().setLeftChild(new Node<String>("test"));

        Tree<String> tree11 = new Tree<>(new Node<String>("test"));
        tree11.getRootNode().setLeftChild(new Node<String>("test"));
        tree11.getRootNode().setLeftChild(new Node<String>("test"));


        return Arrays.asList(new Object[][] {
            {false, tree1, tree2},
            {false, tree3, null},
            {false, tree3, tree1},
            {false, tree3, tree5},
            {false ,tree6, tree4},
            {false, tree7, tree4},
            {true, tree7, tree8},
            {true, tree6, tree9},
            {true, tree10, tree11}
        });
    }
}
