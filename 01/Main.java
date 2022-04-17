import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
       
            Integer[] numberArray = readFirstLine();

            long startTime = System.currentTimeMillis();
            long maxSumme = 0;
            int von = 0, bis = 0, anzahlAdditionen = 0;

            for(int i = 0; i < numberArray.length; i++) {
                for(int j = i; j < numberArray.length; j++) {
                    int summe = 0;
                    for(int k = i; k <= j; k++) {
                        summe += numberArray[k];
                        anzahlAdditionen++;
                    }

                    if (summe > maxSumme) {
                        maxSumme = summe;
                        von = i;
                        bis = j;
                    }

                    
                }
            }

            System.out.println("Zeitmessung " +( System.currentTimeMillis() - startTime ) + " Millisekunden");
            System.out.println("das ist ein test");
            System.out.println("Max. Teilsumme " + maxSumme);
            System.out.println("erster Index " + von);
            System.out.println("zweiter Index " + bis);
            System.out.println("Anzahl Additionen " + anzahlAdditionen);
            
        }


    public static Path getFilePath() {
        Scanner scanner = new Scanner(System.in);
        Boolean isRunning = true;
        Path path;
        while(isRunning) {
            System.out.println("Bitte geben sie den Dateinamen ein!");
            String filename =  scanner.nextLine();
            path = Paths.get(filename);

            if (!Files.exists(path)) {
                System.out.println("Die Datei konnte nicht gefunden werden");

            }  else {
                scanner.close();
                return path;
            }
        }

        scanner.close();
        return null;
    }
    // liest die Datei ein
    // die Zahlen müssen in der ersten Zeile stehen und mit Kommas getrennt sein (ohne Leerzeichen)
    public static Integer[] readFirstLine() {

        try {
            String firstLine = Files.readAllLines(getFilePath()).get(0);
            
            String[] lineSplitStrings = firstLine.split(",");
            Integer[] lineSplitInteger = new Integer[lineSplitStrings.length];

            for(int i = 0; i < lineSplitStrings.length; i++) {
                lineSplitInteger[i] = Integer.parseInt(lineSplitStrings[i]);
            }

            return lineSplitInteger;

        } catch(Exception exception) {
            System.out.println(exception.getMessage());
            return null;
        }
    }
}