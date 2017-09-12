import java.io.*;

/**
 * Created by mario.fernandez on 12/09/2017.
 */
public class Main {
    public static void main(String args[]) {
        String encryptredText = read("2017_09_08_17_45_54_mario.fernandez.Cesar");
        CaesarDecypher caesarDecrypter = new CaesarDecypher(encryptredText);
        caesarDecrypter.run();
        caesarDecrypter.printTexts();
        System.out.println("La clau es " + caesarDecrypter.getKey());
        System.out.println("El text es " + caesarDecrypter.getDecyphedText());
    }

    private static String read(String path) {
        File file = new File(path);
        BufferedReader bf = null;
        try {
            bf = new BufferedReader(new FileReader(file));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        String line;
        try {
            line = bf.readLine();
            bf.close();
            return line;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}
