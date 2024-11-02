
def generateParenthesis(n: int):
        def dfs(openP, closedP, s):
            #print(f"openP: {openP}, closedP: {closedP}, s:{s}")

            if len(s) == n * 2:
                res.append(s)
                #print(f"res: {res}\n")
                return 

            if openP < n:
                dfs(openP+1, closedP, s+'(')

            if closedP < openP:
                dfs(openP, closedP+1, s+')')

        res = []
        dfs(0, 0, '')
        return res

n = 3
print("\nn: ", n)
result = generateParenthesis(n)
print("result: ", result)

print("\n")