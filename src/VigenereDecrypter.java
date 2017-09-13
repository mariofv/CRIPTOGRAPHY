import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by mario.fernandez on 13/09/2017.
 */
public class VigenereDecrypter {

    private String cryptogram;
    private String key;
    private String decryptedText;

    public VigenereDecrypter(String cryptogram) {
        this.cryptogram = cryptogram;
    }

    public void run() {
    }


    public String getDecryptedText() {
        return decryptedText;
    }

    public String getKey() {
        return key;
    }

}
