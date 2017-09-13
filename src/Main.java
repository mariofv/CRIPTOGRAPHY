import java.io.*;

/**
 * Created by mario.fernandez on 12/09/2017.
 */
public class Main {
    public static void main(String args[]) {
        String encryptredText;

        //CAESAR
//        encryptredText = read("data/2017_09_08_17_45_54_mario.fernandez.Cesar");
//        CaesarDecypher caesarDecrypter = new CaesarDecypher(encryptredText);
//        caesarDecrypter.run();
//        write("data/MarioFernandezVillalba_" + caesarDecrypter.getKey() + ".Cesar", caesarDecrypter.getDecyphedText());

        //ESCITALO
//        encryptredText = read("data/2017_09_08_17_45_54_mario.fernandez.Escitalo");
//        EscitaloDecrypter escitaloDecrypter = new EscitaloDecrypter(encryptredText);
//        escitaloDecrypter.run();
//        write("data/MarioFernandezVillalba_" + escitaloDecrypter.getKey().get(0) + 'x' + escitaloDecrypter.getKey().get(1) + ".Escitalo", escitaloDecrypter.getDecryptedText());

        //VIGENERE
        encryptredText = read("data/2017_09_08_17_45_54_mario.fernandez.Vigenere");
        VigenereDecrypter vigenereDecrypter = new VigenereDecrypter(encryptredText);
        vigenereDecrypter.run();
        write("data/MarioFernandezVillalba_" + vigenereDecrypter.getKey() + ".Vigenere", vigenereDecrypter.getDecryptedText());

    }

    private static void write(String fileName, String text) {
        try{
            PrintWriter writer = new PrintWriter(fileName, "UTF-8");
            writer.print(text);
            writer.close();
        } catch (IOException e) {
            // do something
        }
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
        String text = "";
        try {
            boolean first = true;
            while (!((line = bf.readLine()) == null)) {
                if (first) first = false;
                else text += '\n';
                text += line;
            }
            bf.close();
            return text;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}
