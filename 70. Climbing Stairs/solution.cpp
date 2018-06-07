class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 1, temp;
        while(n--)
        {
            temp = a;
            a = b;
            b = temp + b;
        }
        return a;
    }
};
