#Exporting DataFrame to HTML

# HTML Kya Hai?
# HTML (HyperText Markup Language) web pages banane ki language hai.

# Jab Pandas DataFrame ko HTML me convert karta hai, to wo data ko ek <table> ke form me convert kar deta hai.

# Example Data Frame:
# | Name    | Age |
# | ------- | --- |
# | Kshitij | 20  |
# | Rahul   | 21  |

#HTML:

# <table>
#   <tr>
#     <th>Name</th>
#     <th>Age</th>
#   </tr>

#   <tr>
#     <td>Kshitij</td>
#     <td>20</td>
#   </tr>

#   <tr>
#     <td>Rahul</td>
#     <td>21</td>
#   </tr>
# </table>

# Browser is HTML table ko normal table ki tarah dikha dega.

# Why Use HTML Export?
#1. Website Par Data Dikhane Ke Liye
#   Agar tum ML project ya dashboard bana rahe ho:
#   df.to_html()
#   Data directly webpage par show ho sakta hai.


# 2. Reports Generate Karne Ke Liye
# Kai companies HTML reports generate karti hain.
# Example:

# Sales Report
# Attendance Report
# Data Analysis Report

# 3. Email Reports
# Kai automated systems HTML table ko email me bhejte hain.