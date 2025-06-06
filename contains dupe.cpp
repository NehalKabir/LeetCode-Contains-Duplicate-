#include <unordered_set>
#include <vector>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for (auto num:nums){
            if(seen.count(num)){
                return true;
            }
            else{
                seen.insert(num);
            }
        }

        return false;

    }
};
