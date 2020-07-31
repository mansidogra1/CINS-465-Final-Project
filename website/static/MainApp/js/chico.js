var app = angular.module('myapp', []);

app.controller('myctrl', function($scope, $http, $window, $timeout) {

// Show Header Buttons
$scope.ShowButtons=function(){
    $http({
        method:"GET",
        url:"/hide_button/",
        // data:{'username':username}
    }).then(
    function (success){
        console.log(success.data);
        $scope.success=success.data;
        $scope.hider_data=true;
        $scope.show_data=false;
        console.log('show_data',$scope.show_data);
        console.log('hidder_data',$scope.hider_data);
            $timeout(function(){
        },10000);
    },function(error){
        console.log(error.data);
        $scope.err=true;
        $timeout(function(){
        },10000);
        $scope.hider_data=false;
        $scope.show_data=true;
    });
}

// Register Function    
$scope.registerUser=function(){

    console.log($scope.reg_user);
    console.log($scope.reg_stu_id);
    console.log($scope.reg_email);
    console.log($scope.reg_pass);

    if($scope.reg_user==undefined || $scope.reg_stu_id==undefined || $scope.reg_email==undefined || $scope.reg_pass==undefined){
        alert('Please Fill The Details');
        return;
    }

    $http({
            method:"POST",
            url:"/signup/",
            data:{
                'username':$scope.reg_user,
                'studentId':$scope.reg_stu_id,
                'email':$scope.reg_email,
                'password':$scope.reg_pass
            }
        }).then(
        function (success){
            console.log(success.data);
            $scope.success=success.data.message;
            $scope.reg_user='';
            $scope.reg_stu_id='';
            $scope.reg_email='';
            $scope.reg_pass='';

            $scope.success=" Saved";
        
        
            $timeout(function(){
            },10000);
            alert(success.data.message);
            window.location= '/';
        },function(error){
            console.log(error.data);
            $timeout(function(){
            },10000);
            $scope.error=error.data;
            alert(error.data['message']);
        });
}

// Login Function
$scope.login=function() {
    console.log($scope.login_user);
    console.log($scope.login_pass);
    if($scope.login_user==undefined || $scope.login_pass==undefined){
        alert('Please Fill The Details');
        return;
    }
    $http({
        method:"POST",
        url:"/user_login/",
        data:{'username':$scope.login_user,'password':$scope.login_pass}
    }).then(
            function (success){
                console.log(success.data);
                $scope.success=success.data.message;
                $scope.login_user='';
                $scope.login_pass='';
                $timeout(function(){
                },10000);
                window.location= '/';
                // window.location.reload();
                // $scope.correct()
            },function(error){
                    $scope.showerror=true;
                    console.log(error.data);
                    $timeout(function(){
                    },10000);
                    $scope.error=error.data["message"];
                    alert(error.data['message']);
            });
};

$scope.openMenu = function(cid) {
    console.log('cid', cid);
    localStorage.setItem("cid", cid);
    window.location= '/menu';
}
$scope.addItem = function(id) {
    for (let index = 0; index < $scope.product_data.length; index++) {
        if($scope.product_data[index].id == id) {
            $scope.product_data[index].current_quantity = 1;
        }
    }
    
}

$scope.increaseItem = function(id) {
    for (let index = 0; index < $scope.product_data.length; index++) {
        if($scope.product_data[index].id == id) {
            if($scope.product_data[index].current_quantity >= $scope.product_data[index].quantity) {
                alert(`Can not add more than ${$scope.product_data[index].quantity} of this item.`)
            } else {
                $scope.product_data[index].current_quantity += 1;
            }
        }
    }
    
    
}
$scope.decreaseItem = function(id) {
    for (let index = 0; index < $scope.product_data.length; index++) {
        if($scope.product_data[index].id == id) {
            if($scope.product_data[index].current_quantity > 0) {
                $scope.product_data[index].current_quantity -= 1;
            } 
        }
    }
    
}
$scope.buyNow = function() {
    var final_products = [];
      for(var i=0; i < $scope.product_data.length; i++) {
        if($scope.product_data[i].current_quantity >= 1) {
            final_products.push($scope.product_data[i]);
        } 
      }
      console.log('final_products', final_products);
      $http({
        method:"POST",
        url:"/update_products/",
        data:{'data':final_products}
    }).then(
            function (success){
                console.log(success.data);
                $scope.success=success.data.message;
                $timeout(function(){
                },10000);
                alert('Thank You For Placing Your Order.');
                window.location= '/';
                // window.location.reload();
                // $scope.correct()
            },function(error){
                    $scope.showerror=true;
                    console.log(error.data);
                    $timeout(function(){
                    },10000);
                    $scope.error=error.data["message"];
                    alert(error.data['message']);
            });
}

$scope.clearAll = function() {
      for(var i=0; i < $scope.product_data.length; i++) {
        if($scope.product_data[i].current_quantity >= 1) {
            $scope.product_data[i].current_quantity = 0;
        } 
      }
}

// Get Category Name
$scope.GetCategory=function(){
    $http({
        method:"GET",
        url:"/get_category/",
        // data:{'username':username}
    }).then(
    function (success){
        console.log(success.data);
        $scope.category_data=success.data.message;
        console.log('category',$scope.category_data);
            $timeout(function(){
        },10000);
    },function(error){
        console.log(error.data);
        $timeout(function(){
        },10000);
    });
}

// Get Product Name
$scope.GetProduct=function(){
    $scope.all_pdts = true;
    $http({
        method:"GET",
        url:"/get_product/",
        // data:{'username':username}
    }).then(
    function (success){
        console.log(success.data);
        $scope.product_data=success.data.message;
        $scope.products = $scope.product_data;
        $scope.filterProduct();
            $timeout(function(){
        },10000);
    },function(error){
        console.log(error.data);
        $timeout(function(){
        },10000);
    });
}

$scope.filterProduct = function() {
    $scope.products = [];
//    var cid = await getCid();
   if(!$scope.cid) {
        $scope.all_pdts = true;
       $scope.products = $scope.product_data
   } else {
        $scope.getParticularPdt($scope.cid);
   }
   
   localStorage.clear();
}

$scope.getParticularPdt = function(cid) {
    $scope.price = 0;
    $scope.all_pdts = false;
    $scope.products = [];
    $scope.c_id = cid;
    for(var i=0; i < $scope.product_data.length; i++) {
        if($scope.product_data[i].category_id == parseInt(cid)) {
            $scope.products.push($scope.product_data[i]);
        }
    }
}

$scope.showClear = function() {
    var clear_check = false;
    for(var i=0; i < $scope.product_data.length; i++) {
        if($scope.product_data[i].current_quantity >= 1) {
            clear_check = true;
            break;
        } 
      }
      return clear_check;
}

$scope.getcid = function() {
    $scope.cid = parseInt(localStorage.getItem('cid'));

}

$scope.AllProductDetails = function() {
    $scope.products = $scope.product_data;
    $scope.all_pdts = true;
}

$scope.totalPrice = function() {
    var price = 0;
    for(var i=0; i < $scope.product_data.length; i++) {
        price += $scope.product_data[i].current_quantity * $scope.product_data[i].price;
      }
    return price;
}

});

