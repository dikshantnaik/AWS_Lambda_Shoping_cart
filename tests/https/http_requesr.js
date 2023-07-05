// const fetch = require("node-fetch");

// import "node-fetch";
import fetch from "node-fetch";

const url =
  "https://a0aq2g3pdh.execute-api.us-east-1.amazonaws.com/default/add_product_2";
const payload = {
  product_id: "awdd",
  product_name: "Banana",
  product_price: 500,
  product_category: "fruit",
};

fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(payload),
})
  .then((response) => response.json())
  .then((data) => {
    console.log("Response:", data);
    // Handle the response data here
  })
  .catch((error) => {
    console.error("Error:", error);
    // Handle any errors that occurred during the request
  });
