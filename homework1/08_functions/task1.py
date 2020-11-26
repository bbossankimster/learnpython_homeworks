def get_summ(one, two, delimiter='&', upper_case=False):
    if upper_case:
        result = '{}{}{}'.format(str(one).upper(), str(delimiter), str(two).upper())       
    else:
        result = '{}{}{}'.format(str(one), str(delimiter), str(two))
    print(result)
get_summ("Learn", "python")
get_summ("Learn", "python", "&", 1)
print("Finish!")