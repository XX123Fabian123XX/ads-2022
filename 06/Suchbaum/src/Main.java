import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        //Task 3
        Tree<String> searchTree = new Tree<>(null);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Please choose an action");
        System.out.println("i: insert node");
        System.out.println("d: delete node");
        System.out.println("m: modify node");
        System.out.println("P: preorder");
        System.out.println("I: inorder");

        String[] arr = {"A", "B", "C", "a", "a", "b", "c", "z"};

        for(String a : arr) {
            searchTree.insert(a);
        }


        while(true) {
            System.out.println("\nPlease enter the action");
            String input = scanner.nextLine();
            if(input.equals("i")) {
                    System.out.println("Please enter the value to be entered");

                    String value = scanner.nextLine();
                    System.out.println(value);
                    searchTree.insert(value);
            }
            else if(input.equals("d")) {
                    System.out.println("Please enter the value to be entered");
                    String value = scanner.nextLine();
                    searchTree.delete(value);
            }
            else if(input.equals("m")) {
                    System.out.println("Please enter the key to be modified");
                    String oldString = scanner.nextLine();                   
                    System.out.println("Please enter the new key");
                    String newString = scanner.nextLine();
                    searchTree.modify(oldString, newString);
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

