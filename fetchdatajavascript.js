const ipworks = require("@nsoftware/ipworks");

const http = new ipworks.http();

http.on("Transfer", function(e) {
  try {
    const jsonData = JSON.parse(e.text.toString());

    if (jsonData && jsonData.products && Array.isArray(jsonData.products)) {
      jsonData.products.forEach(product => {
        if (product.title) {
          console.log("Title: "+product.title);
        }
      });
    } else {
      console.log("No products found in the JSON data or invalid structure.");
    }
  } catch (error) {
    console.error("Error parsing JSON:", error.message);
  }
})
.on("SSLServerAuthentication", function(e) {
  e.accept = true;
});

http.setFollowRedirects(1);

const url = "https://dummyjson.com/products";

http.get(url).catch((err) => {
  console.log(err.message);
});
