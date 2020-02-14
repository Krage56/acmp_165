def main():
    arr = []
    arr_cross = [None]
    f = True
    n = m = 0
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    #arr_cross.append([0, 0, 1])
    count = 0
    x = y = 0
    while(f):
        if (arr[x][y] <= n) and (arr[x][y] <= m):
            arr_cross.append([x, y, 1])
            if arr_cross[-1][2] == 1:
                x += arr[x][y]
            else:
                y += arr[x][y]
                arr_cross.pop(-1)
        elif x <= n - 1:
            x += arr[x][y]
        elif y <= m - 1:
            y += arr[x][y]
        else:
            if (y == m - 1) and (x == n - 1):
                count += 1
            y = arr_cross[-1][1]
            x = arr_cross[-1][0]
        #f = len(arr_cross)
