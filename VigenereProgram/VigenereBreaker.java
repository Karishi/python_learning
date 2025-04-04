import java.util.*;
import java.io.*;
import edu.duke.*;

public class VigenereBreaker {
    public String sliceString(String message, int whichSlice, int totalSlices) {
        String collated = "";
        for(int k = whichSlice; k<message.length(); k+=totalSlices){
            collated+=Character.toString(message.charAt(k));
        }
        return collated;
    }

    public int[] tryKeyLength(String encrypted, int klength, char mostCommon) {
        int[] key = new int[klength];
        CaesarCracker cracker = new CaesarCracker(mostCommon);
        for(int arrayLocation = 0; arrayLocation<klength; arrayLocation++){
            String slice = sliceString(encrypted,arrayLocation,klength);
            key[arrayLocation] = cracker.getKey(slice);
        }
        
        return key;
    }

    public void breakVigenere () {
        DirectoryResource dictionaryFileSet = new DirectoryResource();
        HashMap<String,HashSet<String>> languages = new HashMap<String,HashSet<String>>();
        for(File f : dictionaryFileSet.selectedFiles()){
            String languageName = f.getName();
            FileResource fr = new FileResource(f);
            languages.put(languageName,readDictionary(fr));
        }
        FileResource encodedFile = new FileResource();
        String fileContents = encodedFile.asString();
        // FileResource dictFR = new FileResource();
        // HashSet<String> dictionary = readDictionary(dictFR);
        // String decrypted = breakForLanguage(fileContents,dictionary);
        // System.out.println(decrypted.substring(0,200));
        breakForAllLangs(fileContents, languages);
    }
    
    public HashSet<String> readDictionary(FileResource fr){
        HashSet<String> hash = new HashSet<String>();
        for(String word : fr.lines()){
            hash.add(word.toLowerCase());
        }
        return hash;
    }
    
    public int countWords(String message,HashSet<String> dictionary){
        int count = 0;
        for(String word : message.split("\\W+")){
            if(dictionary.contains(word.toLowerCase())){
                count++;
            }
        }
        return count;
    }
    
    public String breakForLanguage(String encrypted, HashSet<String> dictionary){
        int bestKeyLength = 0;
        int maxRealWords = 0;
        for(int k = 1; k<=100; k++){
            int[] keyTry = tryKeyLength(encrypted, k, mostCommonCharIn(dictionary));
            VigenereCipher vc = new VigenereCipher(keyTry);
            String decrypted = vc.decrypt(encrypted);
            if(k==38){
                System.out.println("Words in 38: "+countWords(decrypted,dictionary)); 
            }
            if(countWords(decrypted,dictionary)>maxRealWords){
                bestKeyLength = k;
                maxRealWords = countWords(decrypted,dictionary);
            }
        }
        int[] bestKey = tryKeyLength(encrypted, bestKeyLength, mostCommonCharIn(dictionary));
        System.out.println("Best Key Length: "+bestKeyLength);
        System.out.println("Max real words: "+maxRealWords);
        VigenereCipher winningCipher = new VigenereCipher(bestKey);
        String decryption = winningCipher.decrypt(encrypted);
        return decryption;
    }
    
    public char mostCommonCharIn(HashSet<String> dictionary){
        HashMap<Character,Integer> letterCounts = new HashMap<Character,Integer>();
        
        for(String s: dictionary){
            for(int k = 0; k<s.length(); k++){
                char c = s.charAt(k);
                if(!letterCounts.keySet().contains(c)){
                    letterCounts.put(c,1);
                }
                else{
                    letterCounts.put(c,letterCounts.get(c)+1);
                }
            }
        }
        int max=0;
        char best = '!';
        for(char c : letterCounts.keySet()){
            if(letterCounts.get(c)>max){
                max = letterCounts.get(c);
                best = c;
            }
        }
        return best;
    }
    
    public void breakForAllLangs(String encrypted, HashMap<String,HashSet<String>> languages){
        String topLang = "";
        String bestResult = "";
        int max = 0;
        for(String lang : languages.keySet()){
            HashSet<String> dictionary = languages.get(lang);
            char mostCommonChar = mostCommonCharIn(dictionary);
            String decrypted = breakForLanguage(encrypted,dictionary);
            if(countWords(decrypted,dictionary)>max){
                topLang = lang;
                bestResult = decrypted;
                max = countWords(decrypted,dictionary);
            }
        }
        System.out.println(bestResult);
        System.out.println("The best-matching language was "+topLang);
    }
}
