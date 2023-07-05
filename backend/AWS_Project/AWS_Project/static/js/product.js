document.addEventListener("DOMContentLoaded", function () {
  var addToCartButtons = document.querySelectorAll(".add-to-cart");

  addToCartButtons.forEach(function (button) {
    button.addEventListener("click", function (event) {
      event.preventDefault();
      var productId = this.getAttribute("data-product-id");

      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/api/add_to_cart/", true);
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          var response = JSON.parse(xhr.responseText);
          var cardId = response.card_id;

          // Set the card ID in a cookie
          document.cookie = "cardId=" + cardId + "; path=/";

          // Perform any additional actions or UI updates
          alert("Product added to cart successfully!");
        }
      };

      var data = "product_id=" + encodeURIComponent(productId);
      xhr.send(data);
    });
  });
});
