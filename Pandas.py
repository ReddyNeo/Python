import pandas as pd
website={'Day':[1,2,3,4],'Visitors': [1001,4578,7465,2487],'Load':[10,50,68,42]}
wb=pd.DataFrame(website)
print(wb)
print(wb.head(2))
print(wb.tail(1))

