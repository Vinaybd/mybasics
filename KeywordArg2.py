#keyword arguments = an arguments preceded by an identifier\
#                    helps with readability
#                    order of arguments doesn't matter
#                    1.positional  2.default  3.keyword  4.arbitrary


def get_phone(country,area,first,last):
    return f"{country}--{area}--{first}--{last}"

phone_num =get_phone(country=1,area=123,last=7890,first=456)

print(phone_num)