class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoder = new StringBuilder();

        for (String str : strs) {
            encoder.append(str.length());
            encoder.append('#');
            encoder.append(str);
        }

        return encoder.toString();
    }

    public List<String> decode(String encoder) {
        List<String> arr = new ArrayList<>();

        int i = 0;

        while (i < encoder.length()) {
            int index = encoder.indexOf("#", i);
            int j = Integer.parseInt(encoder.substring(i, index));
            i = index + 1;
            String str = encoder.substring(i, i + j);
            arr.add(str);
            i += j;
        }

        return arr;
    }
}