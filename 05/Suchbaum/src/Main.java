import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Tree<String> tree1 = new Tree<>(new Node<String>("tree1"));
        Tree<String> tree2 = new Tree<>(new Node<String>("tree2"));

        Tree<String> tree3 = new Tree<>(new Node<String>("tree3"));
        Tree<String> tree4 = new Tree<>(new Node<String>("tree3"));

        Tree<Integer> tree5 = new Tree<>(new Node<Integer>(100));
        Node<String> testNode = new Node<>("join Tree");

        Tree<String> joinedTree = Tree.<String>bin(tree1, testNode, tree2);

        //Task 3
        Node<Integer> root = new Node<>(50);
        Tree<Integer> leftTree = new Tree<>(new Node<Integer>(25));
        Tree<Integer> rightTree = new Tree<>(new Node<Integer>(75));

        Tree<Integer> searchTree = Tree.<Integer>bin(leftTree, root, rightTree);
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please choose an action");
        System.out.println("i: insert node");
        System.out.println("d: delete node");
        System.out.println("m: modify node");
        System.out.println("P: preorder");
        System.out.println("I: inorder");
        searchTree.insert(13);
        searchTree.insert(10);
        searchTree.insert(37); // exclude for showing
        searchTree.insert(63);
        searchTree.insert(87);
        searchTree.insert(95);
        searchTree.insert(80);
        searchTree.insert(83);
        
        while(true) {
            System.out.println("\nPlease enter the action");
            String input = scanner.nextLine();
            if(input.equals("i")) {
                while(true) {
                    System.out.println("Please enter the value to be entered");
                    String value = scanner.nextLine();
                    int number;
                    try {
                        number = Integer.parseInt(value);
                        searchTree.insert(number);
                        break;
                    } catch(NumberFormatException e) {}
                }
            }
            else if(input.equals("d")) {
                while(true) {
                    System.out.println("Please enter the value to be entered");
                    String value = scanner.nextLine();
                    int number;
                    try {
                        number = Integer.parseInt(value);
                        searchTree.delete(number);
                        break;
                    } catch(NumberFormatException e) {}
                }
            }
            else if(input.equals("m")) {
                while(true) {
                    System.out.println("Please enter the key to be modified");
                    String oldString = scanner.nextLine();
                    int oldKey;
                    try {
                        oldKey = Integer.parseInt(oldString);
                        while(true) {
                            System.out.println("Please enter the new key");
                            String newString = scanner.nextLine();
                            int newKey;
                            try {
                                newKey = Integer.parseInt(newString);
                                searchTree.modify(oldKey, newKey);
                                break;
                            } catch(NumberFormatException e) {}
                        }
                        break;
                    } catch(NumberFormatException e) {}
                }
                
            }
            else if(input.equals("P")) {
                searchTree.preOrder();
            }
            else if(input.equals("I")) {
                searchTree.inOrder();
            }
            else if(input.equals(" ")) {
                break;
            }
        }
        scanner.close();
    }
}
