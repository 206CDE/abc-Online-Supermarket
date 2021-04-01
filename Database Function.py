from github import Github
import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect(
  host = "127.0.0.1",
  user = "Manager",
  password = "E79G3T07J2",
  database = "abc supermarket database"
)
CUR = DB.cursor() 



app = Flask(__name__)

           
@app.route("/send_job_request", methods = ['POST'])
def send_job_request():
  name  = str(request.form['name'])
  tel   = str(request.form['tel'])
  email = str(request.form['email'])
  job   = str(request.form['job'])
  date  = str(datetime.datetime.now())
  if job == "Driver":
    job_id = '101'
  elif job == "Deliveryman":
    job_id = '102'
  elif job == "Checker":
    job_id = '103'
  elif job == "Sale Assistant (part time)":
    job_id = '201'
  elif job == "Sale Assistant (full time)":
    job_id = '202'
  elif job == "Senior Sale Assistant":
    job_id = '203'
  elif job == "Loader":
    job_id = '301'
  elif job == "Warehouseman":
    job_id = '302'
  elif job == "Production Operative":
    job_id = '303'
    
  #Send job request to database
  CUR.execute("""INSERT INTO job_apply (Applicant_Name, Telephone, Email, Job_Name, Job_ID, Apply_Date)
                 VALUES ('""" + name + """','""" + tel + """','""" + email + """','""" + job + """','""" + job_id + """','""" + date + """')""")
  DB.commit()
  
  #Once data send to database, go back to the recent html page
  return """<html><body>
              <script>
                alert('Your request has been successfully sent!');
                window.history.back()
              </script>
            </body></html>"""

    

@app.route("/member_register", methods = ['POST'])
def member_register():
  fname    = str(request.form['fname'])
  lname    = str(request.form['lname'])
  uname    = str(request.form['uname'])
  password = str(request.form['_password']) 
  DoB      = str(request.form['DoB'])
  Reg_Date = str(datetime.datetime.now())
  age      = str(request.form['age'])
  
  if float(age) > 65:
    Discount = '10%'
  else:
    Discount = '5%'

  try:
    #Send register data to database
    CUR.execute("""INSERT INTO member (First_Name, Last_Name, `User_Name(email)`, Password, Date_of_Birth, Register_Date, Discount)
                     VALUES ('""" + fname + """','""" + lname + """','""" + uname + """','""" + password + """','""" + DoB + """','""" + Reg_Date + """','""" + Discount + """')""")
    DB.commit()
 
    #Once data send to database, go back to the recent html page   
    return """<html><body>
                <script>
                  alert('You have successfully register as a member!');
                  window.history.back()
                </script>
              </body></html>"""

  except:
    #If error exist, it means the user has enter an existed user name
    return """<html><body>
                <script>
                  alert('This user name already exists');
                  window.history.back()
                </script>
              </body></html>"""



@app.route("/send_order", methods = ['POST'])
def send_order():
  CUR.execute("""SELECT COUNT(Order_ID) FROM `order`""")
  order_id = CUR.fetchone()
  order_id = str(order_id).replace('(', '')
  order_id = str(order_id).replace(')', '')
  order_id = str(order_id).replace(',', '')
  order_id = str(int(order_id) + 1)
  DB.commit()

  product_list   = str(request.form['product_list']).split(",")
  quantity_list  = str(request.form['quantity_list']).split(",")
  order_product  = ""
  for a in range(len(product_list)):
    order_product = order_product + product_list[a] + " x" + quantity_list[a] + ", "

  title          = str(request.form['title'])
  nickname       = str(request.form['nickname'])
  phone_number   = str(request.form['phone_number'])
  address_name   = str(request.form['address_name'])
  floor          = str(request.form['floor'])
  flat           = str(request.form['flat'])
  block_building = str(request.form['block_building'])
  estate_street  = str(request.form['estate_street'])
  district       = str(request.form['district'])
  region         = str(request.form['region'])
  pay_method     = str(request.form['pay_method'])
  
  try:
    credit_card  = str(request.form['credit_card'])
  except:
    credit_card  = ""

  product_price  = str(request.form['product_price_input'])
  shipping_price = str(request.form['shipping_price_input'])
  discount       = "0%"
  total_price    = str(request.form['total_price_input'])
  
  try:
    #Send order to database
    CUR.execute("""INSERT INTO `order`
               (Order_ID, Order_Product, Title, Name, Phone_No, Address_Name, Floor, Flat ,`Block/Building`,
                `Estate/Street`, District, Region, Payment_Method, Credit_C_Type,
                Product_Price, Shipping_Price, Discount, Total_Price)
                VALUES ('""" + order_id + """','""" + order_product + """','""" 
                + title + """','""" + nickname + """','"""
                + phone_number + """','""" + address_name + """','"""
                + floor + """','""" + flat + """','"""
                + block_building + """','""" + estate_street + """','"""
                + district + """','""" + region + """','"""
                + pay_method + """','""" + credit_card + """','"""
                + product_price + """','""" + shipping_price + """','"""
                + discount + """','""" + total_price + """')""")
    DB.commit()

    #Change Product_Stock and Total_Sale data base on Product_Name in database
    for a in range(len(product_list)):
      product_name = product_list[a]
      
      CUR.execute("""SELECT Product_Stock FROM `product` WHERE Product_Name = '""" + product_name + """'""")
      old_product_quantity = CUR.fetchone()
      old_product_quantity = str(old_product_quantity).replace('(', '')
      old_product_quantity = str(old_product_quantity).replace(')', '')
      old_product_quantity = str(old_product_quantity).replace(',', '')
      new_product_quantity = str(int(old_product_quantity) - int(quantity_list[a]))
      DB.commit()
           
      CUR.execute("""UPDATE product SET Product_Stock = '""" + new_product_quantity + """' WHERE Product_Name = '""" + product_name + """'""")
      DB.commit()

      CUR.execute("""SELECT Product_Total_Sale FROM `product` WHERE Product_Name = '""" + product_name + """'""")
      old_total_sale = CUR.fetchone()
      old_total_sale = str(old_total_sale).replace('(', '')
      old_total_sale = str(old_total_sale).replace(')', '')
      old_total_sale = str(old_total_sale).replace(',', '')
      new_total_sale = str(int(old_total_sale) + int(quantity_list[a]))
      DB.commit()
      
      CUR.execute("""UPDATE product SET Product_Total_Sale = '""" + new_total_sale + """' WHERE Product_Name = '""" + product_name + """'""")
      DB.commit()
      
    #Once data send to database, go back to the main html page
    return """<html><body>
                <script>
                  //Remove all product in shopping cart once the order has sent
                  alert("Your order has been successfully sent!");
                  window.history.go(-3);
                </script>
              </body></html>"""
  
  except:
    return """<html><body>
                <script>
                  alert('Sorry, we have some problem sending your order!');
                  window.history.go(-3);
                </script>
              </body></html>"""


@app.route("/forget_password", methods = ['POST'])
def forget_password():
  email = str(request.form['email'])

  if email != "":
    CUR.execute("""SELECT `User_Name(email)` FROM member WHERE `User_Name(email)` = '""" + email + """'""")
    email_result = CUR.fetchone()
    email_result = str(email_result).replace('(', '')
    email_result = str(email_result).replace(')', '')
    email_result = str(email_result).replace(',', '')
    DB.commit()

    if email_result != "None":
      CUR.execute("""INSERT INTO password_find(Email)
                    VALUES('""" + email + """')""")
      DB.commit()
      return """<html><body>
                  <script>
                    alert("We will send you a email soon to let you reset your password!")
                    window.history.back();
                  </script>
                </body></html>"""
    
    else: #No user name found in database
      return """<html><body>
                  <script>
                    alert("Sorry, we cannot find this user name!")
                    window.history.back();
                  </script>
              </body></html>"""
      
  else: #User cancel the find password process
    return """<html><body>
                <script>
                  window.history.back();
                </script>
              </body></html>"""

  
@app.route("/login", methods = ['POST'])
def login():
  user_name = str(request.form['user_name'])
  password  = str(request.form['password'])

  #Check if username and password correct/match
  CUR.execute("""SELECT `User_Name(email)` FROM member
                 WHERE `User_Name(email)` = '""" + user_name + """' AND
                 Password = '""" + password + """'""")
  result = CUR.fetchone()
  result = str(result).replace('(', '')
  result = str(result).replace(')', '')
  result = str(result).replace(',', '') 
  DB.commit()
  
  #Username and password match
  if result != "None":
    #Get user last name
    CUR.execute("""SELECT Last_Name FROM member
                 WHERE `User_Name(email)` = '""" + user_name + """'""")
    global lname
    lname = CUR.fetchone()
    lname = str(lname).replace('(', '')
    lname = str(lname).replace(')', '')
    lname = str(lname).replace(',', '') 
    DB.commit()
    
    replace_location = """<!-- Login function -->
<button class="login-btn" onclick="document.getElementById('login_form').style.display='block'"><h1><b>Login</b></h1></button>
<div id="login_form" class="modal">
  <form class="modal-content animate" action="http://localhost:5000/login" method="post">
    <div class="imgcontainer">
      <span onclick="document.getElementById('login_form').style.display='none'" class="close" title="Close Modal">&times;</span>
      <img src="Image/Background Logo/Login Logo.png" alt="User" class="user">
    </div>

    <div class="login_container">
      <div class="label_font_size">
      <label><b>Username</b></label>
        <i>
          <input type="text" placeholder=" Enter your username" name="user_name" id="user_name" autocomplete="off" required>
        </i>
      </div>

      <p class="label_font_size">
      <label><b>Password</b></label>
        <i>
          <input type="password" placeholder=" Enter your password" name="password" id="password" required>
        </i>
      </p>

      <p>
        <b><input type="submit" class="inside-login_btn" value="Login"></b>
      </p>

      <br>
      <br>
       
    </div> 

      <div class="down_container">
        <pre style="line-height: 18px">    
       <a href="abc Online Supermarket - Register Page.html" style="color: blue; font-size: 18px">Sign Up</a>                                <a href="abc Online Supermarket - Find Password.html" style="color: black; cursor: pointer; font-size: 18px">Forget Password?</a>
        </pre> 
        <br>      
      </div>     
  </form>
</div>"""
    replace_new_value = """<!-- Logout function -->
  <div>
  <div style="position: absolute; top: 30px; left: 1100px; text-align: center; font-size: 30px"><b>Welcome Back!</b>
    <div style="margin-top: -10px; color: blue"><h3><b><i>""" + lname.replace("'", "") + """</i></b></h3></div>
  </div>

  <form action="http://localhost:5000/logout">
     <input type="image" src="Image/Button Logo/Logout Logo.png" alt="Logout Logo"
     style="position: absolute; top: 5px; left: 1380px; width: 120px; height: 120px">
  </form>
</div>"""
    
    html_file = open('Templates/abc Online Supermarket - Home Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Home Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Product(Fruits) Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Product(Fruits) Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Product(Snacks) Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Product(Snacks) Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Product(Drinks and Beverages) Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Product(Drinks and Beverages) Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Product(Wines) Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Product(Wines) Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Product(Cleaning Supllies, Health and Beauty) Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Product(Cleaning Supllies, Health and Beauty) Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Product(Pets) Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Product(Pets) Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()  

    html_file = open('Templates/abc Online Supermarket - Contact Us Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Contact Us Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - About Us Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - About Us Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Jobs Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Jobs Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Register Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Register Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Help Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Help Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()

    html_file = open('Templates/abc Online Supermarket - Help Page Information.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Help Page Information.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()  

    html_file = open('Templates/abc Online Supermarket - Serach Product Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Serach Product Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close() 

    CUR.execute("""SELECT Discount FROM member
                 WHERE `User_Name(email)` = '""" + user_name + """'""")
    global discount
    discount = CUR.fetchone()
    discount = str(discount).replace('(', '')
    discount = str(discount).replace(')', '')
    discount = str(discount).replace(',', '') 
    DB.commit()

    if discount == "'5%'":
      replace_location = """document.getElementById("discount").innerHTML = "0% OFF  (Non-member)"
total_price = Math.floor(total_price*1)"""
      replace_new_value = """document.getElementById("discount").innerHTML = "5% OFF  (Ordinary Member)"
total_price = Math.floor(total_price*0.95)"""
      html_file = open('Templates/abc Online Supermarket - Information Comfirm Page.html')
      old_content = html_file.read()
      new_content = old_content.replace(replace_location, replace_new_value)  
      with open("Templates/abc Online Supermarket - Information Comfirm Page.html", "w") as html_file:
        html_file.write(new_content)
      html_file.close()

    elif discount == "'10%'":
      replace_location = """document.getElementById("discount").innerHTML = "0% OFF  (Non-member)"
total_price = Math.floor(total_price*1)"""
      replace_new_value = """document.getElementById("discount").innerHTML = "10% OFF  (Elder Member)"
total_price = Math.floor(total_price*0.9)"""
      html_file = open('Templates/abc Online Supermarket - Information Comfirm Page.html')
      old_content = html_file.read()
      new_content = old_content.replace(replace_location, replace_new_value)  
      with open("Templates/abc Online Supermarket - Information Comfirm Page.html", "w") as html_file:
        html_file.write(new_content)
      html_file.close()
      
    return """<html><body>
                <script>
                  alert("You have successfully login!")
                  window.history.back();
                </script>
              </body></html>"""    

  #"None" means the username and password not match, or username doesn't exist
  else:
    return """<html><body>
                <script>
                  alert("Incorrect Username or Password!")
                  window.history.back();
                </script>
              </body></html>"""
  
  #with open("Templates/abc Online Supermarket - Home Page.html", "w") as html_file:
    #html_file.write("yes")  


@app.route("/logout")
def logout():
  replace_location = """<!-- Logout function -->
  <div>
  <div style="position: absolute; top: 30px; left: 1100px; text-align: center; font-size: 30px"><b>Welcome Back!</b>
    <div style="margin-top: -10px; color: blue"><h3><b><i>""" + lname.replace("'", "") + """</i></b></h3></div>
  </div>

  <form action="http://localhost:5000/logout">
     <input type="image" src="Image/Button Logo/Logout Logo.png" alt="Logout Logo"
     style="position: absolute; top: 5px; left: 1380px; width: 120px; height: 120px">
  </form>
</div>"""
  replace_new_value = """<!-- Login function -->
<button class="login-btn" onclick="document.getElementById('login_form').style.display='block'"><h1><b>Login</b></h1></button>
<div id="login_form" class="modal">
  <form class="modal-content animate" action="http://localhost:5000/login" method="post">
    <div class="imgcontainer">
      <span onclick="document.getElementById('login_form').style.display='none'" class="close" title="Close Modal">&times;</span>
      <img src="Image/Background Logo/Login Logo.png" alt="User" class="user">
    </div>

    <div class="login_container">
      <div class="label_font_size">
      <label><b>Username</b></label>
        <i>
          <input type="text" placeholder=" Enter your username" name="user_name" id="user_name" autocomplete="off" required>
        </i>
      </div>

      <p class="label_font_size">
      <label><b>Password</b></label>
        <i>
          <input type="password" placeholder=" Enter your password" name="password" id="password" required>
        </i>
      </p>

      <p>
        <b><input type="submit" class="inside-login_btn" value="Login"></b>
      </p>

      <br>
      <br>
       
    </div> 

      <div class="down_container">
        <pre style="line-height: 18px">    
       <a href="abc Online Supermarket - Register Page.html" style="color: blue; font-size: 18px">Sign Up</a>                                <a href="abc Online Supermarket - Find Password.html" style="color: black; cursor: pointer; font-size: 18px">Forget Password?</a>
        </pre> 
        <br>      
      </div>     
  </form>
</div>"""

  html_file = open('Templates/abc Online Supermarket - Home Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Home Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Product(Fruits) Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Product(Fruits) Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Product(Snacks) Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Product(Snacks) Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Product(Drinks and Beverages) Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Product(Drinks and Beverages) Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Product(Wines) Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Product(Wines) Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Product(Cleaning Supllies, Health and Beauty) Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Product(Cleaning Supllies, Health and Beauty) Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Product(Pets) Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Product(Pets) Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()  

  html_file = open('Templates/abc Online Supermarket - Contact Us Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Contact Us Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - About Us Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - About Us Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Jobs Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Jobs Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Register Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Register Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Help Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Help Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  html_file = open('Templates/abc Online Supermarket - Help Page Information.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Help Page Information.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()  

  html_file = open('Templates/abc Online Supermarket - Serach Product Page.html')
  old_content = html_file.read()
  new_content = old_content.replace(replace_location, replace_new_value)  
  with open("Templates/abc Online Supermarket - Serach Product Page.html", "w") as html_file:
    html_file.write(new_content)
  html_file.close()

  if discount == "'5%'":
    replace_location = """document.getElementById("discount").innerHTML = "5% OFF  (Ordinary Member)"
total_price = Math.floor(total_price*0.95)"""
    replace_new_value = """document.getElementById("discount").innerHTML = "0% OFF  (Non-member)"
total_price = Math.floor(total_price*1)"""
    html_file = open('Templates/abc Online Supermarket - Information Comfirm Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Information Comfirm Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()
    
  elif discount == "'10%'":
    replace_location = """document.getElementById("discount").innerHTML = "10% OFF  (Elder Member)"
total_price = Math.floor(total_price*0.9)"""
    replace_new_value = """document.getElementById("discount").innerHTML = "0% OFF  (Non-member)"
total_price = Math.floor(total_price*1)"""
    html_file = open('Templates/abc Online Supermarket - Information Comfirm Page.html')
    old_content = html_file.read()
    new_content = old_content.replace(replace_location, replace_new_value)  
    with open("Templates/abc Online Supermarket - Information Comfirm Page.html", "w") as html_file:
      html_file.write(new_content)
    html_file.close()
    
  return """<html><body>
              <script>
                window.history.back();
              </script>
            </body></html>"""




if __name__=='__main__':
  app.run()

DB.close()
#https://stackoverflow.com/questions/48251473/how-to-write-to-a-specific-position-inside-a-html-in-python  
