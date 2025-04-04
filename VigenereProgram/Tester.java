
/**
 * Write a description of Tester here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
import edu.duke.*;
import java.util.*;

public class Tester {
    public void test(){
        // FileResource fr = new FileResource();
        // CaesarCipher cipher = new CaesarCipher(5);
        // CaesarCracker cracker = new CaesarCracker('e');
        // int key[] = {17,14,12,4};
        // VigenereCipher vc = new VigenereCipher(key);
        // String encryptedText = vc.encrypt(fr.asString());
        // System.out.println(encryptedText);
        // System.out.println(vc.decrypt(encryptedText));
        VigenereBreaker vb = new VigenereBreaker();
        vb.breakVigenere();
        // System.out.println(vb.sliceString("abcdefghijklm",3,5));
        // System.out.println(Arrays.toString(vb.tryKeyLength(fr.asString(),4,'e')));
    }
}
