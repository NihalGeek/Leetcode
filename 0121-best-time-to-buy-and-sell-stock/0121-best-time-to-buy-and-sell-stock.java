class Solution {
    public int maxProfit(int[] prices) {
        int minpr=prices[0];
        int pro=0;
        for(int i=1;i<prices.length;i++){
            if(prices[i]<minpr){
                minpr=prices[i];
            }
            int profit=prices[i]-minpr;
            if(profit>pro){
                pro=profit;
            }
        }
        return pro;
    }
}