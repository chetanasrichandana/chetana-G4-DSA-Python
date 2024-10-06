class Solution:
    def find_tallest_pillars(pillars):
        pillars.sort(reverse = True)
        tallest_pillar = pillars[0]
        second_tallest_pillar = pillars[1]
        height_difference = tallest_pillar - second_tallest_pillar
        return height_difference
    
    pillars = [5, 10, 8, 7, 12]
    print(find_tallest_pillars(pillars))

