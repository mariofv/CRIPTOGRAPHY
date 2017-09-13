import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by mario.fernandez on 13/09/2017.
 */
public class EscitaloDecrypter {

    private String cryptogram;
    private ArrayList<String> decyphedTexts;
    private ArrayList<ArrayList<Integer>> dimensions;
    private ArrayList<Integer> key;
    private int r;

    private String decryptedText;

    public EscitaloDecrypter(String cryptogram) {
        this.cryptogram = cryptogram;
        dimensions = new ArrayList<>();
        decyphedTexts = new ArrayList<>();
        r = cryptogram.length();
    }

    public void run() {
        computeDecyphedTexts();
        getAwnser();
    }

    private void computeDecyphedTexts() {
        for (int i = 1; i < r; ++i) {
            for (int j = 1; j < r; ++j) {
                if (i*j == r) {
                    computeDecyphedText(i,j);
                }
            }
        }
    }

    private void computeDecyphedText(int i, int j) {
        int x, y;
        x = y = 0;
        ArrayList<Integer> dimension = new ArrayList<>(2);
        dimension.add(i);
        dimension.add(j);
        dimensions.add(dimension);
        char[][] matrix = new char[i][j];
        for (int k = 0; k < r; ++k) {
            matrix[x][y] = cryptogram.charAt(k);
            ++x;
            if (x == i) {
                x = 0;
                ++y;
            }
        }
        String decryptedText = "";
        for (x = 0; x < i; ++x) {
            for (y = 0; y < j; ++y) {
                decryptedText += matrix[x][y];
            }
        }
        decyphedTexts.add(decryptedText);
    }

    private void getAwnser() {
        int max = -1;
        int numKey = -1;
        for (int i = 0; i < decyphedTexts.size(); ++i) {
            int act = checkApperances(i);
            if (act > max) {
                numKey = i;
                max = act;
            }
        }
        key = dimensions.get(numKey);
        decryptedText = decyphedTexts.get(numKey);
    }

    private int checkApperances(int i) {
        int j = 0;
        String str = decyphedTexts.get(i).toLowerCase();
        Pattern p = Pattern.compile("the");
        Matcher m = p.matcher( str );
        while (m.find()) {
            j++;
        }
        return j; // Prints 2
    }

    public String getDecryptedText() {
        return decryptedText;
    }

    public ArrayList<Integer> getKey() {
        return key;
    }

}
