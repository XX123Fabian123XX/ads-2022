
public class Tree<T> {
        private Node<T> rootNode;

        public Tree() {}

        public Tree(Node<T> rootNode) {
            this.rootNode = rootNode;
        }

        public static <T> Tree<T> bin(Tree<T> leftTree, Node<T> node, Tree<T> rightTree) {
            node.setLeftChild(leftTree.getRootNode());
            node.setRightChild(rightTree.getRootNode());
            return new Tree<T>(node);
        }

        public Tree<T> left() {
            if (this.rootNode == null || rootNode.getLeftChild() == null) return null;

            return new Tree<T>(this.rootNode.getLeftChild());
        }

        public Tree<T> right() {
            if (this.rootNode == null || rootNode.getRightChild() == null) return null;

            return new Tree<T>(this.rootNode.getRightChild());
        }

        public Node<T> value() {
            if (this.isEmpty()) System.out.println("root node is empty returning null");
            return rootNode;
        }

        public boolean isEmpty() {
            return rootNode == null;
        }

        public void setRootNode(Node<T> rootNode) {
            this.rootNode = rootNode;
        }

        public Node<T> getRootNode() {
            return this.rootNode;
        }

        @Override
        public boolean equals(Object object) {
            if (object == null) return false;
            if (object instanceof Tree == false) return false;

            Tree tree2 = (Tree) object;

            // check if the root nodes match
            if (this.rootNode.equals(tree2.getRootNode()) == false) return false;

            // check if the root nodes of both trees don't have anymore childs
            if (this.right() == null && this.left() == null && tree2.right() == null && tree2.left() == null) return true;

            // check if one tree has a right child and the other does not
            if ((this.right() == null && tree2.right() != null) || (this.right() != null && tree2.right() == null)) return false;

            // check if one tree has a left child and the other does not
            if ((this.left() == null && tree2.left() != null) || (this.left() != null && tree2.left() == null)) return false;

            // check recursively if the right and left tree trees match

            // if both have a right child -> they must equal
            if (this.right() != null && tree2.right() != null) {
                if (!this.right().equals(tree2.right())) return false;
            }
            // of both have a left child -> they must equal
            if (this.left() != null && tree2.left() != null) {
                if (!this.left().equals(tree2.left())) return false;
            }
            return true;

        }

        @Override
        public String toString() {
            return this.rootNode.toString();
        }
}
