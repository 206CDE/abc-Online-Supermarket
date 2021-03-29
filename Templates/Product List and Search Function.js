//Function "search product" that combine search logo button and container
function search_product() {
  if (document.getElementById("search_product_value").value != "")
    {localStorage.setItem("product", document.getElementById("search_product_value").value);
     window.location.href = "abc Online Supermarket - Serach Product Page.html";
     document.getElementById("search_product_value").value = ""}
};


function find_product() {
    document.getElementById("product_list").innerHTML = 
    //All list of product
    `
    <ul id="ul">
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Apple")'>Apple</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Bananas")'>Bananas (1 comb)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Orange")'>Orange</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Green Grapes (1 bunch)")'>Green Grapes (1 bunch)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Purple Grapes (1 bunch)")'>Purple Grapes (1 bunch)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cherries (1 bunch)")'>Cherries (1 bunch)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Kiwi")'>Kiwi</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Lemon")'>Lemon</a>
      </li>   

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Mango")'>Mango</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Pineapple")'>Pineapple</a>
      </li>    

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Watermelon")'>Watermelon</a>
      </li> 

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Strawberries (1lb)")'>Strawberries (1lb)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Chocolate Bar (100g)")'>Chocolate Bar (100g)</a>
      </li>   

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Milk Chocolate Bar (100g)")'>Milk Chocolate Bar (100g)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Chocolate Biscuit Sticks (70g)")'>Chocolate Biscuit Sticks (70g)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cookies & Cream Biscuit Sticks (70g)")'>
      Cookies and CreamBiscuit Biscuit Sticks (70g)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Strawberry Biscuit Sticks (70g)")'>Strawberry Biscuit Sticks (70g)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Chocolate Mini Swiss Roll (60g)")'>Chocolate Mini Swiss Roll (60g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Peanut Mini Swiss Roll (60g)")'>Peanut Mini Swiss Roll (60g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Mango Mini Swiss Roll (60g)")'>Mango Mini Swiss Roll (60g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Lemon Mini Swiss Roll (60g)")'>Lemon Mini Swiss Roll (60g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Biscuit Roll (200g)")'>Biscuit Roll (200g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Jam Biscuit (300g)")'>Jam Biscuit (300g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cookies (300g)")'>Cookies (300g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Potato Chips (226.8g)")'>Potato Chips (226.8g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Soft Candies (116g)")'>Soft Candies (116g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Marshmallows (150g)")'>Marshmallows (150g)</a>
      </li>      
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Popcorns (559.8g)")'>Popcorns (559.8g)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Lemon Tea (250mL)")'>Lemon Tea</a>
      </li> 

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Lemon Tea (6 packs - 250ml)")'>Lemon Tea (6 packs - 250ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Milk Tea (250ml)")'>Milk Tea (250ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Milk Tea (6 packs - 250ml)")'>Milk Tea (6 packs - 250ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Coca (330ml)")'>Coca (330ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Coca (8 cans - 330ml)")'>Coca (8 cans - 330ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cream Soda (330ml)")'>Cream Soda (330ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cream Soda (8 cans - 330ml)")'>Cream Soda (8 cans - 330ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Coffee (240ml)")'>Coffee (240ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Coffee (6 cans - 240ml)")'>Coffee (6 cans - 240ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Distilled Water (500ml)")'>Distilled Water (500ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Mineral Water (500ml)")'>Mineral Water (500ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Orange Juice (1gal)")'>Orange Juice (1gal)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Apple Juice (1gal)")'>Apple Juice (1gal)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Milk (1gal)")'>Milk (1gal)</a>
      </li> 

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Beer (650ml)")'>Beer (650ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Vodka (1L)")'>Vodka (1L)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Champagne (750ml)")'>Champagne (750ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Grape Wine (750ml)")'>Grape Wine (750ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "White Wine (750ml)")'>White Wine (750ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Red Wine (750ml)")'>Red Wine (750ml)</a>
      </li> 
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Whisky (375ml)")'>Whisky (375ml)</a>
      </li>

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Tissues (7 sheets)")'>Tissues (7 sheets)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Tissues (18 packs - 7 sheets)")'>Tissues (18 packs - 7 sheets)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Box Tissues (90 sheets)")'>Box Tissues (90 sheets)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Toilet Paper (10 rolls)")'>Toilet Paper (10 rolls)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Hand Towel")'>Hand Towel</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cotton Tips (300pcs)")'>Cotton Tips (300pcs)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Body Lotion (400ml)")'>Body Lotion (400ml)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Shampoo (400ml)")'>Shampoo (400ml)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Body Wash (1L)")'>Body Wash (1L)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Toothbrush (3 packs)")'>Toothbrush (3 packs)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Toothpaste (170g)")'>Toothpaste (170g)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Hand Sanitizer (520ml))'>Hand Sanitizer (520ml)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Hand Wash (520ml)")'>Hand Wash (520ml)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Laundry Powder (1.6kg)")'>Laundry Powder (1.6kg)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Dish Soap (828ml)")'>Dish Soap (828ml)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Floor Cleaner (2L)")'>Floor Cleaner (2L)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cat Food - Dry (3kg)")'>Cat Food - Dry (3kg)</a>
      </li>  

      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Dog Food - Dry (3kg)")'>Dog Food - Dry (3kg)</a>
      </li>  
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cat Treats - Chicken (4 packs - 56g)")'>Cat Treats - Chicken (4 packs - 56g)</a>
      </li>  
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cat Threat - Salmon Soft (482g)")'>Cat Threat - Salmon Soft (482g)</a>
      </li>  
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Dog Treat - Marrowbone (500g)")'>Dog Treat - Marrowbone (500g)</a>
      </li>  
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Dog Treat - Biscuits (500g)")'>Dog Treat - Biscuits (500g)</a>
      </li>  
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Cat Accessory - Catsan (5L)")'>Cat Accessory - Catsan (5L)</a>
      </li>  
      
      <li><a href="abc Online Supermarket - Serach Product Page.html" 
      onclick='localStorage.setItem("product", "Dog Accessory - Leash & Collar")'>Dog Accessory - Leash & Collar</a>
      </li>  
    </ul>
    `;
  
 
    //Try find the product name that match or similar to the user "serach product" input
    input = document.getElementById("search_product_value");
    filter = input.value.toUpperCase();
    ul = document.getElementById("ul");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        search_value = a.textContent || a.innerText;
        if (search_value.toUpperCase().indexOf(filter) > -1 & document.getElementById("search_product_value").value != "") 
          {li[i].style.display = "";
           ul.style = `outline: 3px solid black; overflow: auto; width: 278px; height: 320px`}   
        else 
          {li[i].style.display = "none"};   
      }
};

//When the user click other place instead of the search bar, the search result will disable
function not_click_search() {
  window.onclick = function disable() {ul.style.display = "none"}
}


//If "Enter" pressed, the current page will change to serach product page
document.getElementById("search_product_value").addEventListener("keyup", function(event) {
  if (event.key == "Enter") {
    if (document.getElementById("search_product_value").value != "") {
      localStorage.setItem("product", document.getElementById("search_product_value").value);
                            window.location.href = "abc Online Supermarket - Serach Product Page.html";
                            document.getElementById("search_product_value").value = ""}   
  }
})