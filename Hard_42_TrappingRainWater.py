class Solution:
    def trap(self, height: List[int]) -> int:
        block = m_left= m_right =0
        
        for i in range(1,(len(height)-1)):
            m_left=max(height[:i])
            m_right=max(height[i+1:])
            if m_left > height[i] and m_right > height[i]:
                block = block + min(m_left,m_right) - height[i]
        return block