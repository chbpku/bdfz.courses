def tell_story(n):
    if n > 0:
        print("从前有座山，山上有座庙，庙里有个老和尚，他在讲：")
        tell_story(n - 1)
    else:
        print("讲完了！")


tell_story(10)

