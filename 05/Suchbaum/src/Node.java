
/**
 * A node for a tree
 */
public class Node<T> {
    private T value;
    private Node<T> rightChild;
    private Node<T> leftChild;

    
    public Node(T value) {
        this.value = value;
    }

    public Node<T> getRightChild() {
        return rightChild;
    }

    public void setRightChild(Node<T> rightChild) {
        this.rightChild = rightChild;
    }

    public Node<T> getLeftChild() {
        return leftChild;
    }

    public void setLeftChild(Node<T> leftChild) {
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

}
