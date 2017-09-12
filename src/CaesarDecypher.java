import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by mario.fernandez on 12/09/2017.
 */
public class CaesarDecypher {
    private String cryptogram;
    private String decyphedTexts[];
    private int key;
    private String decyphedText;

    public CaesarDecypher(String cryptogram) {
        this.cryptogram = cryptogram;
        decyphedTexts = new String[26];
    }

    public void run() {
        for (int i = 0; i <26; ++i) {
            decyphedTexts[i] = sumKey(i);
        }
        getAwnser();
    }

    private String sumKey(int key) {
        String result = "";
        for (int i = 0; i < cryptogram.length(); ++i) {
            char actualChar = cryptogram.charAt(i);
            if (Character.isAlphabetic(actualChar)) {
                int sum = actualChar + key;
                if ('a' <= actualChar && actualChar <= 'z') {
                    while (sum > 'z') {
                        sum -= 26;
                    }
                    result += ((char)sum);
                }
                else {
                    while (sum > 'Z') {
                        sum -= 26;
                    }
                    result += ((char)sum);
                }
            }
            else {
                result += actualChar;
            }
        }
        return result;
    }

    private void getAwnser() {
        int max = -1;
        for (int i = 0; i < 26; ++i) {
            int act = checkApperances(i);
            if (act > max) {
                key = i;
                max = act;
            }
        }
        decyphedText = decyphedTexts[key];
    }

    private int checkApperances(int i) {
        int j = 0;
        String str = decyphedTexts[i].toLowerCase();
        Pattern p = Pattern.compile("the");
        Matcher m = p.matcher( str );
        while (m.find()) {
            j++;
        }
        return j; // Prints 2
    }

    public String getDecyphedText() {
        return decyphedText;
    }

    public int getKey() {
        return key;
    }

    public void printTexts() {
        for (int i = 0; i < 26; ++i) {
           System.out.println(decyphedTexts[i]);
        }
    }
}
