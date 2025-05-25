class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #the goal of the code is to see if there are any dupes in the nums array
        #we could use hashmap or sets to do this since it can track the number as a key 
        # and the number of times it occurs as the value
        #reason we choose a set over hashmap is that a set does not allow for dupes
        # so once it detects a dupe we can just end it there
        hashset = set()

        
        # use a for loop to iterate through the array
        for num in nums:
            #we want to see if the number at current index in the array is in the set or not
            #if it is then that means that there was a duplicate of the number at an earlier index and we can return true
            #return true means that there was a dupe
            if num in hashset:
                return True
            else:
                #if the number was not in the hashset then that means that it is not a dupe
                #since it is not a dupe we have to add it to the set 
                #that way if there was a dupe that occured later on 
                # the set would be able to recoginze it and return true in the if statement
                hashset.add(num)

        #at this point we have gone through the entire array and have not had any dupes
        #so we return false to signify there were no dupes
        return False
        
         