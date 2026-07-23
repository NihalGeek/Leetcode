class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_water=0;
        int curr_water;
        int lp=0;
        int rp=height.size()-1;
        while(lp<rp){
            int wt=rp-lp;
            int ht=min(height[lp],height[rp]);
            curr_water=wt*ht;
            if(height[lp]<height[rp]){
                lp++;
            }
            else{
                rp--;
            }
            max_water=max(max_water,curr_water);
        }
        return max_water;
        
    }
};
