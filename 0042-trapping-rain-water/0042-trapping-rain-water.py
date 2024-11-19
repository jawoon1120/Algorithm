class Solution:
    def trap(self, height: List[int]) -> int:
        # 포인터를 옮겨간다 
        
        # 1. 높으면 카운트 X
        # 2. 낮았으면 차이만큼 카운트
        # 3. 높아지면 그만
        stack = []
        volume = 0

        for i in range(len(height)):
            
            while stack and height[i] > height[stack[-1]]:
                
                top = stack.pop()
                # print(stack, top,i)
                if not len(stack):
                    break
                
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                # print( "DIST water :",distance, waters)
                volume += distance * waters

            stack.append(i)
            # print(stack)
        return volume

