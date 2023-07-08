## CSTI Zafiyeti

Aşağıdaki kod örneğini inceleyebilirsiniz.
```
<!DOCTYPE html>
<html ng-app="myApp">
<head>
    <title>Shopping Cart</title>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.9/angular.min.js"></script>
</head>
<body>
    <div ng-controller="CartController">
        <h1>Shopping Cart</h1>
        <ul>
            <li ng-repeat="product in cart">{{product.name}} - {{product.price}} TL</li>
        </ul>
        <input type="text" ng-model="newProduct.name" placeholder="Product Name">
        <input type="number" ng-model="newProduct.price" placeholder="Product Price">
        <button ng-click="addToCart(newProduct)">Add to Cart</button>
    </div>
<script>
    // Initializing the myApp module
    var myApp = angular.module('myApp', []);
    
    // Defining the CartController and injecting dependencies
    myApp.controller('CartController', ['$scope', function($scope) {
        // Initial value for the cart
        $scope.cart = [
            { name: 'Apple', price: 2 },
            { name: 'Pear', price: 3 },
            { name: 'Orange', price: 4 }
        ];

        // Adding a new product to the cart
        $scope.addToCart = function(newProduct) {
            // Simulating sending the product to the backend
            simulateBackendRequest(newProduct)
                .then(function(response) {
                    // Update the cart when successfully added
                    $scope.cart.push(newProduct);
                    $scope.newProduct = {}; // Clear the form
                })
                .catch(function(error) {
                    // Show an error message to the user in case of failure
                    console.error(error);
                    alert('An error occurred while adding the product to the cart.');
                });
        };

        // Function for simulating the backend request
        function simulateBackendRequest(product) {
            return new Promise(function(resolve, reject) {
                // Simulating the process of adding a product to the backend
                setTimeout(function() {
                    // Simulating a random success or failure scenario
                    var success = Math.random() < 0.8; // 80% success rate

                    if (success) {
                        resolve('Product added successfully.');
                    } else {
                        reject('An error occurred while adding the product.');
                    }
                }, 1000); // Simulating a 1-second delay
            });
        }
    }]);
</script>
</body>
</html>

```

Kod örneğinden sonra mutlaka medium hesabımı takip edip makalemi okumanızı öneririm. Aynı zamanda bunun tam olarak simüle edilmiş halini day5 içerisinden bulabilirsiniz.

(Medium Makalesi)[https://medium.com/@batuhanaydinn/bug-bounty-hunter-lets-look-at-the-csti-attack-method-from-every-angle-200aabae2bab]