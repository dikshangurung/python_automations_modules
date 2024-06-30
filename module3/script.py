# import re

# def parse_city_country(text):
#     # Pattern to capture city names with optional spaces until a comma or period
#     pattern = r"^([A-Z][a-zA-Z\s]*)(,)"
#     result = re.search(pattern, text)
    
#     if result is None:
#         return ""
#     # print(result.groups())
#     # print(len(result))
#     return result.group(1)  # Return the capturing group with the city name

# print(parse_city_country("Paris, France")) # should return Paris
# print(parse_city_country("Mumbai, India")) # should return Mumbai
# print(parse_city_country("Rio de Janeiro, Brazil")) # should return Rio de Janeiro
# print(parse_city_country("Tokyo! Japan"))  # result should be blank


