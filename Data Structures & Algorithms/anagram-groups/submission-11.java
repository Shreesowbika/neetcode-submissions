class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> seen=new HashMap<>();
        for (String item : strs){
            char[] sorted=item.toCharArray();
            Arrays.sort(sorted);
            String s=new String(sorted);                      
            seen.computeIfAbsent(s, k -> new ArrayList<>()).add(item);
        }
        return new ArrayList<>(seen.values()); 
    }
}
