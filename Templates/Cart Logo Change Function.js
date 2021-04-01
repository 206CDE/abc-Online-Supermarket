//If any item added in the shopping cart, the shopping cart logo(button) style will change to notification button's  

if (localStorage.getItem("item_list") != null & localStorage.getItem("item_list").split(",").length>0){
  document.getElementById("shopping_cart_logo_notification").innerHTML = 
  `<div class="shopping-cart-logo-notification">`+localStorage.getItem("item_list").split(",").length+`</div>`
}