#MY Code

""" method = "w"
input_stocks = open("stocks.csv", 'r')
output_stocks = open("output_stocks.csv", method)

next(input_stocks)

output_stocks.write("Company Name,PE Ratio,PB Ratio")

method = "r+"

output_stocks = open("output_stocks.csv", method)

next(output_stocks)

for lines in input_stocks:
    data_splitted = lines.split(",")
    
    name = data_splitted[0]
    price = data_splitted[1]
    earnings_per_share = data_splitted[2]
    book_value = data_splitted[3]

    pe_ratio = round((int(price) / int(earnings_per_share)), 2)
    price_to_book_ratio = round((int(price) / int(book_value)), 2)

    output_stocks.write(f"\n{name},{str(pe_ratio)},{str(price_to_book_ratio)}")
    

input_stocks.close()
output_stocks.close() """






# Instructor's code

with open("stocks.csv", 'r') as s, open("output_stocks.csv", 'w') as u:
    # as s means "as stock" and as u means "as updated"

    next(s)

    u.write("Company Name,PE Ratio,PB Ratio")

    next(s)

    for lines in s:
        data_splitted = lines.split(",")
        
        name = data_splitted[0]
        price = data_splitted[1]
        earnings_per_share = data_splitted[2]
        book_value = data_splitted[3]

        pe_ratio = round((int(price) / int(earnings_per_share)), 2)
        price_to_book_ratio = round((int(price) / int(book_value)), 2)

        u.write(f"\n{name},{str(pe_ratio)},{str(price_to_book_ratio)}")