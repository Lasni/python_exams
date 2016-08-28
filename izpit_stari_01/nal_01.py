def transform_string(str1, str2):
    lst1 = list(str1)
    lst2_lower = list(str2.lower())
    lst2_upper = list(str2.upper())
    delimiters = " ,.!?"
    result = ""
    for i in lst1:
        if i in delimiters or i in lst2_lower or i in lst2_upper:
            result += i
        else:
            result += "*"
    return result


print(transform_string("Tra la la.", "ta"))