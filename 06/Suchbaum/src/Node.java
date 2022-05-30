
/**
 * A node for a tree
 */
public class Node<T> implements Comparable<Node<T>> {
    private T value;
    private Node<T> rightChild;
    private Node<T> leftChild;
    private Node<T> parent;

    
    public Node(T value) {
        this.value = value;
    }

    public void setParent(Node<T> parent) {
        this.parent = parent;
    }

    public Node<T> getParent() {
        return this.parent;
    }

    public Node<T> getRightChild() {
        return rightChild;
    }

    public void setRightChild(Node<T> rightChild) {
        if (rightChild != null) {
            rightChild.setParent(this);
        }

        this.rightChild = rightChild;
        
    }

    public Node<T> getLeftChild() {
        return leftChild;
    }
    
    public void setLeftChild(Node<T> leftChild) {
        if (leftChild != null ){
            leftChild.setParent(this);
        }

        this.leftChild = leftChild;
    }

    public void setValue(T value) {
        this.value = value;
    }

    public T getValue() {
        return this.value;
    }

    @Override
    public boolean equals(Object object) {
        if (object instanceof Node == false) return false;

        return this.value.equals(((Node)(object)).getValue());
    }

    @Override
    public String toString() {
        return this.value.toString();
    }

    public int compareTo(Node<T> node) {
        Integer first = (Integer) this.value;
        Integer second = (Integer) node.getValue();
        return first.compareTo(second);
    }

    public void printNode() {
        System.out.println("Nodevalue " + this.value );
        if (this.rightChild != null) {
            System.out.println("right child " + this.rightChild.value);
        }

        if (this.leftChild != null) {
            System.out.print("left child" + this.leftChild.value);
        }

        if (this.parent != null)
        System.out.println("Parentvalue" + this.parent.value);
    }
}
