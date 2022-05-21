public class Main {
    public static void main(String args[]) {
        Tree<String> tree1 = new Tree<>(new Node<String>("tree1"));
        Tree<String> tree2 = new Tree<>(new Node<String>("tree2"));

        Tree<String> tree3 = new Tree<>(new Node<String>("tree3"));
        Tree<String> tree4 = new Tree<>(new Node<String>("tree3"));

        Tree<Integer> tree5 = new Tree<>(new Node<Integer>(100));
        Node<String> testNode = new Node<>("join Tree");

        Tree<String> joinedTree = Tree.<String>bin(tree1, testNode, tree2);


    }
}
