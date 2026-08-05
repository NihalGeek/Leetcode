class Solution {
    public int[] sortedSquares(int[] nums) {
       int[] res = new int[nums.length];
       int i=0;
       int j=nums.length-1;
       int p=nums.length-1;
       while(i<=j){
        int sqi=nums[i]*nums[i];
        int sqj=nums[j]*nums[j];
        if(sqi>sqj){
            res[p]=sqi;
            i++;
        }
        else{
            res[p]=sqj;
            j--;
        }
        p--;
       } 
       return res;
    }
}