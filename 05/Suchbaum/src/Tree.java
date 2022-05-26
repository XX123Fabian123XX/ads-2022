
public class Tree<T> {
        private Node<T> rootNode;

        public Tree() {}

        public Tree(Node<T> rootNode) {
            this.rootNode = rootNode;
        }

        public static <T> Tree<T> bin(Tree<T> leftTree, Node<T> node, Tree<T> rightTree) {
            if (node == null) return null;

            if (leftTree == null) {
                node.setLeftChild(null);
            } else {
                node.setLeftChild(leftTree.getRootNode());
            }

            if (rightTree == null) {
                node.setRightChild(null);
            } else {
                node.setRightChild(rightTree.getRootNode());
            }

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

        private void preOrder(Tree<T> tree) {
            if(tree == null) {
                return;
            }
            printDetails(tree);
            preOrder(tree.left());
            preOrder(tree.right());
        }

        /**
         * wrapper to start recursive function
         */
        public void preOrder() {
            preOrder(this);
        }

        private void printDetails(Tree<T> tree) {
            System.out.print(tree.value() + "(" + getHeight(tree) + "," + getBalance(tree) + ") : ");
            System.out.print(tree.left() != null ? tree.left() + "(" + getHeight(tree.left()) + "," + getBalance(tree.left()) + "), " : "null,");
            System.out.print(tree.right() != null ? tree.right() + "(" + getHeight(tree.right()) + "," + getBalance(tree.right()) + ")\n" : "null\n");
        }

        private void inOrder(Tree<T> tree) {
            if(tree == null)
                return;
            inOrder(tree.left());
            printDetails(tree);
            inOrder(tree.right());
        }

        /**
         * wrapper to start recursive function
         */
        public void inOrder() {
            inOrder(this);
        }

        private int getHeight(Tree<T> tree) {
            if(tree == null || tree.value() == null) {
                return 0;
            }
            int leftTHeight = getHeight(tree.left());
            int rightTHeight = getHeight(tree.right());
            return Math.max(leftTHeight, rightTHeight) + 1;
        }

        private int getBalance(Tree<T> tree) {
            return getHeight(tree.left()) - getHeight(tree.right());
        }

        public void insert(T value) {
            Node<T> newNode = new Node<>(value);
            Tree<T> tree = this;
            
            // if tree is empty (start with rootNode)
            if(this.isEmpty()) {
                this.rootNode = newNode;
                return;
            }
            // search for place to insert and insert it (not if key already existing)
            while(true) {
                if(tree.value().compareTo(newNode) <= -1) {
                    if(tree.right() == null) {
                        tree.value().setRightChild(newNode);
                        return;
                    }
                    else {
                        tree = tree.right();
                    }
                }
                else if(tree.value().compareTo(newNode) >= 1) {
                    if(tree.left() == null) {
                        tree.value().setLeftChild(newNode);
                        return;
                    }
                    else {
                        tree = tree.left();
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
            Tree<T> tree = this;

            if(tree.value() == null) {
                return;
            }

            // search for element to modify
            while(tree != null && tree.value().getValue() != modifyNode.getValue()) {
                if(tree.value().compareTo(modifyNode) >= 1) {
                    tree = tree.left();
                }
                else {
                    tree = tree.right();
                }
            }
            
            // element to modify was not found
            if(tree == null) {
                return;
            }
            
            // modify element
            delete(tree.value().getValue());
            modifyNode.setValue(newKey);
            insert(modifyNode.getValue());
        }

        public void delete(T key) {
            Node<T> deleteNode = new Node<>(key);
            Tree<T> tree = this;
            Tree<T> parent = null;

            if(tree.value() == null) {
                return;
            }

            // search for element to delete (save parent element)
            while(tree != null && tree.value().getValue() != deleteNode.getValue()) {
                parent = tree;
                if(tree.value().compareTo(deleteNode) >= 1) {
                    tree = tree.left();
                }
                else {
                    tree = tree.right();
                }
            }

            // element to delete was not found
            if(tree == null) {
                return;
            }
            
            // delete the selected element
            if(tree.left() == null || tree.right() == null) {
                deleteNode(tree, parent);
            }
            else {
                deleteNodeTwoChilds(tree);
            }

        }

        /**
         * max one child available - get available child and set it a level higher
         */
        private void deleteNode(Tree<T> tree, Tree<T> parent) {
            Node<T> child = tree.left() != null ? tree.left().value() : (tree.right() != null ? tree.right().value() : null) ;
          
            if (tree.value() == this.rootNode) {
              this.rootNode = child;
            } else if (tree.value().compareTo(parent.value()) >= 1) {
                parent.value().setRightChild(child);
            } else {
                parent.value().setLeftChild(child);
            }
        }

        /**
         * find minimum node of right childtree
         */
        private void deleteNodeTwoChilds(Tree<T> tree) {
            // Find minimum node of right childtree
            Tree<T> newTree = tree.right();
            Tree<T> newTreeParent = tree;
            while (newTree.left() != null) {
                newTreeParent = newTree;
                newTree = newTree.left();
            }
          
            // write new key to deleting element
            tree.value().setValue(newTree.value().getValue());

            Node<T> node = newTree.right() != null ? newTree.right().value() : null;
            // replacing element was right child
            if (newTree.value().compareTo(tree.right().value()) == 0) {
                tree.value().setRightChild(node);
            }
            else {
                // if there is a subtree (only right) from minimum of right childtree
                newTreeParent.value().setLeftChild(node);
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
