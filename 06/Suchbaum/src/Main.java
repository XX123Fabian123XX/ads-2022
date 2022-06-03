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


        // String[] strings = {"A","l" ,"f", "r", "B", "C", "D", "a"}; 

        // for(String s : strings) {
        //     searchTree.insert(s);
        // }

        // int[] randomNumbers = new int[500];

        // for(int i = 0; i < randomNumbers.length; i++) {
        //     randomNumbers[i] = (int) Math.floor(Math.random()*50000);
        //     searchTree.insert(randomNumbers[i] + "");
        // }

        // for(int i = 0; i < 20; i++) {
        //     searchTree.delete(randomNumbers[i] + "");
        // }

        // for(int i = 50; i < 80; i++) {
        //     searchTree.modify(randomNumbers[i] + "", Math.floor(Math.random() * 50) + "changed");
        // }



        while(true) {
            System.out.println("\nPlease enter the action");
            String input = scanner.nextLine();
            if(input.equals("i")) {
                    System.out.println("Please enter the value to be inserted");

                    String value = scanner.nextLine();

                    if (value.equals("")) continue;

                    searchTree.insert(value);
            }
            else if(input.equals("d")) {
                    System.out.println("Please enter the value to be deleted");
                    String value = scanner.nextLine();
                    System.out.println("das ist die value " + value);
                    if (value.equals("")) continue;

                    searchTree.delete(value);
            }
            else if(input.equals("m")) {
                    System.out.println("Please enter the key to be modified");
                    String oldString = scanner.nextLine();  
                    
                    if (oldString.equals("")) continue;

                    System.out.println("Please enter the new key");
                    String newString = scanner.nextLine();

                    if (newString.equals("")) continue;

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

