import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by mario.fernandez on 13/09/2017.
 */
public class VigenereDecrypter {

    private String cryptogram;
    private String filteredCryptogram;
    private Map<Integer, Queue<Character>> nonAlphabetical;
    private ArrayList<String > mostCommonSubstrings;
    private ArrayList<ArrayList<Integer>> possibleSizesDivisots;
    private int size;
    private ArrayList<String> possibleKeys;
    private ArrayList<String > decyphedTexts;
    private String key;
    private String decryptedText;

    public VigenereDecrypter(String cryptogram) {
        this.cryptogram = cryptogram;
    }

    public void run() {
        filterCryptogram();
        findMostCommonSubstrings();
        findPossibleSizes();
        findSize();
        generatePossibleKeys();
        computeDecyphedTexts();
        getAwnser();
    }

    private void filterCryptogram() {
        filteredCryptogram = "";
        nonAlphabetical = new HashMap<>();
        int j = 0;
        for (int i = 0; i < cryptogram.length(); ++i) {
            char c = cryptogram.charAt(i);
            if (Character.isAlphabetic(c)) {
                filteredCryptogram += c;
                ++j;
            }
            else {
                if (!nonAlphabetical.containsKey(j)) {
                    nonAlphabetical.put(j, new LinkedList<Character>());
                }
                nonAlphabetical.get(j).add(c);
            }
        }
    }

    private void findMostCommonSubstrings() {
        mostCommonSubstrings = new ArrayList<>();
        //TODO: Encontrar las 3 substrings mas comunes de mas de 3 letras

        Map<String, Integer> map = new HashMap<>();
        int limit = cryptogram.length() - 5 + 1;
        for (int i = 0; i < limit; i++) {
            String sub = cryptogram.substring(i, i + 5);
            Integer counter = map.get(sub);
            if (counter == null) {
                counter = 0;
            }
            map.put(sub, ++counter);
        }
        map = sortByValue(map);
        ArrayList<Map.Entry<String,Integer>> entries = new ArrayList<>(map.entrySet());
        int j = entries.size()-1;
        while ( j >= 0 && mostCommonSubstrings.size() < 1) {
            if (entries.get(j).getKey().length() >= 3 && onlyAlpha(entries.get(j).getKey())) {
                mostCommonSubstrings.add(entries.get(j).getKey());
            }
            --j;
        }
    }

    private boolean onlyAlpha(String word) {
        for (char c: word.toCharArray()) {
            if (!Character.isAlphabetic(c)) return false;
        }
        return true;
    }

    private Map<String, Integer> sortByValue(Map<String, Integer> unsortMap) {

        // 1. Convert Map to List of Map
        List<Map.Entry<String, Integer>> list =
                new LinkedList<Map.Entry<String, Integer>>(unsortMap.entrySet());

        // 2. Sort list with Collections.sort(), provide a custom Comparator
        //    Try switch the o1 o2 position for a different order
        Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
            public int compare(Map.Entry<String, Integer> o1,
                               Map.Entry<String, Integer> o2) {
                return (o1.getValue()).compareTo(o2.getValue());
            }
        });

        // 3. Loop the sorted list and put it into a new insertion order Map LinkedHashMap
        Map<String, Integer> sortedMap = new LinkedHashMap<String, Integer>();
        for (Map.Entry<String, Integer> entry : list) {
            sortedMap.put(entry.getKey(), entry.getValue());
        }

        /*
        //classic iterator example
        for (Iterator<Map.Entry<String, Integer>> it = list.iterator(); it.hasNext(); ) {
            Map.Entry<String, Integer> entry = it.next();
            sortedMap.put(entry.getKey(), entry.getValue());
        }*/


        return sortedMap;
    }

    private void findPossibleSizes() {
        possibleSizesDivisots = new ArrayList<>();
        for (int i = 0; i < mostCommonSubstrings.size(); ++i) {
            String commonSubstring = mostCommonSubstrings.get(i);
            ArrayList<Integer> divisors = new ArrayList<>();
            for (int j = -1; (j = filteredCryptogram.indexOf(commonSubstring, j + 1)) != -1; j++) {
                divisors.add(j);
            }
            possibleSizesDivisots.add(divisors);
        }
    }

    private void findSize() {
        Map<Integer, Integer> possibleSizes = new HashMap<>();
        for (ArrayList<Integer> divisors : possibleSizesDivisots) {
            int possibleSize = gcd(divisors);
            if (!possibleSizes.containsKey(possibleSize)) {
                possibleSizes.put(possibleSize, 1);
            }
            else {
                possibleSizes.put(possibleSize, possibleSizes.get(possibleSize) + 1);
            }
        }
        int max = -1;
        for (Map.Entry<Integer, Integer> x : possibleSizes.entrySet()) {
            if (x.getValue() > max) {
                size = x.getKey();
                max = x.getValue();
            }
        }
    }

    private int gcd(int a, int b) {
        while (b > 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    private int gcd(ArrayList<Integer> divisors) {
        int result = divisors.get(0);
        for(int i = 1; i < divisors.size(); i++) result = gcd(result, divisors.get(i));
        return result;
    }

    private void generatePossibleKeys() {
        possibleKeys = new ArrayList<>();
        char[] chars = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        char[] paraula = {'e','y','e','s'};

        iterate(chars, paraula, 4);
    }

    private void iterate(char[] chars, char[] build, int pos) {
        if (pos == size) {
            possibleKeys.add(new String(build));
            return;
        }

        for (int i = 0; i < chars.length; i++) {
            build[pos] = chars[i];
            iterate(chars, build, pos + 1);
        }
    }

    private void computeDecyphedTexts() {
        decyphedTexts = new ArrayList<>();
        for (int i = 0; i < possibleKeys.size(); ++i) {
            String possibleKey = possibleKeys.get(i);
            int actKeyChar = 0;
            String decryptedText = "";
            for (int j = 0; j < filteredCryptogram.length(); ++j) {
                char c = filteredCryptogram.charAt(j);
                if (nonAlphabetical.containsKey(j)) {
                    for (char x :  nonAlphabetical.get(j).toArray(new Character[0])) {
                        decryptedText += x;
                    }
                }
                char decryptedLetter;
                if (c >= 'A' && c <= 'Z') {
                    decryptedLetter = (char)(c - Character.toUpperCase(possibleKey.charAt(actKeyChar)) + 'A');
                    if (decryptedLetter < 'A') decryptedLetter = (char)(decryptedLetter + 26);
                }
                else {
                    decryptedLetter = (char)(c - possibleKey.charAt(actKeyChar) + 'a');
                    if (decryptedLetter < 'a') decryptedLetter = (char)(decryptedLetter + 26);
                }
                decryptedText += decryptedLetter;
                ++actKeyChar;
                if (actKeyChar >= possibleKey.length()) actKeyChar = 0;
            }
            if (nonAlphabetical.containsKey(filteredCryptogram.length())) {
                for (char x :  nonAlphabetical.get(filteredCryptogram.length()).toArray(new Character[0])) {
                    decryptedText += x;
                }
            }
            decyphedTexts.add(decryptedText);
            System.out.println(i + "/" + possibleKeys.size());
        }
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
        key = possibleKeys.get(numKey);
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

    public String getKey() {
        return key;
    }

}
