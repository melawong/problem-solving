def max_area(height):
    max_area = 0
    start = 0
    end = len(height) - 1

    while start < end:
        length = min(height[start], height[end])
        width = end - start
        area = length * width
        print(area, height[start], height[end], length, width)
        max_area = max(max_area, area)

        if(height[start] < height[end]):
            start += 1
        else:
            end -= 1

    return max_area