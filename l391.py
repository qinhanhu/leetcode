class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 1. caculate actual_area of given rectangles. if actual_area != expected_area, return False
        # 2. cnt end_points, if len(end_ponints) != 4 and end_points != expected_end_points(bot_lf, top_left, top_right, bot_right), return False
        
        minX = float('inf')
        minY = float('inf')
        maxX = -float('inf')
        maxY = -float('inf')
        actual_area = 0
        expected_area = 0
        end_points = set()
        for xi, yi, ai, bi in rectangles:
            minX = min(minX, xi)
            minY = min(minY, yi)
            maxX = max(maxX, ai)
            maxY = max(maxY, bi)

            actual_area += (bi - yi) * (ai - xi)
            p1, p2, p3, p4 = (xi, yi), (xi, bi), (ai, bi), (ai, yi)
            for p in [p1, p2, p3, p4]:
                if p not in end_points:
                    end_points.add(p)
                else:
                    end_points.remove(p)
        expected_area = (maxY - minY) * (maxX - minX)
        if actual_area != expected_area:
            return False
        if len(end_points) == 4:
            for p in [(minX, minY), (minX, maxY), (maxX, minY), (maxX, maxY)]:
                if p not in end_points:
                    return False
            return True
        return False
        
            
