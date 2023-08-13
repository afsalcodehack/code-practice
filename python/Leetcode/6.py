class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows < 2:
            return s

        result = "";
        list=  {}
        index = 0;
        step = 1;
        count = 1;

        for i in range(numRows):
            list[i] = [];

        for i in s:
            count = count + 1;
            list[index].append(i);
            if step % 2 == 0:
                index = index - 1;
            else:
                index = index + 1;

            if count == numRows:
                step = step+1;
                count = 1;

        for i in range(numRows):
            result += ''.join(str(e) for e in list[i]);

        return result;



service = Solution();
print(service.convert("PAYPALISHIRING",3))

print(service.convert("AB",1))



# graph = {
# }
#
# adjLists = [ []]
#
# graph[0] = []
# graph[0].append(1)
# graph[0].append(2)
# graph[0].append(4)
# a = ''.join(str(e) for e in graph[0])
# print(a)
#
# for i in graph[0]:
#     print(i, end= " ")