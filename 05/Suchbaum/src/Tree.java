
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

        private void preOrder(Node<T> node) {
            if(node == null) {
                return;
            }
            printDetails(node);
            preOrder(node.getLeftChild());
            preOrder(node.getRightChild());
        }

        /**
         * wrapper to start recursive function
         */
        public void preOrder() {
            preOrder(this.rootNode);
        }

        private void printDetails(Node<T> node) {
            System.out.print(node + "(" + getHeight(node) + "," + getBalance(node) + ") : ");
            System.out.print(node.getLeftChild() != null ? node.getLeftChild() + "(" + getHeight(node.getLeftChild()) + "," + getBalance(node.getLeftChild()) + "), " : "null,");
            System.out.print(node.getRightChild() != null ? node.getRightChild() + "(" + getHeight(node.getRightChild()) + "," + getBalance(node.getRightChild()) + ")\n" : "null\n");
        }

        private void inOrder(Node<T> node) {
            if(node == null)
                return;
            inOrder(node.getLeftChild());
            System.out.println(node);
            inOrder(node.getRightChild());
        }

        /**
         * wrapper to start recursive function
         */
        public void inOrder() {
            inOrder(this.rootNode);
        }

        private int getHeight(Node<T> node) {
            if(node == null) {
                return 0;
            }
            int leftTHeight = getHeight(node.getLeftChild());
            int rightTHeight = getHeight(node.getRightChild());
            return Math.max(leftTHeight, rightTHeight) + 1;
        }

        private int getBalance(Node<T> node) {
            return getHeight(node.getLeftChild()) - getHeight(node.getRightChild());
        }

        public void insert(T value) {
            Node<T> newNode = new Node<>(value);
            Node<T> node = this.rootNode;
            
            // if tree is empty (start with rootNode)
            if(this.isEmpty()) {
                this.rootNode = newNode;
                return;
            }
            // search for place to insert and insert it (not if key already existing)
            while(true) {
                if(node.compareTo(newNode) <= -1) {
                    if(node.getRightChild() == null) {
                        node.setRightChild(newNode);
                        return;
                    }
                    else {
                        node = node.getRightChild();
                    }
                }
                else if(node.compareTo(newNode) >= 1) {
                    if(node.getLeftChild() == null) {
                        node.setLeftChild(newNode);
                        return;
                    }
                    else {
                        node = node.getLeftChild();
                    }
                    
                }
                else {
                    System.out.println("Search Tree contains already node with this key!");
                    return;
                }
            } 
        }

        public void modify(T searchKey, T newKey) {
            Node<T> modifyNode = new Node<>(searchKey);
            Node<T> node = this.rootNode;

            // search for element to modify
            while(node != null && node.getValue() != modifyNode.getValue()) {
                if(node.compareTo(modifyNode) >= 1) {
                    node = node.getLeftChild();
                }
                else {
                    node = node.getRightChild();
                }
            }
            
            // element to modify was not found
            if(node == null) {
                return;
            }
            
            // modify element
            delete(node.getValue());
            modifyNode.setValue(newKey);
            insert(modifyNode.getValue());
        }

        public void delete(T key) {
            Node<T> deleteNode = new Node<>(key);
            Node<T> node = this.rootNode;
            Node<T> parent = null;

            // search for element to delete (save parent element)
            while(node != null && node.getValue() != deleteNode.getValue()) {
                parent = node;
                if(node.compareTo(deleteNode) >= 1) {
                    node = node.getLeftChild();
                }
                else {
                    node = node.getRightChild();
                }
            }

            // element to delete was not found
            if(node == null) {
                return;
            }
            
            // delete the selected element
            if(node.getLeftChild() == null || node.getRightChild() == null) {
                deleteNode(node, parent);
            }
            else {
                deleteNodeTwoChilds(node);
            }

        }

        /**
         * max one child available - get available child and set it a level higher
         */
        private void deleteNode(Node<T> node, Node<T> parent) {
            Node<T> child = node.getLeftChild() != null ? node.getLeftChild() : node.getRightChild();
          
            if (node == this.rootNode) {
              this.rootNode = child;
            } else if (node.compareTo(parent) >= 1) {
                parent.setRightChild(child);
            } else {
                parent.setLeftChild(child);
            }
        }

        /**
         * find minimum node of right childtree
         */
        private void deleteNodeTwoChilds(Node<T> node) {
            // Find minimum node of right childtree
            Node<T> newNode = node.getRightChild();
            Node<T> newNodeParent = node;
            while (newNode.getLeftChild() != null) {
                newNodeParent = newNode;
                newNode = newNode.getLeftChild();
            }
          
            // write new key to deleting element
            node.setValue(newNode.getValue());
          
            // replacing element was right child
            if (newNode.compareTo(node.getRightChild()) == 0) {
                node.setRightChild(newNode.getRightChild());
            }
            else {
                // if there is a subtree (only right) from minimum of right childtree
                newNodeParent.setLeftChild(newNode.getRightChild());
            }
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
