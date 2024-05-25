let person = window.close("hello", "harsha")
console.log(person)

function msg(){  
    setTimeout(function(){  
        alert("Welcome to Javatpoint after 2 seconds")
    },2000);  
      
}  

document.addEventListener("DOMContentLoaded", function(){
    document.getElementById("productForm").addEventListener("submit", function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        var prod = document.getElementById('product_name').value;
        if (prod =='iphone 13'){
            console.log(prod)

        }else if (prod == ""){
            console.log(prod,+","+" not iphone")
            alert("Name must be filled out");
        }
    })
});
