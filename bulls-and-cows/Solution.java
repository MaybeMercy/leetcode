public class Solution {
  public String getHint(String secret, String guess) {

        // get from internet
        if (secret == null || guess == null || secret.length() != guess.length()) {
            return "";
        }

        int countA = 0;
        int countB = 0;

        char[] arrA = secret.toCharArray();
        char[] arrB = guess.toCharArray();

        //求A的数量
        for (int i = 0; i < arrA.length; i++) {
            for (int j = 0; j < arrB.length; j++) {
                if (arrA[i] == ' ' || arrB[j] == ' ') {
                    continue;
                } else if (arrA[i] == arrB[j]) {
                    if (i == j) {
                        countA++;
                        arrA[i] = ' ';
                        arrB[j] = ' ';
                    }
                }
            }
        }

        //求B的数量
        for (int i = 0; i < arrA.length; i++) {
            for (int j = 0; j < arrB.length; j++) {
                if (arrA[i] == ' ' || arrB[j] == ' ') {
                    continue;
                } else if (arrA[i] == arrB[j]) {
                    countB++;
                    arrA[i] = ' ';
                    arrB[j] = ' ';ls
                }
            }
        }

        return String.valueOf(countA) + "A" + String.valueOf(countB) + "B";
    }
}
