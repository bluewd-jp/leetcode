/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 */

// @lc code=start
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut acc: Vec<i32> = vec![];
        for i in 0..nums.len() {
            let n = target - nums[i];
            if acc.contains(&n) {
                return vec![acc.iter().position(|x| x == &n).unwrap() as i32, i as i32];
            } else {
                acc.push(nums[i])
            }
        }
        return vec![];
    }
}
// @lc code=end
