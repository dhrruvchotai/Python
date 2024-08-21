with (
    open('NewTemp.txt') as f1,
    open('High_Score.txt') as f2
):
    print(f"Data of file1: \n {f1.read()}\n file2: \n {f2.read()}")
